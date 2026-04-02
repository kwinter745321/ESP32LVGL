# README.md # Video 83

02 April 2026

# Scope
This is video 83 on a MicroPython/LVGL embedded solution. In this video, we continue to use a Round Touch LCD display but with an ESP32 dev board.  We finish the orientation feature in the display driver.  We demonstrate the LVGL capabilities despite the limited memory.  We demonstrate a clock program which makes a great start for a smart watch style program.  The watch face can be edited to include text and images. 

We use firmware published recently (but it works similar to a previous file.)  Our test rig is an ESP32-C3 SuperMini with an integrated Round GC9A01 Touch Display. You can fetch the firmware and programs from our GitHub site, and begin using them immediately.  

In this video, 
 - We demonstrate our typical button program to show orientation.
 - Also, we demonstrate our clock program to show its smart watch potential.
 - We wire the Round Touch LCD to the ESP32-C3 SuperMini
 - We finish the display driver by adding orientation to CST816S touches.
 - We test gestures and Wifi of the SuperMini.

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video83

# Files

 - Desktop
   - test_button3_display.py
   - test_clock_display.py  (includes example for LVGL gestures)
   - test_wifi_connect2.py

 - Firmware
   - firmware.bin  MicroPython 1.20 dirty (1.24) with LVGL 9.3 (for ESP32-C3 )

 - Flash
   - cst816.py (CST816S driver for waveshare touchscreen)
   - display_driver.py (has config for GC9A01 and the CST816s touch)
   - ili9xxx.py
   - lv_utils.py
   - secret.py  (edit this with your credentials)
   - st77xx.py

