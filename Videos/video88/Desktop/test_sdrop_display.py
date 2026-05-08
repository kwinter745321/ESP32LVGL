# test_sdrop_display.py
#
# Created: 06 May 2026
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.28.0-dirty on 2026-05-07;
# Generic ESP32S3 module with Octal-SPIRAM with ESP32S3
# ESP-IDF 5.5.1
# N16R8
# Flashsize: 16 MB PSRAM: 8MB
# LVGL 9.5.0

import lvgl as lv
from machine import reset, Pin
from display_driver import disp, touch
import time
import fs_driver

lv.init()

# Display Backlight pin
bl = Pin(17, Pin.OUT)
bl.on()

#### globals
titlewidth = 240
squaresize = 60
squarecount = 3
arcsize = 100

###############################################
# UI
###############################################
fs_drv = lv.fs_drv_t()
fs_driver.fs_register(fs_drv,'S')
# current screen
scr = lv.obj()
scr.set_style_text_font(lv.font_montserrat_16,0)

### Styles  ###################
mont48 = None
try:
    mont48 = lv.binfont_create("S:/montserrat-med-48-2.bin" )
except:
    print("Missing font file on flash.  Will use default font.")

objstyle = lv.style_t()
objstyle.init()
objstyle.set_radius(2)
objstyle.set_bg_color(lv.color_hex(0x00ffff))  # cyan

letterstyle = lv.style_t()
letterstyle.init()
letterstyle.set_drop_shadow_opa(lv.OPA._50)
letterstyle.set_drop_shadow_color(lv.palette_main(lv.PALETTE.BLUE))
letterstyle.set_drop_shadow_offset_x(3)
letterstyle.set_drop_shadow_offset_y(3)

dropstyle = lv.style_t()
dropstyle.init()
dropstyle.set_drop_shadow_opa(lv.OPA._50)
dropstyle.set_drop_shadow_color(lv.palette_main(lv.PALETTE.GREY))
dropstyle.set_drop_shadow_radius(8)
dropstyle.set_drop_shadow_offset_x(4)
dropstyle.set_drop_shadow_offset_y(8)

dropstyle2 = lv.style_t()
dropstyle2.init()
dropstyle2.set_drop_shadow_opa(lv.OPA._50)
dropstyle2.set_drop_shadow_color(lv.palette_main(lv.PALETTE.RED))
dropstyle2.set_drop_shadow_offset_x(4)
dropstyle2.set_drop_shadow_offset_y(8)

style_shadow = lv.style_t()
style_shadow.init()
style_shadow.set_text_color(lv.palette_main(lv.PALETTE.GREY))
style_shadow.set_text_opa(lv.OPA._50) 

########################################

screenobj = lv.obj(scr)
screenobj.set_style_pad_row(20, lv.PART.MAIN)
screenobj.set_size(disp.width, disp.height)
screenobj.set_style_border_width(0, lv.PART.MAIN)
screenobj.center()
screenobj.set_flex_flow(lv.FLEX_FLOW.ROW_WRAP)
screenobj.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screenobj.remove_flag(lv.obj.FLAG.SCROLLABLE)

if disp.display_type in ["ili9488","ili9488b"]:
    titlewidth = 320
    squaresize = 80
    squarecount = 6
    arcsize = 130
    pass

titleobj = lv.obj(screenobj)
titleobj.set_size(titlewidth, 80)
titleobj.set_style_border_width(0,0)

title = lv.label(titleobj)
title.set_text("Objects")
title.set_style_text_color(lv.color_black(), 0)
if mont48 != None and disp.display_type in ["ili9488","ili9488b"]:
    title.set_style_text_font(mont48,0)
else:
    title.set_style_text_font(lv.font_montserrat_24,0)
title.add_style(letterstyle,0)
title.center()

for i in range(squarecount):
    obj = lv.obj(screenobj)
    obj.set_size(squaresize, squaresize) 
    obj.add_style(objstyle, 0)
    if i % 3 == 1:
        obj.add_style(dropstyle2, lv.PART.MAIN)
    else:
        obj.add_style(dropstyle, lv.PART.MAIN)
        
    label = lv.label(obj)
    label.set_text(str(i))
    label.set_style_text_font(lv.font_montserrat_16,0)
    label.center()

arc = lv.arc(screenobj)
arc.set_size(arcsize,arcsize)
arc.set_range(0,8)
arc.set_value(4)
arc.add_style(dropstyle2, lv.PART.INDICATOR)

toggleblur = 0

def change(e):
    global toggleblur
    if toggleblur == 0:
        btntext.set_text("Normal")
        btn.set_style_bg_color(lv.palette_main(lv.PALETTE.GREEN),0)
        arc.set_style_blur_radius(15, lv.PART.MAIN)
        toggleblur = 1
    else:
        btntext.set_text("Do Blur")
        btn.set_style_bg_color(lv.palette_main(lv.PALETTE.PURPLE),0)
        arc.set_style_blur_radius(0, lv.PART.MAIN)
        toggleblur = 0

btn = lv.button(screenobj)
btn.add_style(dropstyle, lv.PART.MAIN)
btn.set_style_bg_color(lv.palette_main(lv.PALETTE.PURPLE),0)
btntext = lv.label(btn)
btntext.set_text("Do Blur")

btn.add_event_cb(change, lv.EVENT.CLICKED, None)

def change_shadow(e):
    title.set_style_drop_shadow_offset_x(arc.get_value(),0)
    title.set_style_drop_shadow_offset_y(arc.get_value()*2,0)
    cnt = screenobj.get_child_count()
    for i in range(0,cnt):
        c = screenobj.get_child(i)
        c.set_style_drop_shadow_offset_x(arc.get_value(),0)
        c.set_style_drop_shadow_offset_y(arc.get_value()*2,0)

arc.add_event_cb(change_shadow, lv.EVENT.VALUE_CHANGED, None)
###################################################
lv.screen_load(scr)

# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)