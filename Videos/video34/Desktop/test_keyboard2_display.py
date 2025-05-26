# test_keyboard2_display.py
#
# Updated: 19 May 2025 for MP on ESP32
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-2504.g9fe842956 on 2025-05-17; Generic ESP32S3 module with Octal-SPIRAM with ESP32S3
# ESP32-S3 with SPIRAM_OCT (N16R8)
# LVGL 9.3  <-------------------------------Note
# 

#import display_driver
import lvgl as lv

from display_driver import disp, disp_drv, touch

import time

##############################################
# UI
###############################################
 
# current screen
scr = lv.obj()

try:
    from display_driver import HardReset
    h = HardReset(scr)
except ImportError:
    pass

#### Frame the screen #####################
scr.set_style_bg_color(lv.color_hex(0),0)
scr.set_style_border_width(2, 0)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),0)

#### Text Area ############
style = lv.style_t()
style.init()
style.set_bg_color(lv.color_black())
style.set_text_color(lv.palette_main(lv.PALETTE.YELLOW))
style.set_border_color(lv.palette_main(lv.PALETTE.BLUE))

ta = lv.textarea(scr)
ta.add_style(style, lv.PART.MAIN)
ta.set_size(120, 50)
ta.align(lv.ALIGN.BOTTOM_LEFT,10,-10)
ta.set_placeholder_text("enter text")

#### Keyboard ###########
kb = lv.keyboard(scr)
kb.align(lv.ALIGN.TOP_LEFT, 0, 0)
kb.set_textarea(ta)
kb.set_style_bg_color(lv.color_black(), lv.PART.MAIN)
kb.set_style_text_color(lv.color_black(),lv.PART.ITEMS)

ta.align_to(kb, lv.ALIGN.BOTTOM_LEFT,10,70)

btn = lv.button(scr)
btn.set_pos(245,140)
btn.align_to(kb,lv.ALIGN.BOTTOM_RIGHT,-45,45)
lbl = lv.label(btn)
lbl.set_text("Clear")
lbl.set_style_text_color(lv.color_black(), lv.PART.MAIN)

def btn_clear_cb(e):
    global cnt
    ta.set_text("")
    print("Clicked clear button.")


btn.add_event_cb(btn_clear_cb, lv.EVENT.CLICKED, None)
###################################################
lv.screen_load(scr)
        
# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)

                                                                                                                                                                                                                                                       