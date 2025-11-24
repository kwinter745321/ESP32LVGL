# test_matrix4_display.py
#
# Created: 28 April 2025
# Update:  21 November 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.20.0-2504.g9fe842956 on 2025-05-17; Generic ESP32 module with ESP32

import lvgl as lv
from machine import reset, Pin
from display_driver import disp
import time
lv.init()

bl = Pin(21, Pin.OUT)
bl.on()

# Create a button with a label

scr = lv.obj()
lv.screen_load(scr)
hold = None


def draw_event_cb(e):
    global hold
    print("Event")
    hold = e.get_target_obj
    #dsc = lv.obj_draw_part_dsc_t.__cast__(e.get_param())
    dsc = hold
    #print("dsc",dsc.part)
    #if dsc.part == lv.PART.TICKS and dsc.id == lv.chart.AXIS.PRIMARY_X:
        #month = ["Jan", "Febr", "March", "Apr", "May", "Jun", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
        # dsc.text is defined char text[16], I must therefore convert the Python string to a byte_array
        #dsc.text = bytes(month[dsc.value],"ascii")
#
# Add ticks and labels to the axis and demonstrate scrolling
#
wrapper = lv.obj(scr)
wrapper.set_size(320,240)

title = lv.label(scr)
title.set_text("First Five Months")
title.set_style_text_font(lv.font_montserrat_24, 0)
title.align(lv.ALIGN.CENTER, 0, -100)

# Create a chart
chart = lv.chart(wrapper)
chart.set_size(300, 170)
chart.center()
chart.set_type(lv.chart.TYPE.BAR)
#chart.set_range(lv.chart.AXIS.PRIMARY_Y, 0, 100)
#chart.set_range(lv.chart.AXIS.SECONDARY_Y, 0, 400)
chart.set_point_count(5)
#chart.add_event_cb(draw_event_cb, lv.EVENT.DRAW_MAIN_BEGIN, None)

# Add ticks and label to every axis
#chart.set_axis_tick(lv.chart.AXIS.PRIMARY_X, 10, 5, 12, 3, True, 40)
# chart.set_axis_tick(lv.chart.AXIS.PRIMARY_Y, 10, 5, 6, 2, True, 50)
# chart.set_axis_tick(lv.chart.AXIS.SECONDARY_Y, 10, 5, 3, 4,True, 50)
scale_bottom = lv.scale(wrapper)
scale_bottom.set_mode(lv.scale.MODE.HORIZONTAL_TOP)
scale_bottom.set_size(lv.pct(100), 210)
scale_bottom.set_total_tick_count(5)
scale_bottom.set_major_tick_every(1)
scale_bottom.set_style_pad_hor(lv.chart.get_first_point_center_offset(chart),0)
month = []
month = ["Jan", "Feb", "Mar", "Apr", "May", None]
scale_bottom.set_text_src(month)

# Zoom in a little in X
#chart.set_zoom_x(800)

# Add two data series
ser1 = lv.chart.add_series(chart, lv.palette_lighten(lv.PALETTE.ORANGE, 2), lv.chart.AXIS.PRIMARY_Y)
ser2 = lv.chart.add_series(chart, lv.palette_darken(lv.PALETTE.GREEN, 2), lv.chart.AXIS.SECONDARY_Y)

# # Set the next points on 'ser1'
chart.set_next_value(ser1, 31)
chart.set_next_value(ser1, 66)
chart.set_next_value(ser1, 10)
chart.set_next_value(ser1, 89)
chart.set_next_value(ser1, 63)


# # Directly set points on 'ser2'
ser2.y_points = [92,71,61,15,21,]

chart.refresh()  # Required after direct set