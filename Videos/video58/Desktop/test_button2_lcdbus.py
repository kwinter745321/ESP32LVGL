# test_button2_lcdbus.py
#
# Revised: 03 July 2025
# updated: 08 October 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
# LVGL (9.3.0) MicroPython (1.25.0) Binding compiled on 2025-10-08;
# Generic ESP32S3 module with Octal-SPIRAM with ESP32S3
# Waveshare ESP32-S3-Touch-LCD-4.3
#
import lvgl as lv
from display_driver import display
import task_handler
import i2c
import gt911
from machine import reset
import time

from sdcard_driver import sd
import os
import fs_driver


#### sd card setup ########################
try:
    vfs.mount(sd, "/sd")
    os.chdir('/sd')
    #print(os.listdir("/"))
    print("Mounted /sd")
except Exception as e:
    print("SDCard error:",e)
    
fs_drv = lv.fs_drv_t()
fs_driver.fs_register(fs_drv, 'S')


#### UI ##########################################################
print("UI")
scr = lv.screen_active()

scr.set_style_bg_color(lv.color_hex(0),0)
scr.set_style_border_width(2, 0)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),0)

montserrat_med_18 = lv.binfont_create("S:font/montserrat-med-18-2.bin" )
montserrat_med_28 = lv.binfont_create("S:font/montserrat-med-28-2.bin" )
alexbrush_reg_36 = lv.binfont_create("S:font/alexbrush-reg-36-2.bin" )

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
#lbl.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN | lv.STATE.DEFAULT)
lbl.set_style_text_font(montserrat_med_18, lv.PART.MAIN | lv.STATE.DEFAULT)
#lbl.set_style_text_font(montserrat_med_28, lv.PART.MAIN | lv.STATE.DEFAULT)
#lbl.set_style_text_font(alexbrush_reg_36, lv.PART.MAIN | lv.STATE.DEFAULT)

cnt = 1

def btn_cb(event):
    global cnt
    print("Clicked button:",cnt)
    cnt = cnt + 1

btn.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)

print("UI-end")
#### UI END ##########################################################

# while True:
#     lv.refr_now(lv.display_get_default())
# 
#     time.sleep_ms(10)
#     lv.tick_inc(10)
#     lv.task_handler()
