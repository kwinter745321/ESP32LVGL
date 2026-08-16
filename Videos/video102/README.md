# README.md - video 102

15 August 2026

# Scope
This is video 102 on a MicroPython LVGL embedded solution. In today’s video we create a fun program that uses ESP-NOW.  Our Test Rigs are two ESP32-S3 N16R8 USB boards with a medium-size 320 by 480 pixel TFT touch displays.  This is a complete project; you will be able to transmit and receives message between a pair of devices. We put the single program on both devices, and configure them via touch buttons. The program has two LVGL screen pages.  Although just a few LVGL widgets, we do cover multiple types of LVGL objects and their interactions.
 

In this video, 
 - Demonstrate the chat_display.py program on two Test Rigs and their interactions.
 - Briefly review the ESP-NOW capabilities in MicroPython.
 - Describe the wiring of the Touch Displayand the SP32-S3 device.
 - Demonstrate the Settings page and show configuration.


The code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video102

# Files

 - Desktop
   - chat2_display.py

 - Flash_peer00_st7796
   - Various driver files.  The main driver is display_driver, which ere setups up the ST7796.

 - Flash_peer01_ili9488
   - Various driver files.  The main driver is display_driver, which ere setups up the ILI9488.
 
