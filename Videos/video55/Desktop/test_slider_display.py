# test_slider_display.py
#
# Created: 08 July 2025
# Verified: 23 September 2025
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.20.0-2504.g9fe842956 on 2025-05-17;
#   Generic ESP32S3 module with Octal-SPIRAM with ESP32S3
# LVGL 9.3

import lvgl as lv
from machine import reset
from display_driver import disp
import time
lv.init()

###############################################
# UI
###############################################

# current screen
scr = lv.obj()
lv.screen_load(scr)

scr.set_style_bg_color(lv.color_hex(0),lv.PART.MAIN)
scr.set_style_border_width(2, lv.PART.MAIN)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),lv.PART.MAIN)

#### Slider ###############################
slider1 = lv.slider(scr)
slider1.center()

#### Label ###############################      
label1 = lv.label(scr)
label1.align(lv.ALIGN.TOP_MID, 0,50)
label1.set_style_text_color(lv.color_white(), lv.PART.MAIN)
label1.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN)
label1.set_text("Progress: 0")

#### Callback ###################################
def slider_cb(event):
    label1.set_text("Progress: {}".format( slider1.get_value() ) )

slider1.add_event_cb(slider_cb, lv.EVENT.VALUE_CHANGED, None)

#### END UI ###############################################

# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)
