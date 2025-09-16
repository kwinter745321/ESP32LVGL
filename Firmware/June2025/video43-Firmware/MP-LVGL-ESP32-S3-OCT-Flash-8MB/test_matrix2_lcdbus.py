# test_matrix2_lcdbus.py
#
# Updated:  03 July 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
# LVGL (9.2.2) MicroPython (1.24.1) Binding compiled on 2025-06-13; Generic ESP32S3 module with Octal-SPIRAM with ESP32S3
# Waveshare ESP32-S3-Touch-LCD-4.3
# LVGL 9.2.2
#
import lvgl as lv
from display_driver import display
import time
from machine import reset
 
scr = lv.screen_active()

width = display._physical_width
height = display._physical_height
# width = 800  
# height = 480 
#### UI ##########################


### Button  ###################
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


# while True:
#     lv.refr_now(lv.display_get_default())
# 
#     time.sleep_ms(10)
#     lv.tick_inc(10)
#     lv.task_handler()
