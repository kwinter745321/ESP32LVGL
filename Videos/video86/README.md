# README.md - Video86

22 April 2026

# Scope
This is video 86 on a MicroPython/LVGL embedded solution. ILI9488 is a 320*480 pixel display. In this video, we demonstrate our improved ILI9488 display driver.  We explain how we fixed the driver and switched to a faster RGB565 Conversion routine. 

We use two Test Rigs: a) our Pico2W device and b) an ESP32-S3 device. Even so, we tested the ILI9488 driver for 16 bit ILI9488 displays (which works for all Pico devices and the ESP32-S3.)  You can fetch the firmware and programs from our GitHub site, and begin using them immediately.  Most of our displays have XPT2046 touchscreens (so we demonstrate the touch functions for it.)

In this video, 
    • We demonstrate our working ILI9488 driver (16bit) and the improved ILI9488b (18bit)
    • We discuss the two Test Rigs and wiring
    • We explain how we fixed the RGB565 Conversion routine (and made it faster)
    • We briefly explain Viper

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video86 or
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video86

# Files

- Desktop

- Flash

- ESP32-DisplayDriver

- Firmware
  - Pico2W

  - ESP32-S3
  