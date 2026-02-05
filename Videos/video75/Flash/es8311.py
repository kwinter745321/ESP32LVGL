# es8311.py
#
# Created: 02 February 2026 (custom to the waveshare device)
# note: hard-coded the clock registers
# to-do: calculate clocks properly
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# Waveshare ESP32-S3-Touch-LCD-3.5C
# MicroPython v1.20.0-2510.gacfeb7b7e.dirty on 2025-11-23;
# Generic ESP32S3 module with ESP32S3

#from machine import reset, Pin,
#from machine import SoftI2C
import time

class ES8311():
    def __init__(self,i2c):
        self.i2c = i2c
        self.i2c_address = 0x18
        self.volume = 50

    def write_reg(self, reg, val):
        self.i2c.writeto_mem(self.i2c_address, reg, bytes([val]))
        
    def read_reg(self, reg):
        b = self.i2c.readfrom_mem(self.i2c_address, reg, 1)
        return b

    def show_reg(self, reg):
        byt = self.read_reg(reg)
        print("byte read at %x:[%x]" % (reg,int.from_bytes(byt, "big")))

    def set_dac_volume(self, volume):
        # e.g. volume = 70
        self.volume = volume
        reg32 = ((volume) * 256 // 100) - 1
        print("Set volume:", volume)
        self.write_reg(0x32, reg32)
        
    def power_down(self):
        self.write_reg(0x0D, 0x00)
        
    def power_up(self):
        self.write_reg(0x0D, 0x01)
    
    def es8311_reset(self):
        self.write_reg(0x00, 0x1F) # reset
        time.sleep_ms(2)
        self.write_reg(0x00, 0x00) # reset
        self.write_reg(0x00, 0x80) # Power-on command
        
    def es8311_clock_config(self):
        self.write_reg(0x01, 0x3F)  #select clk src for mclk, enable clock for codec 
        self.read_reg(0x06)
        self.write_reg(0x06, 0x03)  # bclk inverter and divider
        time.sleep_ms(2)

    def init_es8311(self):
        print("Initializing ES8311...")
        # Basic sequence to wake up and configure ES8311
        self.es8311_reset()          #updates reg 0x00
        #enable clocks
        self.es8311_clock_config()   #updates reg 0x01 and 0x06
        #
        self.read_reg(0x02)
        self.write_reg(0x02, 0x00) 
        self.write_reg(0x03, 0x10) 
        self.write_reg(0x04, 0x10) 
        self.write_reg(0x05, 0x00)
        self.read_reg(0x06)
        self.write_reg(0x06, 0x03)
        self.write_reg(0x07, 0x00) 
        self.write_reg(0x08, 0xFF)
        #  Master/Slave,resolution,I2S setup    
        self.read_reg(0x00)
        self.write_reg(0x00, 0x80)
        time.sleep_ms(2)
        self.write_reg(0x09, 0x0C)
        self.write_reg(0x0A, 0x0C)
        #
        self.write_reg(0x0D, 0x01) # Power up analog circuitry - NOT default
        self.write_reg(0x0E, 0x02) # Enable analog PGA, enable ADC modulator - NOT default
        self.write_reg(0x12, 0x00) # power-up DAC - NOT default
        self.write_reg(0x13, 0x10) # Enable output to HP drive - NOT default
        self.write_reg(0x1C, 0x6A) # ADC Equalizer bypass, cancel DC offset in digital domain
        self.write_reg(0x37, 0x08) # Bypass DAC equalizer - NOT default
        self.write_reg(0x14, 0x05) # DAC Output Setup
        self.write_reg(0x30, 0x01) # Enable DAC
        self.write_reg(0x31, 0x00)  # DAC Mute, 00=Sets Max Volume 0dB
        # Set Volume (0-100)
        self.set_dac_volume(50)
        self.write_reg(0x17, 0xC8)  # ADC Volume
        self.write_reg(0x14, 0x1A)  # was 1A PGA Gain
        print("ES8311 Initialized.")

