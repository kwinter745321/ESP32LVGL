# test_simple_ssd1306.py
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
from machine import Pin, SoftI2C
import ssd1306
import time

# Turn off LED
out=Pin(8, Pin.OUT)
out.value(1)

# --- DISPLAY INITIALIZATION ---
i2c = SoftI2C(sda=Pin(5), scl=Pin(6), freq=400000)

# Usually screen dimensions (128x64 or 128x32)
WIDTH = 72
HEIGHT = 40

# Initialize the OLED (Default I2C address is usually 0x3C)
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.rotate(0)


# 1. Clear the screen (0 = Black background)
oled.fill(0)

# 2. Draw static text: text("String", x, y)
oled.text("123456789", 0, 0)
oled.text("line2", 0, 8)
oled.text("line3", 0, 16)
oled.text("line4", 0, 24)
oled.text("line5", 0, 32)
oled.show()
time.sleep(6)
oled.fill(0)

# 3. Draw basic shapes (Pixels and Lines)
oled.pixel(35, 20, 1)          # Single white pixel at center
oled.line(0,0,71,0, 1)
oled.line(0,39,72,39, 1)
oled.line(0,0,0,39, 1)
oled.line(71,0,71,39, 1)
oled.show()
time.sleep(6)
oled.fill(0)

# 4. Simple animation effect
oled.invert(True)              # Invert screen display colors
time.sleep(1)
oled.invert(False)             # Restore normal colors

# 5. End
oled.fill(0)
oled.show()

