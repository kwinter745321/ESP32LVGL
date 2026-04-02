# test_button3_display.py
#
# Created: 08 July 2025
# Update: 01 April 2026
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# Waveshare 1.28inch Round Touch LCD
# MicroPython v1.20.0-2510.gacfeb7b7e.dirty on 2026-04-01;
# ESP32C3 module with ESP32C3

import lvgl as lv
from machine import reset, Pin
from display_driver import disp, touch
import time

lv.init()

bl = Pin(10, Pin.OUT)
bl.on()

###############################################
# UI
###############################################

# current screen
scr = lv.obj()

scr.set_style_bg_color(lv.color_hex(0xffffff),lv.PART.MAIN)
# scr.set_style_border_width(2, lv.PART.MAIN)
# scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),lv.PART.MAIN)

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
btn.set_pos(70,150)
btn.add_style(btnstyle, lv.PART.MAIN)
btn.set_style_bg_color(lv.palette_main(lv.PALETTE.ORANGE),lv.PART.MAIN | lv.STATE.PRESSED)

lbl = lv.label(btn)
lbl.set_text("Press")
lbl.center()
lbl.set_style_text_color(lv.color_black(), lv.PART.MAIN)
lbl.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN)

slider = lv.slider(scr)
slider.set_width(150)
slider.set_pos(40,80)
slider.set_range(0,100)
slider.set_value(20,0)

lbl2 = lv.label(scr)
lbl2.set_text("20")
lbl2.align_to(slider, lv.ALIGN.CENTER, 0, -40)
lbl2.set_style_text_color(lv.color_black(), lv.PART.MAIN)
lbl2.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN)

cnt = 1

def btn_cb(event):
    global cnt, xyz
    print("Clicked button:",cnt)
    lbl.set_text("{:d}".format(cnt))
    cnt = cnt + 1
    
def slider_cb(event):
    slid = event.get_target_obj()
    lbl2.set_text("{:d}".format(slid.get_value()))

btn.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)
slider.add_event_cb(slider_cb, lv.EVENT.VALUE_CHANGED, None)

def swipe(event):
    indev = lv.indev_active()
    ges_dir = indev.get_gesture_dir()
    if ges_dir:
        if ges_dir == lv.DIR.TOP:
            print("home")
        if ges_dir == lv.DIR.LEFT:
            print("left")
        if ges_dir == lv.DIR.RIGHT:
            print("right")
        if ges_dir == lv.DIR.BOTTOM:
            print("down")  

scr.add_event_cb(swipe, lv.EVENT.GESTURE, None)

###################################################
lv.screen_load(scr)

# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)
