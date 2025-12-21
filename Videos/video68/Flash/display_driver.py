# display_driver.py
#
# Created: 17 December 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on:
# LVGL (9.4.0) MicroPython (1.27.0) 
# MicroPython 8dc05cdba3-dirty on 2025-12-17;
# Generic ESP32S3 module with Octal-SPIRAM with ESP32S3
#
from micropython import const
import lcd_bus
import ili9341
import _ili9341_init_type1
import _ili9341_init_type2
import touch_cal_data 
import xpt2046
from machine import Pin, SPI, reset
import machine
import lvgl as lv
import task_handler
import time
import sys

lv.init()

_MOSI = const(11)
_MISO = const(13)
_SCK =  const(12)

_WIDTH = 240
_HEIGHT = 320
_LCD_CS =   const(10)
_LCD_RST =  const(4)
_LCD_DC =   const(7)
_LCD_BL = const(46)
_LCD_FREQ = const(80_000_000)

_TOUCH_CS = const(5)
_TOUCH_FREQ = const(1_000_000)

#########################################################################
# Hard coded the calibrate; if you comment, remove line 99 and 107 below
#########################################################################
cal = touch_cal_data.TouchCalData('')
cal.alphaX = 0.0344256
cal.betaX = 0.9180161
cal.deltaX = -19.963024                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
cal.alphaY = 1.6243784
cal.betaY = -0.01657529
cal.deltaY = -30.847888
cal.mirrorX = False
cal.mirrorY = False
#############################################

spi_bus = SPI.Bus(
    host=1,    #SPI-2
    mosi=_MOSI,
    miso=_MISO,
    sck=_SCK
)

data_bus = lcd_bus.SPIBus(
    spi_bus=spi_bus,
    dc=_LCD_DC,
    cs=_LCD_CS,
    freq=_LCD_FREQ,
)

display = ili9341.ILI9341(
    data_bus=data_bus,
    display_width=_WIDTH,
    display_height=_HEIGHT,
    reset_pin=_LCD_RST,
    reset_state=ili9341.STATE_LOW,
    backlight_pin=_LCD_BL,
    backlight_on_state=ili9341.STATE_HIGH,
    color_space=lv.COLOR_FORMAT.RGB565,
    color_byte_order=ili9341.BYTE_ORDER_BGR,
    rgb565_byte_swap=True
)

display.set_power(1)
display.init(1)
#display.set_color_inversion(True)
display.set_rotation(lv.DISPLAY_ROTATION._0)
display.set_backlight(100)

touch_dev = machine.SPI.Device(
    spi_bus=spi_bus,
    freq=_TOUCH_FREQ,
    cs=_TOUCH_CS
)

indev = xpt2046.XPT2046(
    device=touch_dev,
    touch_cal=cal,
    debug=False
)

# enter cal.reset() in shell to force calibrate
if not indev.is_calibrated:
    if display.get_rotation() == 0:
        indev.calibrate()
        cal.save()
    else:
        print("Please set rotation to 0")

th = task_handler.TaskHandler()   
# un-comment to force it to re-calibrate
#indev.calibrate()
print("The calibrate status s: ", indev.is_calibrated)