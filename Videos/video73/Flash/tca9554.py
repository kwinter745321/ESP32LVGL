# tca9554.py
# Updated:    30 January 2026 to support CTP_ft6x36 driver via tca9554
# Updated by: KWServices
#
# Copyright (C) 2026 KW Services.
# MIT License
# MicroPython v1.20.0-2510.gacfeb7b7e.dirty on 2025-11-23;
# Generic ESP32S3 module with ESP32S3
# Verified on: Waveshare ESP32-S3-Touch-LCD-3.5C
# LVGL 9.3
#
# Revised for MicroPython
# From pca9554 driver written by TjazVracko (IRNAS LTD) GPL 2.0 license


"""
Pca9554 driver, NXP Semiconductors
8 bit I2C expander, 8 GPIO ports
I2C SMBus protocol
Manual: PCA9554_9554A.pdf
"""
#import smbus
from machine import SoftI2C, Pin
#import logging

# selected i2c channel on rpi
I2C_CHANNEL = 1

# Define command byte registers
IN_REG = 0x00   # Input register
OUT_REG = 0x01  # Output register
POL_REG = 0x02  # Polarity inversion register
CONF_REG = 0x03  # Config register (0=output, 1=input)

OUTPUT = 0
INPUT = 1


class TCA9554(object):
    def __init__(self, address):
        """Init i2c channel and tca9554 driver on specified address."""
        try:
            self.PORTS_COUNT = 8    # number of GPIO ports
            self.i2c_bus = SoftI2C( scl=Pin(7), sda=Pin(8), freq=40000)
            self.i2c_address = address
        except ValueError:
            print("No pca9554 device found on specified address!")
            self.i2c_bus = None
        except:
            print("Bus on channel {} is not available.".format(I2C_CHANNEL))
            print("Available busses are listed as /dev/i2c*")
            self.i2c_bus = None

    def read_input_register(self):
        """Read incoming logic levels of the ports (returns actual pin value)."""
        try:
            return self.i2c_bus.readfrom_mem(self.i2c_address, IN_REG, 1)
        except:
            return None

    def read_output_register(self):
        """Read outgoing logic levels of the ports defined as outputs (returns flip-flop controlling the output select)."""
        try:
            return self.i2c_bus.readfrom_mem(self.i2c_address, OUT_REG, 1)
        except:
            return None

    def read_polarity_inversion_register(self):
        """Read if the polarity of input register ports data is inverted (returns for each pin: 1=inverted or 0=retained)."""
        try:
            return self.i2c_bus.readfrom_mem(self.i2c_address, POL_REG, 1)
        except:
            return None

    def read_config_register(self):
        """Read configuration of all ports (returns for each pin 1=input or 0=output)."""
        try:
            return self.i2c_bus.readfrom_mem(self.i2c_address, CONF_REG, 1)
        except:
            return None

    def read_port(self, port_num):
        """Read port bit value (high=1 or low=0)."""
        try:
            line_value = self.i2c_bus.readfrom_mem(self.i2c_address, IN_REG, 1)
            #print("line:",hex(line_value[0]))
            ret = ((line_value[0] >> port_num) & 1)
            return ret
        except:
            print("read_port error")
            return None

    def write_port(self, port_num, state):
        """Write port bit specified in port_num to state value: 0=low, 1=high. Returns True if successful."""
        try:
            current_value = self.i2c_bus.readfrom_mem(self.i2c_address, OUT_REG, 1)
            #print("current:",hex(current_value[0]))
            if state:
                new_value = current_value[0] | 1 << port_num
            else:
                new_value = current_value[0] & (255 - (1 << port_num))
            #print("new:",hex(new_value))
            #self.i2c_bus.write_byte_data(self.i2c_address, OUT_REG, new_value)
            self.i2c_bus.writeto_mem(self.i2c_address, OUT_REG, bytes([new_value]))
            return True
        except:
            print("write_port error")
            return False

    def write_output_register(self, value):
        """Write all ports to states specified in byte value (each pin bit: 0=low, 1=high). Returns True if successful."""
        try:
            if value < 0x00 or value > 0xff:
                return False
            self.i2c_bus.writeto_mem(self.i2c_address, OUT_REG, bytes([value]) )
            return True
        except:
            return False

    def write_polarity_inversion_register(self, value):
        """Write polarity (1=inverted, 0=retained) for each input register port data (value has all ports polarities). Returns True if successful."""
        try:
            if value < 0x00 or value > 0xff:
                return False
            self.i2c_bus.writeto_mem(self.i2c_address, POL_REG, bytes([value]))
            return True
        except:
            return False

    def write_config_register(self, value):
        """Write all ports to desired configuration (1=input or 0=output), parameter: value (type: byte). Returns True if successful."""
        try:
            if value < 0x00 or value > 0xff:
                return False
            self.i2c_bus.writeto_mem(self.i2c_address, CONF_REG, bytes([value]))
            return True
        except:
            return False

    def write_config_port(self, port_num, state):
        """Write port configuration (specified by port_num) to desired state: 1=input or 0=output. Returns True if successful."""
        try:
            if port_num < 0 or port_num >= self.PORTS_COUNT:
                return False
            if state < 0 or state > 1:
                return False
            current_value = self.i2c_bus.readfrom_mem(self.i2c_address, CONF_REG, 1)
            if state:
                new_value = current_value[0] | 1 << port_num
            else:
                new_value = current_value[0] & (255 - (1 << port_num))
            self.i2c_bus.writeto_mem(self.i2c_address, CONF_REG, bytes([new_value]))
            return True
        except:
            return False

    def __del__(self):
        """Driver destructor."""
        self.i2c_bus = None

