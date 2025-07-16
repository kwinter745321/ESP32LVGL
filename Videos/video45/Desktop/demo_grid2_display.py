# demo_grid2_display.py
#
# Created: 14 July 2025
# Based On: https://github.com/lvgl/lvgl/blob/master/examples/layouts/grid/lv_example_grid_2.c
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

# Create a button with a label
col_dsc = [ 70, 70, 70, lv.GRID_TEMPLATE_LAST ]
row_dsc = [ 50, 50, 50, lv.GRID_TEMPLATE_LAST ]

scr = lv.obj()
lv.screen_load(scr)

cont = lv.obj(scr)
cont.set_grid_dsc_array(col_dsc, row_dsc)
cont.set_size(300, 220)
cont.set_style_bg_color(lv.color_black(), lv.PART.MAIN)
cont.center()
cont.set_layout(lv.LAYOUT.GRID)


obj = lv.obj(cont)
obj.set_size(lv.SIZE_CONTENT, lv.SIZE_CONTENT)
obj.set_grid_cell( lv.GRID_ALIGN.START, 0, 1, lv.GRID_ALIGN.START, 0, 1)
label = lv.label(obj)
label.set_text("c0, r0")

obj = lv.obj(cont)
obj.set_size(lv.SIZE_CONTENT, lv.SIZE_CONTENT)
obj.set_grid_cell( lv.GRID_ALIGN.START, 1, 1, lv.GRID_ALIGN.CENTER, 0, 1)
label = lv.label(obj)
label.set_text("c1, r0")

obj = lv.obj(cont)
obj.set_size(lv.SIZE_CONTENT, lv.SIZE_CONTENT)
obj.set_grid_cell( lv.GRID_ALIGN.START, 2, 1, lv.GRID_ALIGN.END, 0, 1)
label = lv.label(obj)
label.set_text("c2, r0")

obj = lv.obj(cont)
obj.set_size(lv.SIZE_CONTENT, lv.SIZE_CONTENT)
obj.set_grid_cell( lv.GRID_ALIGN.STRETCH, 1, 2, lv.GRID_ALIGN.STRETCH, 1, 1)
label = lv.label(obj)
label.set_text("c1-2, r1")

obj = lv.obj(cont)
obj.set_size(lv.SIZE_CONTENT, lv.SIZE_CONTENT)
obj.set_grid_cell( lv.GRID_ALIGN.STRETCH, 0, 1, lv.GRID_ALIGN.STRETCH, 1, 2)
label = lv.label(obj)
label.set_text("c0\nr1-2")