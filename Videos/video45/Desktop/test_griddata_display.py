# test_griddata_display.py
#
# Created: 14 July 2025
# Based On: https://github.com/lvgl/lvgl/blob/master/examples/layouts/grid/lv_example_grid_1.c
#
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on:
# https://sim.lvgl.io/v9.0/micropython/ports/javascript/index.html
# MicroPython v1.20.0-2504.g9fe842956 on 2025-05-17; Generic ESP32S3 module with Octal-SPIRAM with ESP32S3
# MPy 1.24.1
# LVGL 9.3
#
import display_driver
import lvgl as lv
from machine import reset
import random

# Create a button with a label
col_dsc = [ 100, 80, 80, lv.GRID_TEMPLATE_LAST ]
row_dsc = [ 50, 50, 60, lv.GRID_TEMPLATE_LAST ]
label1 = None
label2 = None

#### Subject #############################
tempsubj = lv.subject_t()
tempsubj.init_int(72)

temp = 72
templist = []
count = 1

scr = lv.obj()
lv.screen_load(scr)

cont = lv.obj(scr)
cont.set_grid_dsc_array(col_dsc, row_dsc)
cont.set_size(320, 220)
cont.set_style_bg_color(lv.color_black(), lv.PART.MAIN)
cont.center()

def get_sample():
    global temp
    temp = 72 + random.randint(-5,10)
    tempsubj.set_int(temp)
    label1.set_text("%d\nDeg F" % temp)
    
def calc():
    count = len(templist)
    if count > 10:
        templist.pop(0)
        count = 10
    sum = 0
    for t in templist:
        sum += t
    avg = sum / count
    label2.set_text("%.1f Deg F\nCount: %d" % (avg,count) )
    
def save():
    global temp
    templist.append(temp)
    calc()

def list():
    txt = ""
    eol = ""
    cnt = 0
    for t in templist:
        if cnt == 3:
            cnt = 0
            eol = '\n'
        txt += str(t) + "," + eol
        eol = ""
        cnt += 1
    label2.set_text(txt[:-1])

def button_cb(event):
    btn = event.get_target_obj()
    lbl = btn.get_child(0)
    if lbl:
        txt = lbl.get_text()
        if txt == "Sample":
            get_sample()
        if txt == "List":
            list()
        if txt == "Clear":
            global templist
            templist = [72]
            calc()
            label1.set_text("")
       

btn1 = lv.button(cont)
btn1.set_size(lv.SIZE_CONTENT, lv.SIZE_CONTENT)
btn1.set_grid_cell( lv.GRID_ALIGN.START, 0, 1, lv.GRID_ALIGN.START, 0, 1)
btn1.set_style_bg_color(lv.palette_main(lv.PALETTE.BLUE),lv.PART.MAIN)
btn1.set_style_text_color(lv.color_black(), lv.PART.MAIN)
lbl1 = lv.label(btn1)
lbl1.set_text("Sample")

btn2 = lv.button(cont)
btn2.set_size(lv.SIZE_CONTENT, lv.SIZE_CONTENT)
btn2.set_grid_cell( lv.GRID_ALIGN.START, 1, 1, lv.GRID_ALIGN.START, 0, 1)
btn2.set_style_bg_color(lv.palette_main(lv.PALETTE.BLUE),lv.PART.MAIN)
btn2.set_style_text_color(lv.color_black(), lv.PART.MAIN)
lbl2 = lv.label(btn2)
lbl2.set_text("List")

btn3 = lv.button(cont)
btn3.set_size(lv.SIZE_CONTENT, lv.SIZE_CONTENT)
btn3.set_grid_cell( lv.GRID_ALIGN.START, 2, 1, lv.GRID_ALIGN.START, 0, 1)
btn3.set_style_bg_color(lv.palette_main(lv.PALETTE.BLUE),lv.PART.MAIN)
btn3.set_style_text_color(lv.color_black(), lv.PART.MAIN)
lbl3 = lv.label(btn3)
lbl3.set_text("Clear")

btn1.add_event_cb(button_cb, lv.EVENT.CLICKED, None)
btn2.add_event_cb(button_cb, lv.EVENT.CLICKED, None)
btn3.add_event_cb(button_cb, lv.EVENT.CLICKED, None)

obj1 = lv.obj(cont)
obj1.set_size(lv.SIZE_CONTENT, lv.SIZE_CONTENT)
obj1.set_grid_cell( lv.GRID_ALIGN.STRETCH, 0, 1, lv.GRID_ALIGN.STRETCH, 1, 2)
obj1.set_style_bg_color(lv.color_black(), lv.PART.MAIN)
label1 = lv.label(obj1)
label1.set_text("72\nDeg F")
label1.set_style_text_color(lv.palette_main(lv.PALETTE.YELLOW), 0)
label1.set_style_text_font(lv.font_montserrat_24, 0)

obj2 = lv.obj(cont)
obj2.set_size(lv.SIZE_CONTENT, lv.SIZE_CONTENT)
obj2.set_grid_cell( lv.GRID_ALIGN.STRETCH, 1, 2, lv.GRID_ALIGN.STRETCH, 1, 2)
obj2.set_style_bg_color(lv.color_black(), lv.PART.MAIN)
label2 = lv.label(obj2)

label2.set_style_text_color(lv.palette_main(lv.PALETTE.YELLOW), 0)
label2.set_style_text_font(lv.font_montserrat_24, 0)


#### Observer and Callback ###################################
def temp_observer_cb(observer, subject):
    if observer != None:
        save()

# observer
observer = tempsubj.add_observer(temp_observer_cb, None)    

