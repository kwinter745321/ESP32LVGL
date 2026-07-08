# test_charset_ssd1306.py
#
# Shows each line of characters on the OLED
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

oled.fill(0)
hold = ""

def display(message):
    parts = [message[i:i+9] for i in range(0, len(message), 9)]
    row = 0
    oled.fill(0)
    for part in parts:
        #print(part)
        oled.text(part, 0, row)
        row += 8
    oled.show()
    
def view(start):
    global hold
    #print("start char:",start)
    display(hold[start:start+45])
    time.sleep(10)


for i in range(32,127):
    hold += chr(i)

for s in range(0,127,45):
    view(s)

oled.fill(0)
oled.show()
