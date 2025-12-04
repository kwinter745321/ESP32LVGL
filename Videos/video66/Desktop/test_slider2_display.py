# test_slider2_display.py
#
# Created: 08 July 2025
# Update: 14 September 2025
# Update: 03 December 2025 uses image files stored in flash
# Update: This program uses an image downloaded from https://www.freepik.com
#
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.20.0-2504.g9fe842956 on 2025-05-17; Generic ESP32 module with ESP32

import lvgl as lv
from machine import reset, Pin
from display_driver import disp
from widget import ConvertPNG, GaugeSlider, ImageButton
import time
lv.init()

###############################################
# UI
###############################################

# current screen
scr = lv.obj()
lv.screen_load(scr)

#### background and border #######
black = lv.color_black()
# uncomment to make screen background black
#scr.set_style_bg_color(black,lv.PART.MAIN)
scr.set_style_border_width(2, lv.PART.MAIN)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.YELLOW),lv.PART.MAIN)
bg_color = scr.get_style_bg_color(lv.PART.MAIN)
dark = bg_color.eq(black)

#### Read PNG files from flash directory
arrow_dsc = ConvertPNG("Arrow.png").dsc
right_dsc = ConvertPNG("Button48.png").dsc
left_dsc = ConvertPNG("Button48L.png").dsc

#### Label ###############################      
label1 = lv.label(scr)
label1.align(lv.ALIGN.BOTTOM_MID, 0,-30)
label1.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN)
label1.set_text("Value: 50")

slider = GaugeSlider(scr, arrow_dsc, label1, 0,0, dark=dark)
slider.set_text("Value: ")
slider.set_value(40)
if slider.dark:
    label1.set_style_text_color(lv.color_white(), lv.PART.MAIN)

#slider.cont.set_size(lv.pct(50), 70)

#### Buttons ##################
right = ImageButton(scr, right_dsc, 48, 48, disp.width-75, disp.height-65)
left = ImageButton(scr, left_dsc, 48, 48, 25, disp.height-65)

def rightcb(e):
    val = slider.get_value()
    val = (val//5)*5 + 5
    if val>100:
        val = 100
    slider.set_value(val)
    label1.set_text("Value: {}".format( slider.get_value() ) )
    
def leftcb(e):
    val = slider.get_value()
    val = (val//5)*5 - 5
    if val<=0:
        val = 0
    slider.set_value(val)
    label1.set_text("Value: {}".format( slider.get_value() ) )
    
right.action(rightcb)
left.action(leftcb)

#### END UI ###############################################

# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)
