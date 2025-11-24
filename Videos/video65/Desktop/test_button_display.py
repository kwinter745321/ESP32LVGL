# test_button_display.py
#
# Created: 08 July 2025
# Update: 14 September 2025
# Update: 21 November 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.20.0-2504.g9fe842956 on 2025-05-17; Generic ESP32 module with ESP32

import lvgl as lv
from machine import reset, Pin
from display_driver import disp
import time
lv.init()

bl = Pin(21, Pin.OUT)
bl.on()
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
lbl.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN)

cnt = 1

def btn_cb(event):
    global cnt
    print("Clicked button:",cnt)
    cnt = cnt + 1

btn.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)
###################################################
#lv.screen_load(scr)

# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)
