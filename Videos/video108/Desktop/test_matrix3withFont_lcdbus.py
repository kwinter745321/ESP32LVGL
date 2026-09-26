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
montserrat_med_20 = None
ready = False
try:
    import os
    # Must use os path here
    font_path = "font/montserrat-med-20-2.bin"
    try:
        os.stat(font_path)
        ready = True
    except:
        ready = False
        print(f"Warning external font not found by os. ready:{ready}")
    if ready == True:
        import fs_driver
        fs_drv = lv.fs_drv_t()
        fs_driver.fs_register(fs_drv, 'S')
        # now include LVGL drive letter
        montserrat_med_20 = lv.binfont_create("S:" + font_path )
except:
    print("Possible Heap corruption. Remove external font.")
    if montserrat_med_20 is not None:
        lv.binfont_destroy(montserrat_med_20)
        montserrat_med_20 = None
    if hasattr(fs_drv, 'ready_cb'):
        fs_drv.user_data = None
if ready:
    print("found and loaded external font.")
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
        if montserrat_med_20 is not None:
            btn.set_size(63,50)
            lbl.set_style_text_font(montserrat_med_20, lv.PART.MAIN )
        else:
            lbl.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN )
        btn.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)
        btnlst.append(btn)
        lbllst.append(lbl)
        icnt += 1
    jcnt += 1
###################################################

print("UI-end")


