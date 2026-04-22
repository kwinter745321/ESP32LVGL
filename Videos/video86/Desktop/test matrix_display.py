# test_matrix_display.py
#
# Created: 28 April 2025 for 320x480 displays
# Update:  17 January 2026 
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# ILI9488
# MicroPython v1.20.0-2510.gacfeb7b7e on 2026-01-16;
# Raspberry Pi Pico with RP2040
# LVGL 9.3
# 
import lvgl as lv
from machine import reset, Pin, SPI
import time
#import gc
from display_driver import disp

start_time = time.ticks_ms()

scr = lv.obj()

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
    
jcnt = 1
icnt = 0
for j in range(10,disp.height-20,50):
    for i in range(10,disp.width-20,50):
        #gc.collect()
        btn = lv.button(scr)
        #btn.set_style_bg_color(lv.palette_main(lv.PALETTE.CYAN),lv.PART.MAIN)
        btn.set_style_bg_color(lv.palette_main(6+jcnt),lv.PART.MAIN)
        btn.set_size(48,40)
        btn.set_pos(i, j)
        lbl = lv.label(btn)
        lbl.center()
        txt = str(i)+"-"+str(jcnt)
        lbl.set_text(txt)
        lbl.set_style_text_color(lv.color_black(),0)
        #lbl.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN )
        btn.add_event_cb(btn_cb, lv.EVENT.PRESSED, None)
        btnlst.append(btn)
        lbllst.append(lbl)
        icnt += 1
    jcnt += 1
    #print(gc.mem_free())   
###################################################
lv.screen_load(scr)
elapsed = time.ticks_diff(time.ticks_ms(), start_time)
print(f"Event took {elapsed} ms")