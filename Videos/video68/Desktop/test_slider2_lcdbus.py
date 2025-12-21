# test_slider2_lcdbus.py
#
# Created: 17 December 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on:
# LVGL (9.4.0) MicroPython (1.27.0) 
# MicroPython 8dc05cdba3-dirty on 2025-12-17;
# Generic ESP32S3 module with Octal-SPIRAM with ESP32S3
#

from machine import Pin, reset

import lvgl as lv
lv.init()
from display_driver import display

import time

###############################################

from display_driver import display
scr = lv.screen_active()
scr.set_style_bg_color(lv.color_white(),0)
scr.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN )
lv.screen_load(scr)
print("Screen loaded")
###############################################

slider = lv.slider(scr)
slider.set_size(200, 30)
slider.set_style_bg_color(lv.palette_main(lv.PALETTE.GREEN),lv.PART.MAIN)
slider.set_style_bg_color(lv.palette_main(lv.PALETTE.RED),lv.PART.KNOB)
slider.center()
slider.set_value(50, lv.PART.MAIN)

label = lv.label(scr)
label.set_pos(30,10)
label.set_text("HELLO WORLD!")
label.set_style_text_color(lv.color_black(), lv.PART.MAIN)
label.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN )
label.align(lv.ALIGN.CENTER, 0, -50)

btn = lv.button(scr)
btn.set_size(100,40)
btn.set_pos(60,220)
btnlbl = lv.label(btn)
btnlbl.set_style_text_color(lv.color_white(), lv.PART.MAIN)
btnlbl.set_text("Press")
btnlbl.center()

cnt = 0
def btn_cb(event):
    global cnt
    cnt += 1
    val = slider.get_value()
    msg = "Press: {} Slider: {}".format(cnt, val)
    label.set_text(msg)
    
def sld_cb(event):
    global cnt
    val = slider.get_value()
    msg = "Press: {} Slider: {}".format(cnt, val)
    label.set_text(msg)
        
    
btn.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)
slider.add_event_cb(sld_cb, lv.EVENT.VALUE_CHANGED, None)




