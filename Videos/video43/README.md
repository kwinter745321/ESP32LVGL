# README - video 43

# Topic
This is video 43 on MicroPython and LVGL 9. This video presents the LCD Bus from Kevin Schlosser (new binding approach discussed in Video 35) and uses it to interface to the Waveshare ESP32-S3-Touch-LCD-4.3 device.  The Waveshare device components are matched to the various MicroPython LVGL modules in the firmware.

In this video, 
 - Demonstrate a working program
 - Explore the Waveshare wiki to understand the components
 - Discuss the lcd_bus modules used to configure the Waveshare components
 - Review the display and sdcard drivers

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL

Repo:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video43


# Contents
This directory contains the files for this video.  

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop   | test_matrix2_lcdbus.py | Demostrate display, io-expander, gt911 touch drivers  |
|           | test_button2_lcdbus.py | Demostrate above with sdcard/fs_sdriver  |
|           |                      |                            |
| Firmware  |                      |                            |
| - May2025  |                      |                            |
| - MP-LVGL9.3-1.24-ESP32-S3-Oct-LCD-BUS  |                      |
|           |                      |                                 |
| Flash     | Driver files         |                             |  
|           | display_driver.py    | Configure lcd_bus, rgb_display, io expander and gt911 touch classes   |
|           | ch422g.py            | ch422g driver for io expander       |
|           | sdcard_driver.py     | Configure spi_bus               |
|           |                      |                                 |
| sdcard    |                      |                                 |
| - font     |font files       |  Mostly montserrat and a few samples  |
|           |                      |                                 |