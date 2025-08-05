#test_slider-lcdbus.py
#
# Created: 05 Aug 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on:
# LVGL (9.3.0) MicroPython (1.25.0) Binding compiled on 2025-08-05;
# Generic ESP32S3 module with Octal-SPIRAM with ESP32S3
# MicroPython 1.25.0
# LVGL 9.3
#
from micropython import const
import lcd_bus
import ili9341
import _ili9341_init_type1
import _ili9341_init_type2
import xpt2046
from machine import Pin, SPI, SoftSPI, reset
import machine
import lvgl as lv
import task_handler
import time

lv.init()

_MOSI = const(11)
_MISO = const(13)
_SCK =  const(12)

_WIDTH = 240
_HEIGHT = 320
_LCD_CS =   const(10)
_LCD_RST =  const(4)
_LCD_DC =   const(7)
_LCD_FREQ = const(20_000_000)

_TOUCH_CS = const(5)
_TOUCH_FREQ = const(1_000_000)

spi_bus = SPI.Bus(
    host=1,    #SPI-2
    mosi=_MOSI,
    miso=_MISO,
    sck=_SCK
)

display_bus = lcd_bus.SPIBus(
    spi_bus=spi_bus,
    dc=_LCD_DC,
    cs=_LCD_CS,
    freq=_LCD_FREQ,
)

display = ili9341.ILI9341(
    data_bus=display_bus,
    display_width=_WIDTH,
    display_height=_HEIGHT,
    reset_pin=_LCD_RST,
    reset_state=ili9341.STATE_LOW,
    color_space=lv.COLOR_FORMAT.RGB565,
    color_byte_order=ili9341.BYTE_ORDER_BGR,
    rgb565_byte_swap=True
)

display.set_power(1)
display.init(1)

# use for calibration
# calibration is done in Portrait mode
#display.set_rotation(lv.DISPLAY_ROTATION._0)

# in case you want landscape
display.set_rotation(lv.DISPLAY_ROTATION._90)

display.set_backlight(100)

touch_dev = machine.SPI.Device(
    spi_bus=spi_bus,
    freq=_TOUCH_FREQ,
    cs=_TOUCH_CS
)

indev = xpt2046.XPT2046(touch_dev)

# un-comment to force it to re-calibrate
#indev.calibrate()

#if not indev.is_calibrated:
#    display.set_backlight(100)
#    indev.calibrate()
    
th = task_handler.TaskHandler()
scrn = lv.screen_active()

slider = lv.slider(scrn)
slider.set_size(300, 20)
slider.center()

label = lv.label(scrn)
label.set_text('HELLO WORLD!')
label.align(lv.ALIGN.CENTER, 0, -50)

#time.sleep_ms(20)
#lv.screen_load(scrn)
print("Screen loaded")

 