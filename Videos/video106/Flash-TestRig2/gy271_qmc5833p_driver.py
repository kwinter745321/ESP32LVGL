from machine import SoftI2C, Pin
from math import atan2, pi
import struct, time
import gc

class Magnetometer:
    def __init__(self, scl, sda):
        """
        Driver for the QMC5883P magnetometer chip, commonly found on the GY-271 module.
        
        Required input parameters: SCL pin number, SDA pin number
        
        The chip is set up to the following parameters:
         - Normal power mode
         - 200Hz data output rate
         - 4x sensor reads per data output
         - No down sampling
         - 2 Gauss sensor range
         - Set and reset mode on
        
        Potential methods:
            getdata_raw() - returns the raw magnetometer readings in Gauss
            compass_2d(declination=...) - returns a heading rounded to the nearest degree (no pitch/roll compensation). Magnetic declination input optional.
            compass_3d(q, declination=...) - returns a heading rounded to the nearest degree. Fully pitch/roll compensated. Quaternion orientation input required, magnetic declination optional.
            calibrate(calibrationrotations=...) - enables you to calibrate the sensor. calibrationrotations optional. See the docstring in the calibrate() method for details on the calibration.
        """
        self.qmc5883p = SoftI2C(scl=Pin(scl), sda=Pin(sda), freq=400000)
        self.qmc5883p_address = 0x2C
    
        self.registers = {
                    "chipid" : 0x00,
                    
                    "x-axis data" : 0x01,
                    "y-axis data" : 0x03,
                    "z-axis data": 0x05,
                    "axis invert" : 0x29,
                    
                    "status" : 0x09,
                    "control1" : 0x0A,
                    "control2" : 0x0B,
                    }
        
        self.data = [0, 0, 0]
        self.softcal = [1, 1, 1]
        self.hardcal = [0, 0, 0]
        
        # Module needs about 250 microseconds to boot up from power on -> being able to receive I2C comms
        time.sleep_us(250)
        
        self._modulesetup()
    
    def _log(self, string):
        print(string)
        
    def _modulesetup(self):
        # Setting the module to Normal power mode, 200Hz data output rate, x4 sensor reads per data output, down sampling = 0 (output every sample)
        self.qmc5883p.writeto_mem(self.qmc5883p_address, self.registers["control1"], bytes([0x1D]))
        # Setting the module to 2 Gauss range, "Set and Reset On" mode
        self.qmc5883p.writeto_mem(self.qmc5883p_address, self.registers["control2"], bytes([0x0C]))
        
        self._log("Module setup complete")
    
    @micropython.native
    def _update_data(self):
        counter = 0
        
        # Checking the DRDY bit of the status register - if no new data, wait a bit then check again
        while not(self.qmc5883p.readfrom_mem(0x2C, 0x09, 1)[0] & 0x01):
            # 1/200 of a second - time it should take for a measurement
            time.sleep_us(5)
            counter += 1
            
            if counter > 2:
                return None
            
        # Reading all 6 data bytes in one burst
        data = self.qmc5883p.readfrom_mem(self.qmc5883p_address, self.registers["x-axis data"], 6)

        # Decoding the bytes data into signed ints, then converting the readings to Gauss
        x_axis = struct.unpack("<h", data[:2])[0]/15000
        y_axis = struct.unpack("<h", data[2:4])[0]/15000
        z_axis = struct.unpack("<h", data[4:])[0]/15000

        self.data[0] = (x_axis - self.hardcal[0]) * self.softcal[0]
        self.data[1] = (y_axis - self.hardcal[1]) * self.softcal[1]
        self.data[2] = (z_axis - self.hardcal[2]) * self.softcal[2]
        
        return True
    
    @micropython.native
    def _quat_rotate_mag_readings(self, q):
        qw, qx, qy, qz = q
        mx, my, mz = self._normalize(self.data)
        
        # Rotate magnetometer vector into world reference frame
        rx = (qw*qw + qx*qx - qy*qy - qz*qz)*mx + 2*(qx*qy - qw*qz)*my + 2*(qx*qz + qw*qy)*mz
        ry = 2*(qx*qy + qw*qz)*mx + (qw*qw - qx*qx + qy*qy - qz*qz)*my + 2*(qy*qz - qw*qx)*mz
        
        return rx, ry
    
    @micropython.native
    def _world_heading_vector(self, q):
        qw, qx, qy, qz = q
        local_heading = [-1, 0, 0]
        
        # Using quaternion rotation to find the world x/y heading vector
        wx = (qw*qw + qx*qx - qy*qy - qz*qz)*local_heading[0] + 2*(qx*qy - qw*qz)*local_heading[1] + 2*(qx*qz + qw*qy)*local_heading[2]
        wy = 2*(qx*qy + qw*qz)*local_heading[0] + (qw*qw - qx*qx + qy*qy - qz*qz)*local_heading[1] + 2*(qy*qz - qw*qx)*local_heading[2]
        
        return wx, wy
    
    @micropython.native
    def _normalize(self, vector):
        v1, v2, v3 = vector
        
        length = v1*v1 + v2*v2 + v3*v3
        length = length**0.5
        
        v1 /= length
        v2 /= length
        v3 /= length
        
        return [v1, v2, v3]
    
    def _axes_calibration_rotations(self, fieldstrength):
        x_values, y_values, z_values = [], [], []
        xcomplete, ycomplete, zcomplete = False, False, False
        
        x_values.append(self.data[0])
        y_values.append(self.data[1])
        z_values.append(self.data[2])
        
        self._log("Begin compass rotation")
        
        while not(xcomplete and ycomplete and zcomplete):
            gc.collect()
            #print("mem free:",gc.mem_free() )
            flag = self._update_data()
            
            if not xcomplete:
                x_values.append(self.data[0])
            if not ycomplete:
                y_values.append(self.data[1])
            if not zcomplete:
                z_values.append(self.data[2])
            
            # Detecting if that axis has had a full rotation and returned to the starting point. Only triggers once
            if (max(x_values)-min(x_values)) > 0.8*2*fieldstrength and abs(x_values[-1] - x_values[0]) < 0.1 and not xcomplete:
                xcomplete = True
                self._log("X axis complete")
            if (max(y_values)-min(y_values)) > 0.8*2*fieldstrength and abs(y_values[-1] - y_values[0]) < 0.1 and not ycomplete:
                ycomplete = True
                self._log("Y axis complete")
            if (max(z_values)-min(z_values)) > 0.8*2*fieldstrength and abs(z_values[-1] - z_values[0]) < 0.1 and not zcomplete:
                zcomplete = True
                self._log("Z axis complete")
                
            time.sleep_ms(10)
            
        return x_values, y_values, z_values
    
    def _hard_offsets(self, x_values, y_values, z_values, rotations):
        x_offset, y_offset, z_offset = 0, 0, 0
        
        x_offset = (sum(x_values[-rotations:])/rotations + sum(x_values[:rotations])/rotations)/2
        y_offset = (sum(y_values[-rotations:])/rotations + sum(y_values[:rotations])/rotations)/2
        z_offset = (sum(z_values[-rotations:])/rotations + sum(z_values[:rotations])/rotations)/2
        
        self.hardcal[0] = x_offset
        self.hardcal[1] = y_offset
        self.hardcal[2] = z_offset
    
    def _soft_offsets(self, x_values, y_values, z_values, rotations):
        x_offset, y_offset, z_offset = 0, 0, 0
        
        x_offset = (sum(x_values[-rotations:])/rotations - sum(x_values[:rotations])/rotations)/2
        y_offset = (sum(y_values[-rotations:])/rotations - sum(y_values[:rotations])/rotations)/2
        z_offset = (sum(z_values[-rotations:])/rotations - sum(z_values[:rotations])/rotations)/2
        
        offset_avg = (x_offset + y_offset + z_offset)/3
        
        x_scale = offset_avg/x_offset
        y_scale = offset_avg/y_offset
        z_scale = offset_avg/z_offset
        
        self.softcal[0] = x_scale
        self.softcal[1] = y_scale
        self.softcal[2] = z_scale
    
    def calibrate(self, calibrationrotations=2):
        """
        Calibration method for the magnetometer. Removes both hard- and soft-iron effects from the magnetometer readings
        
        To calibrate the sensor: Call the calibrate() method, hold the magnetometer and rotate it 360 degrees around ONE of its axes at a time.
        You will need to rotate the sensor 360 degrees around TWO DIFFERENT axes in order to complete the calibration rotations (i.e. rotate all 3 axes through 360 degrees)
        
        Parameters:
            calibrationrotations - the number of times it will expect you to complete the series of sensor rotations outlined above. Default is 2.
        
        No output - calibration values automatically saved and applied to the magnetometer readings.
        """
        self._log("Calibrating...")
        
        x_values, y_values, z_values = [], [], []
        fieldstrength = 0
        number_readings_fieldstrength = 20
        
        # Working out an approximate local magnetic field strength
        for i in range(number_readings_fieldstrength):

            flag = self._update_data()
            
            vector_length = self.data[0]*self.data[0] + self.data[1]*self.data[1] + self.data[2]*self.data[2]
            vector_length = vector_length**0.5
            
            fieldstrength += vector_length
            
            time.sleep_ms(5) # sensor operates at 200Hz - 4 milliseconds between new sensor data
            
        fieldstrength /= number_readings_fieldstrength
        
        self._log("Field strength determined")
        
        # Finding the average sensor range per axis
        for i in range(calibrationrotations+1):
            x, y, z = self._axes_calibration_rotations(fieldstrength)
            self._log("Calibration rotation {} complete".format(i+1))
            
            x_values.extend(x) # Adding data from next rotation to the arrays
            y_values.extend(y)
            z_values.extend(z)
        
        x_values = sorted(x_values)
        y_values = sorted(y_values)
        z_values = sorted(z_values)
        
        num_readings = max(calibrationrotations, int(((len(x_values)+len(y_values)+len(z_values))/3)//20)) # EITHER use the largest/smallest 5% of the average dataset length, OR the number of rotation sequences
        
        self._hard_offsets(x_values, y_values, z_values, num_readings)
        self._log("Hard iron calibration complete")
        
        self._soft_offsets(x_values, y_values, z_values, num_readings)
        self._log("Soft iron calibration complete")
            
    def getdata_raw(self):
        """
        Returns the raw magnetometer data in Gauss. Takes no parameters.
        
        Output is as a [magnetometer_x, magnetometer_y, magnetometer_z] list
        """
        flag = self._update_data()
        
        return self.data
    
    def compass_2d(self, declination=0):
        """
        Basic compass that doesn't include any pitch/roll compensation so only accurate when level. North is taken as the negative x-axis.
        
        Can take a parameter, declination (input as degrees, e.g. 1.5), which is different in every location. Default value is 0. If declination is given, then the output heading will be a true heading, instead of magnetic.
        
        Outputs a compass heading rounded to the nearest degree.
        """
        
        flag = self._update_data()
        
        heading = atan2(self.data[1], -self.data[0])*(180/pi) - declination
        
        # Ensuring heading values go from 0 to 360
        heading %= 360
        
        return int(heading+0.5) # Rounds to nearest degree
    
    @micropython.native
    def compass_3d(self, quat, declination=0):
        """
        Fully pitch and roll compensated compass, which is accurate at all orientations of the sensor. North is taken as the negative x-axis.
        
        Required parameter: Quaternion orientation of the sensor - formatted as a list [qw, qx, qy, qz]
        Optional parameter: Magnetic declination (input as degrees, e.g. 1.5), which is different in every location. Default value is 0. If declination is given, then the output heading will be a true heading, instead of magnetic.
        
        Outputs a compass heading rounded to the nearest degree.
        """
        
        flag = self._update_data()
        
        # Magnetic north direction vector - vector=[rx, ry, 0]
        rx, ry = self._quat_rotate_mag_readings(quat)
            
        # Device forward direction vector - vector=[wx, wy, 0]
        wx, wy = self._world_heading_vector(quat)
        
        # Dot product between the world heading vector and magnetic north direction vector
        dot_product = rx*wx + ry*wy
        # Cross product z component (x and y are 0)
        cross_product_z = rx*wy - ry*wx
        
        heading = atan2(cross_product_z, dot_product) * (180/pi) - declination
        # Heading calc maths: cross product = |a|*|b|*sin(theta), dot product = |a|*|b|*cos(theta)
        # So atan(crossproduct/dotproduct)=atan(sin(theta)/cos(theta))=atan(tan(theta))=theta
        
        # Ensuring heading goes from 0-360 degrees
        heading %= 360
        # Rounds to nearest degree
        return int(heading+0.5)
        

if __name__ == "__main__":
    import mpu6050 as MPU6050
    
    imu = MPU6050.MPU6050(41, 42)
    imu.dmpsetup(2)
    imu.calibrate(10)
    
    compass = Magnetometer(46, 3)
    compass.calibrate(1)
    
    while True:
        quaternion, orientation, localvel, worldacc = imu.imutrack()
        print(compass.compass_3d(quat=quaternion, declination=1.43))
        time.sleep(0.1)