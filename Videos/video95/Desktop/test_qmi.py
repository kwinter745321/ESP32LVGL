import time
from machine import Pin, I2C, SoftI2C
from qmi8658 import QMI8658

# Initialize I2C (adjust pins according to your specific board's schematic)
i2c = SoftI2C(scl=Pin(10), sda=Pin(11), freq=400000)

try:
    imu = QMI8658(i2c)
    print("QMI8658 initialized successfully!")
except RuntimeError as e:
    print(e)

while True:
    try:
        # Read acceleration (g) and gyroscope (dps)
        acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z = imu.read_xyz()
        
        print(f"Accel: X:{acc_x: .2f}g, Y:{acc_y: .2f}g, Z:{acc_z: .2f}g")
        print(f"Gyro:  X:{gyro_x: .2f}°/s, Y:{gyro_y: .2f}°/s, Z:{gyro_z: .2f}°/s")
        print("-" * 40)
        
    except Exception as e:
        print("Error reading sensor:", e)
        
    time.sleep(0.5)
