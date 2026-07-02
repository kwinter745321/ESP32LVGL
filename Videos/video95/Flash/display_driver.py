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
#import xpt2046
from cst816 import Touch_CST816S

import machine
from machine import SPI, Pin, reset, SoftSPI, SoftI2C
import time
import os
import sys

#import fs_driver

# Initialize LVGL
lv.init()
#print("Running LVGL %d.%d" % (lv.version_major(), lv.version_minor() )  )

# Initialize display  ILI9341 SPI=20M T=2M
#spi = SoftSPI(baudrate=20_000_000, sck=Pin(10), mosi=Pin(11), miso=Pin(14) )
#spi = SPI(0, baudrate=20_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
#tspi = SPI(0, baudrate=2_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
#spi = SoftSPI(baudrate=40_000_000, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
#tspi = SoftSPI(baudrate=2_000_000, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
spi = SoftSPI(baudrate=40_000_000, sck=Pin(6), mosi=Pin(7), miso=Pin(9))
#tspi = SoftSPI(baudrate=2_000_000, sck=Pin(2), mosi=Pin(3), miso=Pin(4))
#sdspi = SPI(1, baudrate=2_000_000, sck=Pin(10), mosi=Pin(12), miso=Pin(11))

PORTRAIT = const(0)
LANDSCAPE = const(1)
INV_PORTRAIT = const(2)
INV_LANDSCAPE = const(3)

#### disp object ###################################
#backlight = Pin(2,Pin.OUT)
#reset = Pin(12,Pin.OUT)
#reset.on()

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
#disp = st77xx.St7789( spi=spi, dc=8, cs=9, rst=12, bl=13, rot=PORTRAIT, res=(240,320), model='big')
disp = st77xx.St7789( spi=spi, dc=4, cs=5, rst=8, bl=15, rot=PORTRAIT, res=(240,280), model='280')

#disp = ili9xxx.Gc9a01(spi=spi, dc=0, cs=17, rst=1, rot=ILI9341_PORTRAIT)
#disp = ili9xxx.Ili9341(spi=spi, dc=22, cs=5, rst=20, rot=LANDSCAPE)
#disp = ili9xxx.Ili9341(spi=spi, dc=9, cs=13, rst=8, rot=LANDSCAPE)
#disp.set_model("big")  # uncomment for ILI9341 2.8 and 3.2 inch display
#disp = ili9xxx.St7796(spi=spi, dc=0, cs=17, rst=1, rot=ST7796_PORTRAIT)
#print("Create 'disp' object for Display:",disp.display_type)
#print("Pause 1 sec.")
#time.sleep(1)

#### screen object ###################################
hres = disp.width   
vres = disp.height

disp_drv = lv.display_create(hres,vres)
scr = lv.screen_active()


i2c = SoftI2C(scl = Pin(10), sda = Pin(11), freq = 400_000, timeout= 1000)
#print(i2c)
touch = Touch_CST816S(i2c=i2c,int_pin=14,rst_pin=13)     

@micropython.native
def tsread(indev_drv, data) -> int:
    data.state = 0
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
                y = disp.height - y - 1
            if disp.rot == INV_PORTRAIT:
                x = disp.width - x - 1
                y = disp.height - y - 1
            if disp.rot == INV_LANDSCAPE:
                y,x = coords
                x = disp.width - x - 1
            #print(disp.width, disp.height, x,y)
            data.point.x = x
            data.point.y = y
            data.state = 1
    else:
        data.state = 0

#indev for touch screen
indev_drv = lv.indev_create()
indev_drv.set_type(lv.INDEV_TYPE.POINTER)
indev_drv.set_read_cb(tsread)


    # cs = machine.Pin(15, Pin.OUT)
    # mi = machine.Pin(12, Pin.IN)
    # mo = machine.Pin(11, Pin.OUT)
    # sk = machine.Pin(10, Pin.OUT)
    # cs = 1
    # time.sleep(1)
    # spi = SPI(1, baudrate=1_320_000, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
    # time.sleep(1)
    # sd = sdcard.SDCard(spi, machine.Pin(15, Pin.OUT), '/sd')


###############################################
# Reset Thonny
###############################################
    
#### Reset Button #####################
class HardReset():
    
    def __init__(self, scr):
        self.rbtn = None
        self.rlbl = None
        self.quitbtn = None
        self.scr = scr
        self.rbtn = lv.button(scr)
        self.rbtn.set_size(50,25)
        #self.rbtn.set_pos(240,200)
        self.rbtn.align(lv.ALIGN.BOTTOM_RIGHT,-10,-10)
        self.rbtn.set_style_bg_color(lv.palette_main(lv.PALETTE.RED),0)
        self.rlbl = lv.label(self.rbtn)
        self.rlbl.set_text("Reset")
        self.rlbl.center()
        self.rbtn.align_to(scr, lv.ALIGN.TOP_LEFT, 5, 45)
        self.rbtn.add_event_cb(self.reset_cb, lv.EVENT.CLICKED, None)
        lv.screen_load(scr)

    def reset_cb(self, event):
        print("Clicked reset")
        self.startmb()
        
    def reset(self):
        reset()
        
    def show(self):
        global coords
        return coords
        
    def quitcb(self, event):
        print("quitting...")
        reset()

    def startmb(self):
        self.mb = lv.msgbox(self.scr)
        self.mb.add_title("Resets PICO")
        self.mb.add_text("Really reset the program?")
        self.mb.add_close_button()
        self.quitbtn = self.mb.add_footer_button("Reset")
        self.mb.set_style_border_width(5, 0)
        self.mb.set_style_border_color(lv.palette_main(lv.PALETTE.RED),0)
        self.quitbtn.add_event_cb(self.quitcb, lv.EVENT.CLICKED, None)


