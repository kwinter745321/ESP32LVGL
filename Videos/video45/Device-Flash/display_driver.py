# display_driver.py
#
# Updated:  03 July 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
# LVGL (9.2.2) MicroPython (1.24.1) Binding compiled on 2025-06-13; Generic ESP32S3 module with Octal-SPIRAM with ESP32S3
# Waveshare ESP32-S3-Touch-LCD-4.3
# LVGL 9.2.2

import lvgl as lv
import lcd_bus
import rgb_display
import task_handler
import i2c
import gt911
from machine import reset
import time

rgb_bus = lcd_bus.RGBBus(  # ST7262 parallel 800×480 4.3" IPS
    hsync=46,
    vsync=3,
    de=5,
    pclk=7,
    data0=14, data1=38, data2=18, data3=17, data4=10,
    data5=39, data6=0, data7=45, data8=48, data9=47, data10=21,
    data11=1, data12=2, data13=42, data14=41, data15=40,
    freq=13000000,
    hsync_front_porch=8,
    hsync_pulse_width=4,
    hsync_back_porch=8,
    #hsync_idle_low=False,
    vsync_front_porch=16,
    vsync_pulse_width=4,
    vsync_back_porch=16,
    vsync_idle_low=True,
    de_idle_high=False,
    pclk_idle_high=False,
    pclk_active_low=1,
    #disp_active_low=False,
    #refresh_on_demand=False,
)

print("RGBBus",rgb_bus)

_WIDTH, _HEIGHT = 800, 480
_BUF1 = rgb_bus.allocate_framebuffer(_WIDTH * _HEIGHT * 2, lcd_bus.MEMORY_SPIRAM)
_BUF2 = rgb_bus.allocate_framebuffer(_WIDTH * _HEIGHT * 2, lcd_bus.MEMORY_SPIRAM)

display = rgb_display.RGBDisplay(
    data_bus=rgb_bus,
    display_width=_WIDTH,
    display_height=_HEIGHT,
    frame_buffer1=_BUF1,
    frame_buffer2=_BUF2,
    backlight_pin=2,
    color_space=lv.COLOR_FORMAT.RGB565,
    rgb565_byte_swap=False,
)
print("display",display)
display.set_power(True)
display.init()
# Note: defaults to LANDSCAPE Mode
# Note: Backlight is probably turned on above
task_handler = task_handler.TaskHandler()
indev = None

def init_touch():
    global indev
    _WIDTH = const(800)
    _HEIGHT = const(480)

    i2c_bus = i2c.I2C.Bus(host=0, scl=9, sda=8)
    touch_i2c = i2c.I2C.Device(i2c_bus, gt911.I2C_ADDR, gt911.BITS)
    indev = gt911.GT911(touch_i2c, reset_pin=None, startup_rotation=0)
    if indev.hw_size != (_WIDTH, _HEIGHT):
        fw_config = indev.firmware_config
        fw_config.width = _WIDTH
        fw_config.height = _HEIGHT
        fw_config.save()

init_touch()

# width = display._physical_width
# height = display._physical_height
