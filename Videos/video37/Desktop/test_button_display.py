# test_button_display.py
#
# Updated: 30 May 2025
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-2504.g9fe842956 on 2025-05-17; Generic ESP32 module with ESP32
# ESP32-GENERIC
# LVGL 9.3 
#
# Tested with ESP32-WROOM-32 USB board
# Tested with ESP32-2432S028 (CYD) USB Board


import lvgl as lv
from display_driver import disp, disp_drv, touch
from machine import Pin,reset

import time
lv.init()

###############################################
# UI
###############################################
 
# current screen
scr = lv.obj()
#h = HardReset(scr)

scr.set_style_bg_color(lv.color_hex(0),0)
scr.set_style_border_width(2, 0)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),0)

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
btn.add_style(btnstyle, 0)

lbl = lv.label(btn)
lbl.set_text("One")
lbl.center()
lbl.set_style_text_color(lv.color_hex(0),0)
lbl.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN | lv.STATE.DEFAULT)

cnt = 1

def btn_cb(event):
    global cnt
    print("Clicked button:",cnt)
    cnt = cnt + 1

btn.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)

###################################################
lv.screen_load(scr)
        

# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)