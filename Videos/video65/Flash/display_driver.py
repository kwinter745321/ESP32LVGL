# display_driver.py
# Update 1.1: 08 May 2025 to support the four Orientation modes
# Update 1.2: 17 October to include GC9A01 driver
# Update 1.3: 21 November to merge driver updates with e32r28t model
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-2504.g9fe842956 on 2025-04-04; Raspberry Pi Pico2 with RP2350
# Raspberry Pi Pico (RP2040)
# MicroPython v1.20.0-2504.g9fe842956 on 2025-05-17; Generic ESP32 module with ESP32
# E32R28T ESP32
# LVGL 9.3
#
# 
import lvgl as lv
import ili9xxx
import st77xx
import xpt2046

import machine
from machine import SPI, Pin, reset
import time
#import os
#import sdcard2 as sdcard
#import fs_driver

# Initialize LVGL
lv.init()
print("Running LVGL %d.%d" % (lv.version_major(), lv.version_minor() )  )


#spi = SPI(1, baudrate=27000000, sck=12, mosi=11, miso=Pin(13))
#drv = ili9xxx.Ili9341(spi=spi, dc=7, cs=10, rst=4)

# Initialize display  ILI9341 SPI=20M T=2M
spi = SPI(1, baudrate=20_000_000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
tspi = SPI(2, baudrate=2_000_000, sck=Pin(25), mosi=Pin(32), miso=Pin(39))
#sdspi = SPI(1, baudrate=2_000_000, sck=Pin(10), mosi=Pin(12), miso=Pin(11))

ILI9341_PORTRAIT = 0
ILI9341_LANDSCAPE = 1
ILI9341_INVERTED_PORTRAIT = 2
ILI9341_INVERTED_LANDSCAPE = 3

ST7796_PORTRAIT = 1
ST7796_LANDSCAPE = 0
ST7796_INVERTED_PORTRAIT = 3
ST7796_INVERTED_LANDSCAPE = 2

#### disp object ###################################
disp = ili9xxx.Ili9341(spi=spi, dc=2, cs=15, rst=15, rot=ILI9341_LANDSCAPE)
#disp.set_model("big")  # uncomment for ILI9341 2.8 and 3.2 inch display
disp.set_model("e32")  # uncomment for E32R28T (ESP32-2424S012) 2.8 inch display
#disp = ili9xxx.St7796(spi=spi, dc=0, cs=17, rst=1, rot=ST7796_PORTRAIT)
print("Create 'disp' object for Display:",disp.display_type)
print("Pause 1 sec.")
time.sleep(1)

#### screen object ###################################
hres = disp.width   
vres = disp.height

disp_drv = lv.display_create(hres,vres)
scr = lv.screen_active()

# ILI9341
#touch = xpt2046.Xpt2046_hw(spi=tspi,cs=21,width=(240),height=(320),rot=disp.rot)
if disp.display_type == 'st7796':
    touch = xpt2046.Xpt2046_hw(spi=tspi,cs=33,width=(320),height=(480),rot=disp.rot)
else:
    touch = xpt2046.Xpt2046_hw(spi=tspi,cs=33,width=(240),height=(320),rot=disp.rot)

coords = None
dim = (hres,vres)

def transform9341(p,rot):
    x, y = p
    if   rot==0: coords = x,dim[1]-y-1       
    elif rot==1: coords = x,y      
    elif rot==2: coords = x,dim[1]-y-1 
    else:        coords = dim[0]-x-1,y        
    return coords

def transform9341big(p,rot):
    x, y = p
    if   rot==0: coords = dim[0]-x,dim[1]-y     
    elif rot==1: coords = x,dim[1]-y     
    elif rot==2: coords = dim[0]-x,dim[1]-y 
    else:        coords = x,dim[1]-y        
    return coords

def transform_e32(p,rot):
    x, y = p
    if   rot==0: coords = x,y       
    elif rot==1: coords = dim[0]-x-1,y      
    elif rot==2: coords = x,y 
    else:        coords = dim[0]-x-1,y        
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
        #print("coords:",coords)
        x, y = coords
        if disp.display_type == "st7796":
            coords = transform7796((x,y),disp.rot)
        else:
            if disp.model == "big":
                coords = transform9341big(coords,disp.rot)
            if disp.model == "e32":
                coords = transform_e32(coords,disp.rot)
                #print("e32:",coords)
            elif disp.model == None:
                coords = transform9341((x,y),disp.rot)
                #print("None:",coords)
        data.point.x, data.point.y = coords
        data.state = lv.INDEV_STATE.PRESSED
        return True
    data.state = lv.INDEV_STATE.RELEASED
    return False

# #indev for touch screen
indev_drv = lv.indev_create()
indev_drv.set_type(lv.INDEV_TYPE.POINTER)
indev_drv.set_read_cb(tsread)

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
        #self.rbtn.set_pos(240,200)
        self.rbtn.set_style_bg_color(lv.palette_main(lv.PALETTE.RED),0)
        self.rlbl = lv.label(self.rbtn)
        self.rlbl.set_text("Reset")
        self.rlbl.center()
        self.rbtn.align_to(scr, lv.ALIGN.BOTTOM_RIGHT,-15,-15)
        self.rbtn.add_event_cb(self.reset_cb, lv.EVENT.CLICKED, None)

    def reset_cb(self, event):
        print("Clicked reset")
        self.startmb()
        
    def reset(self):
        reset()
        
    def show(self):
        global coords
        return coords
        
    def quitcb(self, event):
        scr.clean()
        print("quitting...")
        time.sleep(1)
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

