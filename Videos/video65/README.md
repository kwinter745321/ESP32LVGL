# README - video 65

24 November 2025

# Scope
This is video 65 on embedded solutions. In this video, we discuss the E32R28T device.  The device is similar to the Cheap Yellow Display ("CYD"), as it has an ILI9341 display and xpt2046 touchscreen. However, it is configured differently.  We discuss the E32R28T device and its components.  We discuss in extra detail the firmware deployment as well as the display and touch configuration.  We run several demonstration programs that are colorful and also help us verify the touchscreen functionality.

You can fetch the programs from the Github, and begin using them immediately.  As this The video explains how the various display and touch functions interact with LVGL, a new person or someone seeking more behind the scenes knowledge will get keen insight.

In this video, 
    • Demonstrate severl test programs.
    • Present three display samples and test rig wiring.
    • Discuss the driver update.
    • Walk through the driver code update.

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video65

# Files

 - Desktop

    - test_button_display.py
    - test_slider_display.py
    - test_matrix4_display.py
    - test_chart_display.py

 - Firmware

    - firmware.bin
    - info 

 - Flash

    - display_driver.py         Modifed for this project
    - ili9xxx.py                Classes for certain displays: ILi9341, ST7796, and GC9A01
    - lv_utils.py               A utility
    - st77xx.py                 Holds classes for certain displays: st7735 (and is a base class for ili9xxx)
    - xpt2046.py                A specific touchscreen driver for the xpt2046 hardware

