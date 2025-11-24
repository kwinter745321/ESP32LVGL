# test_matrix4_display.py
#
# Created: 28 April 2025
# update v2:  24 June 2025 for 320*480 display
# Update v3: 14 September 2025
# Update v4: 21 November 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.20.0-2504.g9fe842956 on 2025-05-17; Generic ESP32 module with ESP32

import lvgl as lv
from machine import Pin, SPI, reset
import time

from display_driver import disp

bl = Pin(21, Pin.OUT)
bl.on()

scr = lv.obj()
lv.screen_load(scr)
width = disp.width
height = disp.height

#### UI ##########################

scr.set_style_bg_color(lv.color_hex(0),0)
scr.set_style_border_width(2, 0)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),0)

### Button  ###################
btnlst = []
lbllst = []

def btn_cb(event):
    obj = event.get_target_obj()
    child = obj.get_child(0)
    txt = child.get_text()
    print(3*"#",txt,3*"#")
    
size = 50
if size < 30:
    size = 30
    
jcnt = 1
icnt = 0
for j in range(10,(height-20),size):
    for i in range(10,(width-20),size):
        btn = lv.button(scr)
        #btn.set_style_bg_color(lv.palette_main(lv.PALETTE.CYAN),lv.PART.MAIN)
        btn.set_style_bg_color(lv.palette_main(6+jcnt),lv.PART.MAIN)
        btn.set_size(size-2,size-10)
        btn.set_pos(i, j)
        lbl = lv.label(btn)
        lbl.center()
        txt = str(i)+"-"+str(jcnt)
        if size < 50:
            txt = str(jcnt)
        lbl.set_text(txt)
        lbl.set_style_text_color(lv.color_black(),0)
        #lbl.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN )
        btn.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)
        btnlst.append(btn)
        lbllst.append(lbl)
        icnt += 1
    jcnt += 1
###################################################
