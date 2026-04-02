# test_clock_gc9a01.py
#
# Created: 17 October 2025
# Updated: 01 April 2026
#
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.20.0-2510.gacfeb7b7e.dirty on 2026-04-01;
# ESP32C3 module with ESP32C3
#
import lvgl as lv
from machine import SPI, Pin
import display_driver
from display_driver import disp
import time
from machine import reset
import machine

import utime
import math

bl = Pin(10, Pin.OUT)
bl.on()

#### UI ####
scr = lv.obj()
lv.screen_load(scr)

custom_labels = ["","1","2","3","4","5","6","7","8","9","10","11","12"]
cell = None

blue = lv.palette_main(lv.PALETTE.BLUE)
yellow = lv.palette_main(lv.PALETTE.YELLOW)
red = lv.palette_main(lv.PALETTE.RED)
green = lv.palette_main(lv.PALETTE.GREEN)
grey = lv.color_hex(0x898989)
white = lv.color_white()
black = lv.color_black()
#######################################################

# #### Scale ##############
scale = lv.scale(scr)
scale.set_text_src(custom_labels)
scale.set_range(0, 60)
scale.set_angle_range(360)   # draw scale as a circle
scale.center()
scale.set_size(240, 240)
scale.set_mode(lv.scale.MODE.ROUND_INNER)
scale.set_rotation(270)      # rotate scale so it looks like a clock
scale.set_style_bg_opa(lv.OPA.COVER, lv.PART.MAIN)
scale.set_style_bg_color(lv.color_black(), lv.PART.MAIN)
scale.set_label_show(True)

scale.set_total_tick_count(61)
scale.set_major_tick_every(5)
scale.set_style_line_width(1, lv.PART.ITEMS)
scale.set_style_line_width(4, lv.PART.INDICATOR)
scale.set_style_length(5, lv.PART.ITEMS)
scale.set_style_length(9, lv.PART.INDICATOR)
scale.set_style_text_font(lv.font_montserrat_24,lv.PART.MAIN)
scale.set_style_text_color(lv.color_white(), lv.PART.INDICATOR) # numbers
scale.set_style_line_color(lv.color_white(), lv.PART.ITEMS) # ticks
scale.set_style_line_color(lv.color_white(), lv.PART.INDICATOR)  #major tick

# # Create a style for the clock face
style_face = lv.style_t()
style_face.init()
style_face.set_radius(lv.RADIUS_CIRCLE)
style_face.set_border_width(0)

# Create the clock face object
clock_face = lv.obj(scr)
clock_face.set_size(140, 140)
clock_face.set_style_bg_opa(lv.OPA.TRANSP, lv.PART.MAIN)
#clock_face.set_style_border_width(0, lv.PART.MAIN)
clock_face.align(lv.ALIGN.CENTER, 0, 0)
clock_face.add_style(style_face, lv.PART.MAIN)

# Create a style for the clock hands
style_hand = lv.style_t()
style_hand.init()
style_hand.set_line_width(4)
style_hand.set_line_color(blue)
style_hand.set_line_rounded(True)

# clock_face code suggested by google upon search on 17 October 2025
# Define the center of the clock face
center_x, center_y = 110, 110
hand_length_h = 50
hand_length_m = 75
hand_length_s = 85

def content(parent):
    global cell
    cont = lv.obj(parent)
    cont.set_pos(35,35)
    cont.set_size(170,85)
    cont.center()
    cont.set_style_border_width(0, lv.PART.MAIN)
    cont.set_style_bg_opa(lv.OPA.TRANSP, lv.PART.MAIN)
    cont.add_flag(lv.obj.FLAG.FLOATING)
#     cont.set_layout(lv.LAYOUT.GRID)
#     cont.set_style_grid_column_dsc_array(col_dsc, 0)
#     cont.set_style_grid_row_dsc_array(row_dsc, 0)
    cont.set_flex_flow(lv.FLEX_FLOW.ROW_WRAP)
    cont.set_style_pad_left(20, lv.PART.MAIN)
    cont.set_flex_align(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.CENTER)
    cell = lv.label(cont)
    cell.set_size(120,50)
    cell.set_style_text_color(white, lv.PART.MAIN)

# Create a parent object for the hands to handle rotation
hand_parent = lv.obj(clock_face)
hand_parent.set_size(240, 240)
hand_parent.align(lv.ALIGN.CENTER, 0, 0)
hand_parent.add_flag(lv.obj.FLAG.FLOATING) # Prevents parent style from affecting hands
hand_parent.set_style_bg_color(black,lv.PART.MAIN)
#hand_parent.set_style_bg_opa(lv.OPA.TRANSP, lv.PART.MAIN)
hand_parent.set_style_border_width(0, lv.PART.MAIN)
#hand_parent.set_style_bg_color(yellow,lv.PART.MAIN)
hand_parent.add_style(style_face, lv.PART.MAIN)
content(hand_parent)

# Create the hour hand
hour_hand = lv.line(hand_parent)
hour_points = [
    {"x": center_x, "y": center_y},
    {"x": center_x, "y": center_y - hand_length_h}
]
hour_hand.set_points(hour_points, 2)
hour_hand.add_style(style_hand, 0)

# Create the minute hand
minute_hand = lv.line(hand_parent)
minute_points = [
    {"x": center_x, "y": center_y},
    {"x": center_x, "y": center_y - hand_length_m}
]
minute_hand.set_points(minute_points, 2)
minute_hand.add_style(style_hand, 0)

# Create the second hand (make it a different color)
style_sec_hand = lv.style_t()
style_sec_hand.init()
style_sec_hand.set_line_width(2)
style_sec_hand.set_line_color(lv.palette_main(lv.PALETTE.RED))
style_sec_hand.set_line_rounded(True)

second_hand = lv.line(hand_parent)
second_points = [
    {"x": center_x, "y": center_y},
    {"x": center_x, "y": center_y - hand_length_s}
]
second_hand.set_points(second_points, 2)
second_hand.add_style(style_sec_hand, 0)

def update_clock_cb(timer):
    """Callback function to update the clock hands every second."""
    # Get the current time from utime.localtime()
    #
    current_time = utime.localtime()
    #print(current_time)
    hours = current_time[3]
    minutes = current_time[4]
    seconds = current_time[5]

    # Convert hours to 12-hour format
    if hours >= 12:
        hours -= 12

    # Calculate the angle for each hand in degrees, where 0 degrees is at the 12 o'clock position
    # The `set_rotation` function on the parent rotates all child hands together,
    # so we update the hand positions manually relative to the center
    #
    angle_h = (hours * 30) + (minutes * 0.5) - 90  # -90 for 12 o'clock start position
    angle_m = (minutes * 6) - 90
    angle_s = (seconds * 6) - 90

    # Convert angles to radians for mathematical calculations
    rad_h = math.radians(angle_h)
    rad_m = math.radians(angle_m)
    rad_s = math.radians(angle_s)

    # Calculate the new end-point coordinates for each hand
    h_x_end = int(center_x + hand_length_h * math.cos(rad_h))
    h_y_end = int(center_y + hand_length_h * math.sin(rad_h))
    m_x_end = int(center_x + hand_length_m * math.cos(rad_m))
    m_y_end = int(center_y + hand_length_m * math.sin(rad_m))
    s_x_end = int(center_x + hand_length_s * math.cos(rad_s))
    s_y_end = int(center_y + hand_length_s * math.sin(rad_s))
    
    # Update the hands' points
    new_h_points = [
        {"x": center_x, "y": center_y},
        {"x": h_x_end, "y": h_y_end}
    ]
    hour_hand.set_points(new_h_points, 2)
    
    new_m_points = [
        {"x": center_x, "y": center_y},
        {"x": m_x_end, "y": m_y_end}
    ]
    minute_hand.set_points(new_m_points, 2)

    new_s_points = [
        {"x": center_x, "y": center_y},
        {"x": s_x_end, "y": s_y_end}
    ]
    second_hand.set_points(new_s_points, 2)
    
# Create an LVGL timer that calls the update_clock_cb function every 1000ms
timer = lv.timer_create(update_clock_cb, 1000, None)

def pageone():
    print("page one")
    
def pagetwo():
    print("page two")


def swipe(event):
    indev = lv.indev_active()
    ges_dir = indev.get_gesture_dir()
    if ges_dir:
        if ges_dir == lv.DIR.TOP:
            print("home")
        if ges_dir == lv.DIR.LEFT:
            print("left")
            #pageone()
        if ges_dir == lv.DIR.RIGHT:
            print("right")
            pagetwo()
        if ges_dir == lv.DIR.BOTTOM:
            print("down")
            dt = time.localtime()
            #(2026, 3, 29, 16, 8, 49, 6, 88)
            dts = "{0}-{1}-{2}\n{3}:{4}:{5}".format(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5]) 
            cell.set_text(dts)

scr.add_event_cb(swipe, lv.EVENT.GESTURE, None)

print("Perform a down gesture.")


