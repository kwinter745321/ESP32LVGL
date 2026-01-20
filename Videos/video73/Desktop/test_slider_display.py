# test_slider_display.py
#
# Created: 08 July 2025
# Updated: 23 September 2025
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
from display_driver import disp
import time
lv.init()

bl = Pin(6, Pin.OUT)
bl.on()
###############################################
# UI
###############################################

# current screen
scr = lv.obj()
lv.screen_load(scr)

#### White background yellow border #######
#scr.set_style_bg_color(lv.color_hex(0),lv.PART.MAIN)
scr.set_style_border_width(2, lv.PART.MAIN)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.YELLOW),lv.PART.MAIN)

#### Slider ###############################
slider1 = lv.slider(scr)
slider1.center()
slider1.set_value(50, 0)

def slider_cb(event):
    label1.set_text("Value: {}".format( slider1.get_value() ) )

slider1.add_event_cb(slider_cb, lv.EVENT.VALUE_CHANGED, None)

#### Label - Value ###############################      
label1 = lv.label(scr)
label1.align(lv.ALIGN.BOTTOM_MID, 0,-40)
label1.set_style_text_color(lv.color_black(), lv.PART.MAIN)
label1.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN)
label1.set_text("Value: 50")

#### Button - Right ############################### 
right = lv.button(scr)
right.set_size(48,48)
right.set_pos(disp.width-75,disp.height-65)
rightlbl = lv.label(right)
rightlbl.center()
rightlbl.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN)
rightlbl.set_style_text_color(lv.color_black(), lv.PART.MAIN)
rightlbl.set_text(">")

#### Button - Left ############################### 
left = lv.button(scr)
left.set_size(48,48)
left.set_pos(25,disp.height-65)
leftlbl = lv.label(left)
leftlbl.center()
leftlbl.set_style_text_color(lv.color_black(), lv.PART.MAIN)
leftlbl.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN)
leftlbl.set_text("<")

def rightcb(e):
    val = slider1.get_value()
    val = (val//5)*5 + 5
    if val>100:
        val = 100
    slider1.set_value(val, 0)
    label1.set_text("Value: {}".format( slider1.get_value() ) )
    
def leftcb(e):
    val = slider1.get_value()
    val = (val//5)*5 - 5
    if val<=0:
        val = 0
    slider1.set_value(val, 0)
    label1.set_text("Value: {}".format( slider1.get_value() ) )
    
right.add_event_cb(rightcb, lv.EVENT.CLICKED, None)
left.add_event_cb(leftcb, lv.EVENT.CLICKED, None)
#### END UI ###############################################

# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)
