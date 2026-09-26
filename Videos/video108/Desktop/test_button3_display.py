# test_button3_lcdbus.py
#
# Created: 03 July 2025
# Updated: 25 September 2026
#
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on:
# MicroPython 78ff170de9-dirty on 2026-09-18;
# Generic ESP32S3 module with Octal-SPIRAM with ESP32S3
# LCD_Bus with LVGL 9.4.0
#
import lvgl as lv
import machine
import struct
from display_driver import display
import time
from machine import reset, Pin
scr = lv.screen_active()
lv.screen_load(scr)
width = display._physical_width 
height = display._physical_height
scr.set_style_bg_color(lv.color_hex(0x0),lv.PART.MAIN)

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
#btn.center()
btn.add_style(btnstyle, lv.PART.MAIN)
btn.set_style_bg_color(lv.palette_main(lv.PALETTE.ORANGE),lv.PART.MAIN | lv.STATE.PRESSED)

lbl = lv.label(btn)
lbl.set_text("Press")
lbl.center()
lbl.set_style_text_color(lv.color_black(), lv.PART.MAIN)
lbl.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN)

slider = lv.slider(scr)
slider.set_width(150)
slider.set_pos(40,80)
slider.set_range(0,100)
slider.set_value(20,0)

lbl2 = lv.label(scr)
lbl2.set_text("20")
lbl2.align_to(slider, lv.ALIGN.CENTER, 0, -40)
lbl2.set_style_text_color(lv.color_white(), lv.PART.MAIN)
lbl2.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN)

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

###################################################
lv.screen_load(scr)
