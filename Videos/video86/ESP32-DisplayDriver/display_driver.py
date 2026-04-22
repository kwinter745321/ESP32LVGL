# display_driver.py
# Updated:    08 May 2025 to support the four Orientation modes
# Updated:    17 October 2025 include GC9A01 driver
# Updated:    02 November 2025 include ST7735 display from ST77xx driver
# Updated by: KWServices
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-2504.g9fe842956 on 2025-04-04; Raspberry Pi Pico2 with RP2350
# Raspberry Pi Pico (RP2040)
# LVGL 9.3
#
# 
import lvgl as lv
import ili9xxx
import st77xx
import xpt2046
import machine
from machine import SPI, Pin, reset, SoftSPI, SoftI2C, I2C
#from cst328 import CST328
import gc

import time
import sys

#import fs_driver

# Initialize LVGL
lv.init()
print(sys.implementation)
print("Running LVGL %d.%d" % (lv.version_major(), lv.version_minor() )  )

LCD_SCLK = 10
LCD_MOSI = 11
LCD_MISO = 12


# Initialize SPI
spi = SPI(1, baudrate=40_000_000, sck=Pin(12), mosi=Pin(11), miso=Pin(13) )
#tspi = SPI(0, baudrate=1_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
tspi = SPI(1, baudrate=2_000_000, sck=Pin(12), mosi=Pin(11), miso=Pin(13))
#sdspi = SPI(1, baudrate=2_000_000, sck=Pin(10), mosi=Pin(12), miso=Pin(11))

PORTRAIT = const(0)
LANDSCAPE = const(1)
INV_PORTRAIT = const(2)
INV_LANDSCAPE = const(3)

#### disp object ###################################
# backlight = Pin(16,Pin.OUT)
# backlight.on()

LCD_CS = 13
LCD_DC = 14
LCD_RST = 15
LCD_BL = 16

time.sleep_ms(255)
# Waveshare 1.44 128x128
#disp = st77xx.St7735( spi=spi, dc=8, cs=9, rst=12, bl=13, rot=0, res=(128,128), model="1.44",bgr=False )
# Waveshare 1.8
#disp = st77xx.St7735( spi=spi, dc=8, cs=9, rst=12, bl=13, rot=0, res=(128,160), model="greentab", bgr=False)
# HiLetgo 1.8 (Must use HW SPI)
#disp = st77xx.St7735( spi=spi, dc=0, cs=17, rst=1, bl=2, rot=0, res=(128,160), model="redtab", bgr=False)
# WeAct 1.8
#disp = st77xx.St7735( spi=spi, dc=8, cs=9, rst=12, bl=13, rot=0, res=(128,160), model="greentab", bgr=False)
# Xiia 2.4
#disp = ili9xxx.Ili9341(spi=spi, dc=8, cs=9, rst=12, rot=ILI9341_LANDSCAPE)
# 1.3
#disp = st77xx.St7789( spi=spi, dc=8, cs=9, rst=12, bl=13, rot=ST77XX_PORTRAIT, res=(240,320), model=None)
#disp = st77xx.St7789( spi=spi, dc=14, cs=13, rst=15, bl=16, rot=1, res=(240,320), model='big')

#disp = ili9xxx.Gc9a01(spi=spi, dc=0, cs=17, rst=1, rot=ILI9341_PORTRAIT)
#disp = ili9xxx.Ili9341(spi=spi, dc=9, cs=13, rst=8, rot=LANDSCAPE)
#disp.set_model("big")  # uncomment for ILI9341 2.8 and 3.2 inch display

# 4.0 inch ILI9488 (16 bit interface)
#disp = ili9xxx.Ili9488(spi=spi, dc=4, cs=10, rst=7, rot=PORTRAIT)
# 3.5 inch ILI9488 Capacitive touch
#disp.write_register(0x21, b"\x00")
# ILI9488 (18 bit interface)
disp = ili9xxx.Ili9488b(spi=spi, dc=4, cs=10, rst=7, rot=PORTRAIT)
# 3.5 inch ILI9488 Capacitive touch
#disp.write_register(0x21, b"\x00")

#disp = ili9xxx.St7796(spi=spi, dc=9, cs=13, rst=8, rot=1)
#print("Create 'disp' object for Display:",disp.display_type)
#print("Pause 1 sec.")
#time.sleep(1)

#### screen object ###################################
hres = disp.width   
vres = disp.height

#hres = 320
#vres = 480
print("Display hres:{} vres:{} ".format(hres,vres) )

disp_drv = lv.display_create(hres,vres)
####disp_drv.set_color_format(lv.COLOR_FORMAT.RGB888)

scr = lv.screen_active()
# for capacitive display
print("Memory free:",gc.mem_free())
gc.collect()
print("Memory free:",gc.mem_free())
#### touchscreen object ###################################
touch = None
if disp.display_type in ['ili9488', 'st7796']:
    touch = xpt2046.Xpt2046_hw(spi=tspi,cs=14,width=(320),height=(480),rot=disp.rot)
elif disp.display_type in ['ili9341', 'st7789']:
    touch = xpt2046.Xpt2046_hw(spi=tspi,cs=14,width=(240),height=(320),rot=disp.rot)
else:
    print("May not be a XPT2046 touchscreen. Use different driver.")
    #touch = xpt2046.Xpt2046_hw(spi=tspi,cs=14,width=(240),height=(240),rot=disp.rot)
touch = xpt2046.Xpt2046_hw(spi=tspi,cs=14,width=(320),height=(480),rot=disp.rot)
print(tspi)

coords = None
dim = (hres,vres)

print("Display type:",disp.display_type," Rotation: ",disp.rot)
if disp.display_type == "ili9488b":
    print("Display model:",disp.model)

def transform9488(coords,rot):
    if coords != None:
            x,y = coords
            if disp.rot == PORTRAIT:
                x = disp.width - x - 1
                y = disp.height - y - 1
            if disp.rot == LANDSCAPE:
                y = disp.height - y - 1
            if disp.rot == INV_PORTRAIT:
                x = disp.width - x - 1
                y = disp.height - y - 1
            if disp.rot == INV_LANDSCAPE:
                y = disp.height - y - 1
    return x,y


def transform9341(p,rot):
    x, y = p
    if   rot==0: coords = x,dim[1]-y-1       
    elif rot==1: coords = x,y      
    elif rot==2: coords = x,dim[1]-y-1 
    else:        coords = x,y        
    return coords

def transform9341big(p,rot):
    x, y = p
    if   rot==0: coords = dim[0]-x,dim[1]-y     
    elif rot==1: coords = x,dim[1]-y     
    elif rot==2: coords = dim[0]-x,dim[1]-y 
    else:        coords = x,dim[1]-y
    #print(x,y,coords)
    return coords

def transform7796(p,rot):
    x, y = p
    if   rot==0: coords = dim[0]-y,x            
    elif rot==1: coords = y,x
    elif rot==2: coords = dim[0]-y,x         
    else:        coords = y,x       
    return coords

@micropython.native
def tsread(indev_drv, data) -> int:
    global coords
    coords = touch.pos()
    if coords:
        
        x, y = coords
#         if disp.display_type == "st7796":
#             coords = transform7796((x,y),disp.rot)
#         else:
#             if disp.model == "big":
#                 coords = transform9341big(coords,disp.rot)
#             else:
#                 coords = transform9341((x,y),disp.rot)
        coords = transform9488(coords, disp.rot)
        data.point.x, data.point.y = coords
        data.state = lv.INDEV_STATE.PRESSED
        #print(data.point.x, data.point.y)
        return True
    data.state = lv.INDEV_STATE.RELEASED
    return False

if touch != None:
    # #indev for touch screen
    indev_drv = lv.indev_create()
    indev_drv.set_type(lv.INDEV_TYPE.POINTER)
    indev_drv.set_read_cb(tsread)
