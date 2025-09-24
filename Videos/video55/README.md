# README.md - Video55

24 September 2025

# Topic 

This is video 55 on setting up MicroPython setting up LVGL on an ESP32-S3 Octal (8MB PSRAM) USB Board.  We demonstrate two GUI code examples. We discuss the hardware and wiring.  We mount the ESP32-S3-DevKitC-1 USB board on a Base and the ILI9341 display on a breadboard.  The firmware used is the standard MicroPython and LVGL software; built in May 2025.

In this video, 
 - Demonstrate our slider and button examples
 - Present the display and the wiring
 - Discuss the GitHub files
 - Walk through the code

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video55

ILI9341 Display board at Amazon is:  HiLetgo ILI9341 2.8" SPI TFT LCD Display Touch Panel 240X320 with PCB 5V/3.3V STM32

# Files

 - Firmware

    - firmware.bin - The MicroPython/LVGL firmware for an ESP32-S3 Octal (8MB PSRAM) device.

 - Desktop

    - test_button_display.py - Demonstrate single button and callback. 
    - test_slider_display.py - Demonstrate a slider with callback that updates slider value in a label.

 - Flash

    - display_driver.py - Setups up LVGL display and touchscreen.  Edit this file to change the display type. Default is 2.4 inch ILI9341 display.
    - ili9xxx.py        - Driver with ILI9341 and other classes.
    - lv_utils.py       - LVGL utility.
    - st77xx.py         - Base driver for the display classes.
    - xpt2046.py        - Touchscreen XPT2046 Driver.
