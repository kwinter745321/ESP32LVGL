# README - video 37 - MicroPython LVGL 9 - Introduction to ESP32 - Generic

# Topic 30 May 2025
This is video 37 on MicroPython and LVGL. This video introduces MP-LVGL firmware for the ESP32-Generic based US boards.  Two implementations are discussed: 1) a generic ESP32-WROOM-32 USB board wired to an ILI9341 display (with Touch), and 2) the ESP-2432S028 USB Board aka Cheap Yellow Display, (CYD). We discuss the wiring and drivers.

In this video,
 - Discuss the two test rigs
 - Discuss the wiring for the ESP32 rig
 - Discuss the Display Driver file
 - Demonstrate a simple button program and review code

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL

Repo:
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video37

The Pico MP Display Base Board is available for purchase:
https://www.tindie.com/products/aiy745321/pico-mp-display-board/
This board is for standard Pico, PicoW, and Pico2 USB Boards.

# Contents
This directory contains the files for this video.  

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop   | temp_button_display.py | The demonstration program  |
|           |                      |                            |
| Firmware  |                      |                            |
| -May2025  |                      |                            |
| -MP-LVGL9.3-1.24-ESP32-Generic          |firmware.bin          |   ESP32 firmware  (MP1.24.1 and LVGL 9.3)  |
|           |                      |                                 |
|           |                      |                                 |
| Flash      |                      |                             |
| -2432S028-CYD          |                      |                              |
|           |Driver files          |  |
|           |   display_driver.py          | display setup (edited for CYD) |
|           |   ili9xxx.py  |  ILI9431 driver and others   |
|           |   lv_utils.py  |  LVGL utility   |
|           |   st77xx.py  |  st77xx and base class for displays.  |
|           |   xpt2046.py  |  SPI-based Touch driver.  |
|           |                      |                                                 |
| -ESP32-WROOM-32          |                      |                              |
|           |Driver files          |  |
|           |   display_driver.py          | display setup (edited for ESP32 ).
|           |   ili9xxx.py  |  ILI9431 driver and others   |
|           |   lv_utils.py  |  LVGL utility   |
|           |   st77xx.py  |  st77xx and base class for displays.  |
|           |   xpt2046.py  |  SPI-based Touch driver.  |
|           |                      |                                                 |
