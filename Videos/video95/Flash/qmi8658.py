import time
from machine import Pin, I2C

QMI8658_WHO_AM_I = 0x00
QMI8658_REVISION_ID = 0x01
QMI8658_CTRL1 = 0x02
QMI8658_CTRL2 = 0x03
QMI8658_CTRL7 = 0x08
QMI8658_ACC_X_L = 0x35

class QMI8658:
    def __init__(self, i2c, address=0x6B):
        self.i2c = i2c
        self.address = address
        
        # Verify chip ID
        chip_id = self.i2c.readfrom_mem(self.address, QMI8658_WHO_AM_I, 1)[0]
        if chip_id != 0x05:
            raise RuntimeError(f"QMI8658 not found. Found ID: {hex(chip_id)}")
            
        # Initialize the IMU
        self._write_reg(QMI8658_CTRL1, 0b00000000) # No change in serial interface
        self.enable_acc()
        self.enable_gyro()

    def _write_reg(self, reg, value):
        self.i2c.writeto_mem(self.address, reg, bytes([value]))

    def enable_acc(self, enable=True):
        val = 0x01 if enable else 0x00
        # CTRL2: Acc enable, ODR 1000Hz, +/- 2g
        self._write_reg(QMI8658_CTRL2, 0b00110000 | val)

    def enable_gyro(self, enable=True):
        val = 0x01 if enable else 0x00
        # CTRL3: Gyro enable, ODR 1000Hz, +/- 512dps
        self._write_reg(QMI8658_CTRL2 + 1, 0b01010000 | val)
        # CTRL7: Enable both accelerometer and gyroscope
        self._write_reg(QMI8658_CTRL7, 0b00000011)

    def read_xyz(self):
        # Read 12 bytes of raw sensor data (accel XYZ, gyro XYZ)
        data = self.i2c.readfrom_mem(self.address, QMI8658_ACC_X_L, 12)
        
        # Convert raw bytes to signed 16-bit integers
        xyz = [0] * 6
        for i in range(6):
            val = data[i*2] | (data[i*2 + 1] << 8)
            if val >= 32768:
                val -= 65536
            xyz[i] = val
            
        # Apply scaling divisors (assuming defaults: +/-2g, +/-512dps)
        acc_scale = 16384.0  # LSB / g
        gyro_scale = 64.0    # LSB / dps
        
        return [
            xyz[0] / acc_scale, xyz[1] / acc_scale, xyz[2] / acc_scale,
            xyz[3] / gyro_scale, xyz[4] / gyro_scale, xyz[5] / gyro_scale
        ]
