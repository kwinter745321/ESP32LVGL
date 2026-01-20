# test_button_display.py
#
# Created: 08 July 2025
# Update: 14 September 2025
# Update: 21 November 2025
# Update: 17 January 2026 
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# Waveshare ESP32-S3-Touch-LCD-3.5C
# MicroPython v1.20.0-2510.gacfeb7b7e.dirty on 2025-11-23;
# Generic ESP32S3 module with ESP32S3

import lvgl as lv
from machine import reset, Pin
from display_driver import disp, touch
import time
##from lv_utils import task_handler
from machine import SoftI2C


lv.init()

bl = Pin(6, Pin.OUT)
bl.on()

i2c = SoftI2C( scl=Pin(7), sda=Pin(8), freq=40000)

###############################################
# UI
###############################################

# current screen
scr = lv.obj()
lv.screen_load(scr)

scr.set_style_bg_color(lv.color_hex(0),lv.PART.MAIN)
scr.set_style_border_width(2, lv.PART.MAIN)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),lv.PART.MAIN)

### Style  ###################
btnstyle = lv.style_t()
btnstyle.init()
btnstyle.set_radius(5)
btnstyle.set_bg_opa(lv.OPA.COVER)
btnstyle.set_bg_color(lv.palette_main(lv.PALETTE.BLUE))
btnstyle.set_outline_width(2)
btnstyle.set_outline_color(lv.palette_main(lv.PALETTE.BLUE))
btnstyle.set_outline_pad(8)
 
#### Button ##################
btn = lv.button(scr)
btn.set_size(100,50)
btn.center()
btn.add_style(btnstyle, lv.PART.MAIN)

lbl = lv.label(btn)
lbl.set_text("One")
lbl.center()
lbl.set_style_text_color(lv.color_black(), lv.PART.MAIN)
lbl.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN)

cnt = 1

def btn_cb(event):
    global cnt, xyz
    print("Clicked button:",cnt)
    cnt = cnt + 1


btn.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)
###################################################
#lv.screen_load(scr)

# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)
