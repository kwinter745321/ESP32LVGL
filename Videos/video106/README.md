# README.md - Video106

10 September 2026

# Scope
This is video 106 on a MicroPython LVGL embedded solution. In today’s video we look at the recent MicroPython v1.29.0 and analyze the ESP32 features.  We built the firmware for both ESP32-H2 and ESP32-S3. Our Test Rigs utilize both firmware and the ST7796 and GC9A01 displays.
 
In this video, 
 - Demonstrate the standard test programs button3 and matrix3.
 - Briefly review the ESP-NOW capabilities in MicroPython.
 - Briefly review the ESP32-H2 device.
 - Describe the wiring of the Touch Display for the ESP32-S3 and ESP32-H2 devices.
 - Demonstrate ulab processing data from the MPU6050 sensor.


The code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video106

# Files
For this video we built three Test Rigs.
- TestRigs:
  - TestRig 1 - ESP32-S3 N16R8 board with ST7796 display and XPT2046 touchscreen
  - TestRig 2 - ESP32-H2 N4 board with ST7796 display and XPT2046 touchscreen
  - TestRig 3 - ESP32-S3 N16R8 board with GC9A01 display and CS816S touchscreen

 - Firmware
   - ESP32-S3 N16R8 Firmware with MP 1.29.0 LVGL 9.5.0 and ulab 6.12 (4D)
   - ESP32-H2 N4    Firmware with MP 1.29.0 LVGL 9.5.0 and ulab 6.12 (2D)

 - Desktop
   - test_matrix3_display.py
   - test_button3_display.py
   - test_ulab_version.py
   - test_ulab_mpu6050.py

 - Flash-xxxx
 - The display_driver is where you update pin assignments

   - display_driver.py   (Original)
   - dd.py (temporary name) My first attempt to improve this file. Edit pins here; let me know what you think.
   - various other driver files