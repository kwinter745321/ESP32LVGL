# display_driver.py
# Updated:    19 January 2026 to support CTP_ft6x36 driver via tca9554
# Note:  Anything not related to ST7796 was removed
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# Waveshare ESP32-S3-Touch-LCD-3.5C
# MicroPython v1.20.0-2510.gacfeb7b7e.dirty on 2025-11-23;
# Generic ESP32S3 module with ESP32S3
# 
import lvgl as lv
import ili9xxx
#import xpt2046
from ctp_ft6x36 import ft6x36
import pca9554

import machine
from machine import reset, SPI, Pin
import time


# Initialize LVGL
lv.init()
print("Running LVGL %d.%d" % (lv.version_major(), lv.version_minor() )  )

# Initialize SPI
spi = SPI(2, baudrate=60_000_000, sck=Pin(5), mosi=Pin(1), miso=Pin(2))

time.sleep(1)
pca = pca9554.Pca9554(0x20)
# Display RST
pca.write_config_port(1, pca9554.OUTPUT)

# Screen Orientation Values
PORTRAIT = 0
LANDSCAPE = 1
INVERTED_PORTRAIT = 2
INVERTED_LANDSCAPE = 3

#### disp object ###################################
disp = ili9xxx.St7796(spi=spi, dc=3, cs=6, rst=6, rot=1)
print("Create 'disp' object for Display:",disp.display_type)
print("Pause 1 sec.")
time.sleep(1)

#### screen object ###################################
hres = disp.width   
vres = disp.height
# normally this returns 320,480 for ST7796
print("Creating display using hres,vres",hres,vres)
# invert colors
disp.write_register(0x21,None)

disp_drv = lv.display_create(hres,vres)
scr = lv.screen_active()

if   disp.rot==0: touch=ft6x36(0,sda=8,scl=7,reset=6,irq=5,width=320,height=480,inv_x=False,inv_y=False,swap_xy=False)           
elif disp.rot==1: touch=ft6x36(0,sda=8,scl=7,reset=6,irq=5,width=480,height=320,inv_x=True,inv_y=False,swap_xy=True)  
elif disp.rot==2: touch=ft6x36(0,sda=8,scl=7,reset=6,irq=5,width=320,height=480,inv_x=True,inv_y=True,swap_xy=False )         
else: touch=ft6x36(0,sda=8,scl=7,reset=6,irq=5,width=480,height=320,inv_x=False,inv_y=True,swap_xy=True)   

