# README - video 35 - MicroPython LVGL 9 - Is it pioneering a new way? Part 2

# Topic 22 May 2025
This is video 35 on MicroPython and LVGL. This is the second video of a two part miniseries on the LVGL MicroPython pioneering efforts These efforts are being developed on ESP32, but are destined for many platforms like the RPI Pico.  For this video, we rebuilt the ESP32-S3 firmware (again).  We used the new Binding approach for ESP32. We discuss the new API now available and use it to setup another example.

The hardware, mounted on a breadboard, is the WeAct Studios ESP32-S3-Oct (N16R8) USB board and a standard ILI9341 display.

In this video,
    • Demonstrate the temp-humidity program again (but on the new firmware)
    • Discuss the firmware build, the API and setup changes
    • Review the code on a simple example
    • Provide impressions


The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL

Repo:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video35

The Pico MP Display Base Board is available for purchase:
https://www.tindie.com/products/aiy745321/pico-mp-display-board/
This board is for standard Pico, PicoW, and Pico2 USB Boards.

# Contents
This directory contains the files for this video.  

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop   | temp_humidity_lcdbus.py | The demonstration program  |
|           | test_slider_lcdbus.py        | The demonstration program  |
|           |                      |                            |
| Firmware  |                      |                            |
| -May2025  |                      |                            |
| -MP-LVGL9.2.2-1.24-ESP32-S3-Oct-LCD-Bus          |lvgl_micropy_ESP32_GENERIC_S3-SPIRAM_OCT-8.bin          |   ESP32 firmware  (MP1.24.1 and LVGL 9.2.2)  |
|           |                      |                                 |
|           |                      |                                 |
| Pico      |                      |                             |
|           |                      |                              |
|           |Driver files          |  |
|           |   secret.py          | Put your wireless service-name and password here.
|           |                      |                                             |
|           |                      |                                                 |

