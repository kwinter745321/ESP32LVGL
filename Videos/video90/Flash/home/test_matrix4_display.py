# test_matrix4_display.py
#
# Created: 14 May 2026
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.28.0-dirty on 2026-05-08; 
# Generic ESP32S3 module with Octal-SPIRAM with ESP32S3 
# OTA
# LVGL 9.5
#
import sys
sys.path.append("/home/lib")
import proc
proc=None

import lvgl as lv
from machine import reset, Pin, SPI
import time
#import gc
from display_driver import disp

start_time = time.ticks_ms()

bl = Pin(17 , Pin.OUT)
bl.on()


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

def __main__(args):     # Entry point and command line arguments
    try: 
        while True:          # Main loop (for, while, etc)
            if proc.sts=="H":       # Mechanism to hold and resume the process if it is launched in batch (&) and held
                time.sleep(1)
                continue
            if proc.sts=="S":
                print("Program Stopped.")
                break
            lv.timer_handler()
            time.sleep_ms(10)
    except:
        print("Exception")
    finally:
        scr.clean()
        bl.off()
        print("Program end.")

