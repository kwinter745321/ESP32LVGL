# test_each_ssd1306.py
#
# Slowly shows each character on the OLED
#
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
from machine import Pin, I2C
import ssd1306
import time

# Initialize I2C (Pin numbers depend on your board, e.g., ESP32 or Pico)
i2c = I2C(0, scl=Pin(6), sda=Pin(5)) 
oled = ssd1306.SSD1306_I2C(72, 40, i2c)

# Clear screen
oled.rotate(0)
oled.fill(0)


def view(start):
    global oled
    x = 0
    y = 0
    oled.fill(0)
    for i in range(start, start+45):
        if i > 126:
            break
        char_str = chr(i)
        oled.text(char_str, x, y)
        oled.show()
        time.sleep(0.1) # Pause to see each character
        
        x += 8 # Move to the next character position (8 pixels wide)
        if x > 64:  #nine characters
            x = 0
            y += 8 # Move to next line (8 pixels tall)

# Display characters 32 through 126 (Standard ASCII)
view(32)
time.sleep(10)
view(77)
time.sleep(10)
view(122)
time.sleep(10)
#oled.fill(0)
#oled.show()
