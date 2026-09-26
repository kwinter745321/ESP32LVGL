# test_matrix3_lcdbus.py
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
from display_driver import display
import time
from machine import reset
 
scr = lv.screen_active()

width = display._physical_width    # 800
height = display._physical_height  # 480

#### UI ##########################

btnlst = []
lbllst = []

def btn_cb(event):
    obj = event.get_target_obj()
    child = obj.get_child(0)
    txt = child.get_text()
    print(3*"#",txt,3*"#")
    
jcnt = 1
icnt = 0
for j in range(10,(height-20),70):
    for i in range(10,(width-40),70):
        btn = lv.button(scr)
        #btn.set_style_bg_color(lv.palette_main(lv.PALETTE.CYAN),lv.PART.MAIN)
        btn.set_style_bg_color(lv.palette_main(10+jcnt),lv.PART.MAIN)
        btn.set_size(58,50)
        btn.set_pos(i, j)
        lbl = lv.label(btn)
        lbl.center()
        txt = str(i)+"-"+str(jcnt)
        lbl.set_text(txt)
        lbl.set_style_text_color(lv.color_black(),0)
        lbl.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN )
        btn.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)
        btnlst.append(btn)
        lbllst.append(lbl)
        icnt += 1
    jcnt += 1
###################################################

print("UI-end")


