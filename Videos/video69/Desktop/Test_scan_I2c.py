# Test_scan_I2c.py
#
# Updated: 24 December 2025
#
# License: MIT
#
# firmware: MicroPython v1.27.0 on 2025-12-09;
#   Generic ESP32P4 module with WIFI module
#   of external ESP32C6 with ESP32P4
#
from machine import Pin, I2C, SoftI2C
import machine
import time

##### flash drive ################
#nothing extra needed

##### definitions ################
I2C_PORT = 'I2C1'
I2C_SDA_PIN = 7 
I2C_SCL_PIN = 8
I2C_FREQ = 400000

#### Init #####################
scl = Pin(I2C_SCL_PIN, mode=Pin.OUT)
sda = Pin(I2C_SDA_PIN, mode=Pin.OUT)

i2c=machine.SoftI2C(scl=Pin(8),sda=Pin(7),freq=100000)                                                                                                                                  

#### Test Program #####################
try:
    print("----------------")
    print("Program started.")
    print("* Test scan of I2C devices.")
    print("* I2C is wired on MCU's %s port." % (I2C_PORT))
    print("*",i2c)
    print('Scanning I2C bus...')
    devices = i2c.scan() 
    print('Scan finished.')
    device_count = len(devices)

    if device_count == 0:
        print('No I2C device found.')
    else:
        print('I2C devices found:',device_count)
        print("| Decimal Address | Hex Address |")
        print("| --------------- | ----------- |")
        for device in devices:
            xdevice = str(hex(device))
            print("| %15s " % device,end="")
            print("| %9s " % xdevice," |")

except KeyboardInterrupt:
    done = True
    print('Interrupted by Control-c.')
finally:
    print('Finished.')
    

