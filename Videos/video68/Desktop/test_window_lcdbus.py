# test_window_lcdbus.py
#
# Created: 17 December 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on:
# LVGL (9.4.0) MicroPython (1.27.0) 
# MicroPython 8dc05cdba3-dirty on 2025-12-17;
# Generic ESP32S3 module with Octal-SPIRAM with ESP32S3
#

from machine import Pin, reset

import lvgl as lv
lv.init()
from display_driver import display
from machine import reset

import time

#### Screen ###########################################
#th = task_handler.TaskHandler()

scr = lv.screen_active()
lv.screen_load(scr)
scr.set_style_bg_color(lv.color_white(),0)
scr.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN )

time.sleep(1)
#### UI ###########################################
win = None

def win_cb(event):
    global win
    btn = event.get_target_obj()
    if btn:
        img = btn.get_child(0)
        p = img.get_parent()
        idx = p.get_index()
        if idx == 3:
            print("Clicked close")
            win.delete()
            
cnt = 0
def btn_cb(event):
    global cnt
    cnt += 1
    msg = "Clicked: " + str(cnt)
    label.set_text(msg)
    print(msg)
            
def show_win():
    global win
    win = lv.win(scr)
    win.set_size(200,200)
    win.set_pos(0,0)
    win.set_style_border_width(2,0)
    win.set_style_bg_color(lv.palette_main(lv.PALETTE.YELLOW),0)
    win.add_title("Win")
    btnl = win.add_button(lv.SYMBOL.LEFT,40)
    btnr = win.add_button(lv.SYMBOL.RIGHT,40)
    btnc = win.add_button(lv.SYMBOL.CLOSE,40)
    cont = win.get_content()
    cont.set_style_bg_color(lv.palette_main(lv.PALETTE.YELLOW),0)
    lbl = lv.label(cont)
    lbl.set_text("Test label")
    lbl.set_style_text_color(lv.color_black(),0)
    btn = lv.button(cont)
    btn.set_size(80,30)
    btn.set_pos(10,70)
    lblbtn = lv.label(btn)
    lblbtn.set_text("Press")
    btnl.add_event_cb(win_cb, lv.EVENT.CLICKED, None)
    btnr.add_event_cb(win_cb, lv.EVENT.CLICKED, None)
    btnc.add_event_cb(win_cb, lv.EVENT.CLICKED, None)
    btn.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)

btnshow = lv.button(scr)
btnshow.set_pos(20,20)
showlbl = lv.label(btnshow)
showlbl.set_text("Show Win")

def btnshow_cb(event):
    show_win()

btnshow.add_event_cb(btnshow_cb, lv.EVENT.CLICKED, None)
    



# btnl.add_event_cb(win_cb, lv.EVENT.CLICKED, None)
# btnr.add_event_cb(win_cb, lv.EVENT.CLICKED, None)
# btnc.add_event_cb(win_cb, lv.EVENT.CLICKED, None)

label = lv.label(scr)
label.set_size(100,16)
label.set_pos(50,250)
#label.align_to(cal, lv.ALIGN.OUT_BOTTOM_MID, 0, 20)
label.set_style_text_color(lv.palette_main(lv.PALETTE.RED),lv.PART.MAIN)
label.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN )
label.set_text("------")



#btn.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)

print("screen loaded")






