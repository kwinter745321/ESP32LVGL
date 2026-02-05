# test_i2saudio_display.py
#
# Created: 02 February 2026 (custom to the device)
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# Waveshare ESP32-S3-Touch-LCD-3.5C
# MicroPython v1.20.0-2510.gacfeb7b7e.dirty on 2025-11-23;
# Generic ESP32S3 module with ESP32S3

import lvgl as lv
from machine import reset, Pin
from display_driver import disp, touch
from audio_driver import send_audio, set_volume
import time
##from lv_utils import task_handler

lv.init()


         
###############################################
# UI
###############################################

# current screen
scr = lv.obj()
lv.screen_load(scr)
scr.remove_flag(lv.obj.FLAG.SCROLLABLE)

# backlight
bl = Pin(6, Pin.OUT)
bl.on

# songs
songs = ["test1.wav", "7thlife-7.wav", "7thlife-14.wav",]


# initial values
lsbtn = None
current_volume = 60
lbl2b = None

# fonts and colors
n16 = lv.font_montserrat_16
n24 = lv.font_montserrat_24
red = lv.palette_main(lv.PALETTE.RED)
beige = lv.color_hex(0xf5efeb)
gray = lv.color_hex(0xc0c0c0)

# Create a container for the whole screen
cont = lv.obj(scr)
cont.set_size(480, 320)
cont.set_style_bg_color(beige,lv.PART.MAIN)
cont.center()
cont.set_flex_flow(lv.FLEX_FLOW.COLUMN_WRAP)
cont.set_flex_align(
    lv.FLEX_ALIGN.START, 
    lv.FLEX_ALIGN.START,
    lv.FLEX_ALIGN.START
)
cont.set_style_pad_all(10, 0)

def find_song(name):
    idx = 0
    for item in songs:
        if name in item:
            set_focus(idx)
            last_played(idx)
            send_audio(item)
            clear_focus(idx)
            break
        idx += 1
    return idx

def name_list_cb(e):
    code = e.get_code()
    if code == lv.EVENT.CLICKED:
        lsbtn = e.get_target_obj()
        # Get the text of the button
        btn_text = lsbtn.get_child(1).get_text()
        if code == lv.EVENT.CLICKED:
            print(f"List item clicked: {btn_text}")
            find_song(btn_text)

name_list = lv.list(cont)
name_list.set_size(250, 290) # Set the size of the list
name_list.add_text("Available songs")
name_list.set_style_text_font(n16, 0)

for name in songs:
    btn = name_list.add_button(lv.SYMBOL.AUDIO, name)
    btn.add_event_cb(name_list_cb, lv.EVENT.ALL, None)

listcnt = name_list.get_child_count() - 1 #ignore header
print("Song count:",listcnt)

def btn1cb(e):
    global current_volume
    current_volume = 0
    lblb.set_text(str(current_volume))
    set_volume(current_volume)
    
def btn2cb(e):
    global current_volume
    current_volume = 60
    lblb.set_text(str(current_volume))
    set_volume(current_volume)
    
def btn3cb(e):
    global current_volume
    current_volume = 70
    lblb.set_text(str(current_volume))
    set_volume(current_volume)

obj = lv.obj(cont)
obj.set_size(200,110)
obj.remove_flag(lv.obj.FLAG.SCROLLABLE)
lbl = lv.label(obj)
lbl.set_text("Sound Volume:")
lbl.set_style_text_font(n16, 0)
lblb = lv.label(obj)
lblb.set_text(str(current_volume))
lblb.set_pos(130, 0)
lblb.set_style_text_color(red, 0)
lblb.set_style_text_font(n16, 0)
btn1 = lv.button(obj)
btn1.set_pos(0,30)
btn1lbl = lv.label(btn1)
btn1lbl.set_text(lv.SYMBOL.MUTE)
btn1lbl.set_style_text_font(n24, 0)
btn2 = lv.button(obj)
btn2.set_pos(50,30)
btn2lbl = lv.label(btn2)
btn2lbl.set_text(lv.SYMBOL.VOLUME_MID)
btn2lbl.set_style_text_font(n24, 0)
btn3 = lv.button(obj)
btn3.set_pos(105,30)
btn3lbl = lv.label(btn3)
btn3lbl.set_text(lv.SYMBOL.VOLUME_MAX)
btn3lbl.set_style_text_font(n24, 0)

obj2 = lv.obj(cont)
obj2.set_size(190,80)
obj2.remove_flag(lv.obj.FLAG.SCROLLABLE)
lbl2 = lv.label(obj2)
lbl2.set_text("Last Played:")
lbl2.set_style_text_font(n16, 0)
stat = lv.label(obj2)
stat.set_size(180,40)
stat.set_pos(0,20)
stat.set_text("")
stat.set_style_text_color(red, 0)
stat.set_style_text_font(n16, 0)

btn1.add_event_cb(btn1cb, lv.EVENT.CLICKED, None)
btn2.add_event_cb(btn2cb, lv.EVENT.CLICKED, None)
btn3.add_event_cb(btn3cb, lv.EVENT.CLICKED, None)

def last_played(idx):
    stat.set_text(songs[idx])

def set_focus(idx):
    obj = name_list.get_child(idx)
    obj.set_style_bg_color(gray, 0)
    
def clear_focus(idx):
    obj = name_list.get_child(idx)
    obj.set_style_bg_color(lv.color_white(), 0)
    