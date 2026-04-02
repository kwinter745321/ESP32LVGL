# display_driver.py
# Updated:    08 May 2025 to support the four Orientation modes
# Updated:    17 October 2025 include GC9A01 driver
# Updated:    02 November 2025 include ST7735 display from ST77xx driver
# Modified:   29 March 2026 to support the CST816 touchscreen driver
# Updated by: KWServices
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.27.0-dirty on 2026-03-02;
# Raspberry Pi Pico 2 W with RP2350
# LVGL 9.5
#
# 
import lvgl as lv
import ili9xxx
import st77xx
#import xpt2046
import machine
from machine import SPI, Pin, reset, SoftSPI, SoftI2C, I2C
#from cst328 import CST328
from cst816 import Touch_CST816S

import time
import sys

#import fs_driver

# Initialize LVGL
lv.init()
print("Running LVGL %d.%d" % (lv.version_major(), lv.version_minor() )  )

LCD_SCLK = 4
LCD_MOSI = 6
LCD_MISO = 5


# Initialize display  ILI9341 SPI=20M T=2M
spi = SoftSPI(baudrate=20_000_000, sck=Pin(4), mosi=Pin(6), miso=Pin(5) )
print(spi)
#spi = SPI(0, baudrate=20_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
#tspi = SPI(0, baudrate=2_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
#sdspi = SPI(1, baudrate=2_000_000, sck=Pin(10), mosi=Pin(12), miso=Pin(11))
i2c = SoftI2C(scl = Pin(9), sda = Pin(8), freq = 100_000, timeout= 1000)
print(i2c)
touch = Touch_CST816S(i2c=i2c,int_pin=1,rst_pin=0)
print(touch)

PORTRAIT = const(0)
LANDSCAPE = const(1)
INV_PORTRAIT = const(2)
INV_LANDSCAPE = const(3)

#### disp object ###################################
#backlight = Pin(15,Pin.OUT)
#backlight.on()

LCD_CS = 7
LCD_DC = 3
LCD_RST = 2
LCD_BL = 10

time.sleep_ms(255)
# Waveshare 1.44 128x128
#disp = st77xx.St7735( spi=spi, dc=8, cs=9, rst=12, bl=13, rot=0, res=(128,128), model="1.44",bgr=False )
# Waveshare 1.8
#disp = st77xx.St7735( spi=spi, dc=8, cs=9, rst=12, bl=13, rot=0, res=(128,160), model="greentab", bgr=False)
# HiLetgo 1.8 (Must use HW SPI)
#disp = st77xx.St7735( spi=spi, dc=0, cs=17, rst=1, bl=2, rot=0, res=(128,160), model="redtab", bgr=False)
# WeAct 1.8
#disp = st77xx.St7735( spi=spi, dc=8, cs=9, rst=12, bl=13, rot=1, res=(128,160), model="greentab", bgr=False)
# Xiia 2.4
#disp = ili9xxx.Ili9341(spi=spi, dc=8, cs=9, rst=0, rot=ILI9341_LANDSCAPE)
# 1.3
#disp = st77xx.St7789( spi=spi, dc=8, cs=9, rst=12, bl=13, rot=ST77XX_PORTRAIT, res=(240,320), model=None)
#disp = st77xx.St7789( spi=spi, dc=14, cs=13, rst=15, bl=16, rot=1, res=(240,320), model='big')

disp = ili9xxx.Gc9a01(spi=spi, dc=3, cs=7, rst=2, rot=3)
#disp = ili9xxx.Ili9341(spi=spi, dc=0, cs=17, rst=1, rot=ILI9341_LANDSCAPE)
#disp.set_model("big")  # uncomment for ILI9341 2.8 and 3.2 inch display
#disp = ili9xxx.St7796(spi=spi, dc=0, cs=17, rst=1, rot=ST7796_PORTRAIT)
#print("Create 'disp' object for Display:",disp.display_type)
#print("Pause 1 sec.")
#time.sleep(1)

#### screen object ###################################
hres = disp.width   
vres = disp.height
print("res:",hres,vres)

disp_drv = lv.display_create(hres,vres)
scr = lv.screen_active()


#### touchscreen object ###################################
I2C_SDA = 6
I2C_SCL = 7
I2C_INT = 17
I2C_RST = 16
#i2c = SoftI2C(scl = Pin(5), sda = Pin(4), freq = 100_000, timeout= 1000)
#i2c = SoftI2C(scl = Pin(7), sda = Pin(6), freq = 100_000, timeout= 50)
#print(i2c)
#touch = CST328(i2c, disp.width, disp.height, rotation=disp.rot)
#touch = None
#time.sleep(1)
#touch = Touch_CST816S(i2c=i2c,int_pin=17,rst_pin=16)
# try:
#     touch = Touch_CST816S(mode=1,i2c=i2c,int_pin=I2C_INT,rst_pin=I2C_RST)
# except:
#     print("touch device error")
#time.sleep(1)    

@micropython.native
def tsread(indev_drv, data) -> int:
    if touch == None:
        return
    if touch.state == True:
        touch.state = False
        touch.get_point()
        coords =  (touch.X_point,touch.Y_point)
        #print("touched: ",coords)
        if coords != None:
            x,y = coords
            if disp.rot == LANDSCAPE:
                y,x = coords
                y = disp.width - y - 1
            if disp.rot == INV_PORTRAIT:
                x = disp.width - x - 1
                y = disp.height - y - 1
            if disp.rot == INV_LANDSCAPE:
                y,x = coords
                x = disp.width - x - 1
            data.point.x = x
            data.point.y = y
            data.state = 1
    else:
        data.state = 0

#indev for touch screen
indev_drv = lv.indev_create()
indev_drv.set_type(lv.INDEV_TYPE.POINTER)
indev_drv.set_read_cb(tsread)

