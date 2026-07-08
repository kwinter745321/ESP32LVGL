# test_circle_ssd1306.py
#
# Displays a circle of pixels on the OLED
#
# Contains code suggested by Google AI
# Created: 07 July 2025
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.28.0-dirty on 2026-05-06;
# ESP32C3 module with ESP32C3
# LVGL 9.5
#

import math
from machine import I2C, Pin
import ssd1306
import time

# 1. Initialize I2C (adjust pins for your specific microcontroller)
i2c = I2C(0, scl=Pin(6), sda=Pin(5), freq=400000)
#oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled = ssd1306.SSD1306_I2C(72, 40, i2c)


# 2. Define a circle function (Bresenham's Midpoint Circle Algorithm)
def draw_circle(x0, y0, radius, color=1):
    f = 1 - radius
    ddf_x = 1
    ddf_y = -2 * radius
    x = 0
    y = radius
    # Draw the initial 4 cardinal points
    oled.pixel(x0, y0 + radius, color)
    oled.pixel(x0, y0 - radius, color)
    oled.pixel(x0 + radius, y0, color)
    oled.pixel(x0 - radius, y0, color)
    while x < y:
        if f >= 0:
            y -= 1
            ddf_y += 2
            f += ddf_y
        x += 1
        ddf_x += 2
        f += ddf_x
        # Draw the 8 symmetric segments of the circle
        oled.pixel(x0 + x, y0 + y, color)
        oled.pixel(x0 - x, y0 + y, color)
        oled.pixel(x0 + x, y0 - y, color)
        oled.pixel(x0 - x, y0 - y, color)
        oled.pixel(x0 + y, y0 + x, color)
        oled.pixel(x0 - y, y0 + x, color)
        oled.pixel(x0 + y, y0 - x, color)
        oled.pixel(x0 - y, y0 - x, color)


# 3. Clear the display and draw our 30-pixel wide circle
# Total width of 30 pixels means a radius of 15
oled.fill(0)
#draw_circle(64, 32, 15, 1)  # Center (64, 32) on a 128x64 screen
draw_circle(36, 20, 15, 1)  # Center (36, 20) on a 72x40 screen
oled.show()
time.sleep(4)
oled.fill(0)
oled.show()
