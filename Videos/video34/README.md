# README - video 34 - MicroPython LVGL 9 - Is it pioneering a new way?

# Topic 20 May 2025
This is video 34 on MicroPython and LVGL. This is the first video of a two part miniseries on the LVGL MicroPython pioneering efforts These efforts are being developed on ESP32, but are destined for many platforms like the RPI Pico.  In this video, we use a newly built firmware for an ESP32-S3 board to introduce LVGL 9.3 - MicroPython on the ESP32. We discuss wiring and setup. Then we demonstrate the setup using two previous examples.

The hardware, mounted on a breadboard, is the WeAct Studios ESP32-S3-Oct (N16R8) USB board and a standard ILI9341 display.

In this video,
    • Present firmware, wiring and setup changes
    • Demonstrate using two previous example
    • Provide impressions


The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL

Repo:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video34

The Pico MP Display Base Board is available for purchase:
https://www.tindie.com/products/aiy745321/pico-mp-display-board/
This board is for standard Pico, PicoW, and Pico2 USB Boards.

# Contents
This directory contains the files for this video.  

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop   | temp_humidity_display.py | The demonstration program  |
|           | test_keyboard2.py        | The demonstration program  |
|           |                      |                            |
| Firmware  |                      |                            |
| -May2025  |                      |                            |
| -MP-LVGL9.3-1.24-ESP32-S3-Oct-Legacy          |firmware.uf2          |   ESP32 firmware  (MP1.24.1 and LVGL 9.3)  |
|           |                      |                                 |
|           |                      |                                 |
| Pico      |                      |                             |
|           |                      |                              |
|           |Driver files          |  |
|           |   display_driver.py  | display and touch setup for ILI9341 or ST7796 display. |
|           |   ili9xxx.py         | generic ILI9341 and ST7796 driver  |
|           |   lv_utils.py        | Utility routines for LVGL |
|           |   secret.py          | Put your wireless service-name and password here.
|           |   st7xx.py           | generic driver utilized by both displays.  It's class has the base routines.                                            |
|           |   xpt2046.py       | touch driver updated for 240x320 or 320x480 displays         |
|           |                      |                                             |
|           |                      |                                                 |

