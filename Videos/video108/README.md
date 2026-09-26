# README.md - Video 108


26 September 2026

# Scope
This is video 108 on a MicroPython LVGL embedded solution. In today’s video we look at the LVGL-MicroPython project created by Kevin Schlosser and others.  His softyware creates LVGL firmware with MicroPython.  We built the firmware for an ESP32-S3 N16R8 device and several displays (ILI9341, ST7796 and the RGB display ST7262). Our Test Rigs is the Waveshare ESP32-S3 Touch-LCD-4.3B device which uses the 480x800 ST7262 display and touchscreen.  After building the firmware we built and demonstrate an interesting Smart Calendar program.  This firmware can ALSO be used by generic ESP32-S3 devices and generic ILI9341/ST7796 displays (with XPT2046 Touchscreen.)
 
In this video, 
 - Demonstrate the standard test program test_matrix3_lcdbus (slightly modified).
 - Briefly review the LCD_Bus technology.
 - Describe the Waveshare ESP32-S3 Touch-LCD-4.3B device.
 - Demonstrate the Smart Calendar program called test_activities_lcdbus.py.

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video108

# Files
At this GitHub site there are three groups of files; a firmware, a directory with Flash files, and finally a Desktop directory with test programs.  Grab the firmware and install it first.  Then load the Flash directory files using a program like Thonny. Finally you can open test_calendar_lcdbus.py in Thonny. 

- Firmware
    - There are two bin files.  
    - This one lvgl_micropy_ESP32_GENERIC_S3-SPIRAM_OCT-8.bin is for generic ESP32-S3 N8R8 devices.  (5MB of storage)
    - If you have a N16R8 (in other words a device with 16 MB flash) then use this lvgl_micropy_ESP32_GENERIC_S3-SPIRAM_OCT-16.bin (13 MB storage)

- Desktop
    - various test programs. 
    - if you like color then try test_matrix3_lcdbus.py

- Flash
    - various flash files. 
    - display_driver is where pins are defined
    - the sdcard driver works but not with the application

