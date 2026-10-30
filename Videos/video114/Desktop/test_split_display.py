# test_split_display.py
#
# Created: 25 October 2026
# Verified: 26 October 2026
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.29.0-dirty on 2026-10-24;
# Raspberry Pi Pico 2 W with RP2350
# LVGL 9.6

import lvgl as lv
from machine import reset, Pin
#from display_driver import disp, touch
from dd import disp, touch, backlight
import time

start_time = time.ticks_ms()

SPLIT_MIN_PANE = 60
SPLIT_DIVIDER_W = 12

###############################################
# UI
###############################################
hold = None
# current screen
scr = lv.obj()
lv.screen_load(scr)
scr.set_style_bg_color(lv.color_hex(0x0),lv.PART.MAIN)
scr.set_style_text_font(lv.font_montserrat_24,0)
# scr.set_style_border_width(2, lv.PART.MAIN)
# scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),lv.PART.MAIN)

def splitter_pressing_cb(event):
    divider = event.get_target_obj()
    cont = divider.get_parent()
    pane_left = cont.get_child(0)
    # indev = lv.indev_active()
    # if indev ==  None:
    #     return
    # else:
    #     hold = indev
    ##p = lv.point_t()
    ##indev.get_point(p)
    pos = touch.pos()
    if pos == None:
        return
    
    divider.set_style_bg_color(lv.palette_main(lv.PALETTE.ORANGE),0)
    content = lv.area_t()
    cont.get_content_coords(content)
    avail = content.get_width() - SPLIT_DIVIDER_W
    px = content.get_width() - pos[1]  # force touch to work
    if avail <= 2*SPLIT_MIN_PANE:
        return
    left_w = (px - content.x1) - SPLIT_DIVIDER_W // 2
    if left_w < SPLIT_MIN_PANE:
        left_w = SPLIT_MIN_PANE
    if left_w > avail - SPLIT_MIN_PANE:
        left_w = avail - SPLIT_MIN_PANE
    pane_left.set_width(left_w)

def splitter_release_cb(event):
    divider = event.get_target_obj()
    divider.set_style_bg_color(lv.palette_main(lv.PALETTE.GREY),0)

def lv_example_split():
    cont = lv.obj(scr)
    cont.set_size(lv.pct(100),lv.pct(100))
    cont.set_scrollable(False)   # 9.6
    cont.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
    cont.set_style_pad_all(0,0)
    cont.set_style_border_width(0,0)
    cont.set_flex_flow(lv.FLEX_FLOW.ROW)

    pane_left = lv.obj(cont)
    pane_left.set_height(lv.pct(100))
    pane_left.set_width(lv.pct(50))
    pane_left.set_style_bg_color(lv.color_hex(0xe8f0fe),0)
    label_left = lv.label(pane_left)
    label_left.set_text("Left\n(drag the divider)")
    label_left.center()
    #
    divider = lv.obj(cont)
    divider.set_size(SPLIT_DIVIDER_W, lv.pct(100))
    divider.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
    divider.set_style_radius(0,0)
    divider.set_style_border_width(0,0)
    divider.set_style_bg_color(lv.palette_main(lv.PALETTE.GREY),0)
    divider.add_event_cb(splitter_pressing_cb, lv.EVENT.PRESSING, None)
    divider.add_event_cb(splitter_release_cb, lv.EVENT.RELEASED, None)
    #
    pane_right = lv.obj(cont)
    pane_right.set_height(lv.pct(100))
    pane_right.set_flex_grow(1)
    pane_right.set_style_bg_color(lv.color_hex(0xe6f4ea),0)
    label_right = lv.label(pane_right)
    label_right.set_text("Right")
    label_right.center()


lv_example_split()

###################################################


# elapsed = time.ticks_diff(time.ticks_ms(), start_time)
# print(f"Event took {elapsed} ms")

# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)





