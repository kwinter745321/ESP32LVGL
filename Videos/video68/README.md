# README.md - Video 68

21 December 2025

# Scope

This is video 68 on a MicroPython/LVGL embedded solution. In this video, we discuss the latest firmware build and how to use two widgets: Calendar and Window.  Our Test Rig uses an ESP32-S3-N16R8 USB Board wired to an ILI9341 integrated display with a xpt2046 touchscreen. The MicroPython team recently released v1.27.0 and the LVGL team released LVGL 9.4.0. So, our firmware is combined with these new features.  Finally, the firmware was built with the LCD Bus style drivers. This firmware includes drivers for the following displays (embedded in the firmware): GC9A01, ILI9341, ST7735, ST7796.  Also, there are two embedded touchscreens XPT2046 and GT911. Of course, you can still use your drivers as before.

You can fetch the firmware and programs from the GitHub, and begin using them immediately.  

In this video, 
 - Demonstrate several widgets: lv.calendar and lv.window.
 - Present the firmware build and test rig wiring.
 - Research of the Calendar and Window widgets.
 - Walk through the driver and program code.

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video68

# Note

At the time of publication, We had trouble configuring the touchscreen for Landscape mode (the display happily rotates).  As the demonstration actually needed the display in Portrait mode, we left it as portrait orientation.


# Files

Firmware

 - lvgl_micropy_ESP32_GENERIC_S3-SPIRAM_OCT-16.bin

Desktop

 - test_slider2_lcdbus.py  (often used as a diagnostic to verify the touchscreen)
 - test_window_lcdbus.py
 - test_calendar_lcdbus.py

Flash

 - ch422g.py (IO expander used by GT911)
 - display_driver.py

