# sdcard_driver.py
#
# Updated:  03 July 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
# LVGL (9.2.2) MicroPython (1.24.1) Binding compiled on 2025-06-13; Generic ESP32S3 module with Octal-SPIRAM with ESP32S3
# Waveshare ESP32-S3-Touch-LCD-4.3
# LVGL 9.2.2
#
import os
import ch422g
import machine

from i2c import I2C


i2c_bus = I2C.Bus(
        host=0,
        scl=9,
        sda=8,
        freq=400000,
        use_locks=False
        )

io_expander_device = I2C.Device(i2c_bus, dev_id=ch422g.I2C_ADDR, reg_bits=ch422g.BITS)
ch422g.Pin.set_device(io_expander_device)

tp_reset_pin =  ch422g.Pin(
    ch422g.EXIO1,  # sets the pin to use on the IO expander
    mode=ch422g.Pin.OUT,  # sets the mode as output
    # 0 if the pin needs to be high to to reset 
    # 1 if the state needs to be low to perform a reset 
    value=0)

tp_lcdbl_pin =  ch422g.Pin(
    ch422g.EXIO2,  # sets the pin to use on the IO expander
    mode=ch422g.Pin.OUT,  # sets the mode as output
    # 0 if the pin needs to be high to to reset 
    # 1 if the state needs to be low to perform a reset 
    value=0)

'''
tp_lcdrst_pin =  ch422g.Pin(
    ch422g.EXIO3,  # sets the pin to use on the IO expander
    mode=ch422g.Pin.OUT,  # sets the mode as output
    # 0 if the pin needs to be high to to reset 
    # 1 if the state needs to be low to perform a reset 
    value=0)
'''
tp_sd_cs_pin =  ch422g.Pin(
    ch422g.EXIO4,  # sets the pin to use on the IO expander
    mode=ch422g.Pin.OUT,  # sets the mode as output
    value=0)

# rest muss low sein, sonst geht I2C nicht
tp_reset_pin.low()
# lcdbl muss low sein, sonst ist display dunkel
tp_lcdbl_pin.low()
# cs muss high sein, sost geht SD nicht
tp_sd_cs_pin.high()

spi_bus = machine.SPI.Bus(
    host=2,  # SPI2 (HSPI)
    mosi=11,   #14,  # SD_CMD (DI) → IO14
    miso=13,    #9,  # SD_DAT0 (DO) → IO9
    sck=12,    #11,  # SD_CLK → IO11
)

sd = None
try:
    sd = machine.SDCard(
        spi_bus=spi_bus,
        cs=2,   # since set above just using the backlight pin here
        freq=20000000
    )

    #vfs.mount(sd, "/sd")
    #os.chdir('/sd')
    #print(os.listdir("/"))
    #print("Mounted /sd")
except Exception as e:
    print("SDCard error:",e)
