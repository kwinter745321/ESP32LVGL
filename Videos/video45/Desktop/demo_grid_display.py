# demo_grid_display.py
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

col_dsc = [ 70, 70, 70, lv.GRID_TEMPLATE_LAST ]
row_dsc = [ 50, 50, 50, lv.GRID_TEMPLATE_LAST ]

scr = lv.obj()
lv.screen_load(scr)

cont = lv.obj(scr)
cont.set_style_grid_column_dsc_array(col_dsc, 0)
cont.set_style_grid_row_dsc_array(row_dsc, 0)
cont.set_size(300, 220)
cont.center()
cont.set_style_bg_color(lv.color_black(), lv.PART.MAIN)
cont.set_layout(lv.LAYOUT.GRID)

obj = None
label = None

for i in range(0,9):
    col = i % 3
    row = i // 3
    print(col, row)
    obj = lv.obj(cont)
    obj.set_grid_cell(lv.GRID_ALIGN.STRETCH, col, 1, lv.GRID_ALIGN.STRETCH, row, 1)
    label = lv.label(obj)
    txt = "c%d,r%d" % (col, row)
    label.set_text(txt)
    label.center()