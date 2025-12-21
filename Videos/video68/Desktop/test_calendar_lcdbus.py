# test_calendar_lcdbus.py
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

import time

#### Screen ###########################################
#th = task_handler.TaskHandler()

scr = lv.screen_active()
lv.screen_load(scr)
scr.set_style_bg_color(lv.color_white(),0)
scr.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN )

time.sleep(1)
#### UI ###########################################

cal_date = lv.calendar_date_t()


# Get the current time as a tuple
current_time = time.localtime()

# Extract the year and month
year = current_time[0]  
month = current_time[1]
day = current_time[2]

cald = lv.calendar(scr)
cald.set_pos(0,0)
cald.set_size(240,240)
cald.set_today_date(year,month,day)
cald.set_month_shown(year,month)
cald.set_style_border_color(lv.palette_main(lv.PALETTE.YELLOW), lv.PART.MAIN)
cald.set_style_border_width(5, lv.PART.MAIN)
cald.add_header_dropdown()

label = lv.label(scr)
label.set_size(100,16)
label.set_pos(50,250)
label.set_style_text_color(lv.palette_main(lv.PALETTE.RED),lv.PART.MAIN)
label.set_text("Pick a day")

def date_str(d):
    val = "None"
    if d != None:
        val = "{}-{}-{}".format(d.year,d.month,d.day)
    return val

def cald_cb(event):
    global cal_date
    cald.get_pressed_date(cal_date)
    if cal_date != None:
        dat = date_str(cal_date)
        print(dat)
        if dat != "0-0-0":
            label.set_text(dat)
    
cald.add_event_cb(cald_cb, lv.EVENT.CLICKED, None)

print("Screen loaded")

