# README - Video 69

30 December 2025

# Scope
This is video 69 on a MicroPython embedded solution. In this video, we discuss the ESP32-P4 support in the latest MicroPython firmware.  We are using the standard firmware from micropython.org.  We discuss and demonstrate three features: Ethernet, Wifi, and GPIO configured for ILI9341/XPT2046 Display graphics and touchscreen.  

You can fetch the firmware and programs from the GitHub, and begin using them immediately.  

In this video, 
    - Demonstrate micropython network features and generic ILI9341 graphics.
    - Present the Waveshare ESP32-P4-Module-DEV-KIT board.
    - Present the firmware and Test Rig wiring.
    - Walk through the program code.

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video69

# Files

 - Desktop
    - test_network.py
    - test_wifi.py
    - Graphics
        - demo_color_palette.py
        - demo_clear.py
        - demo_fonts_rotated.py
        - demo_touch.py

 - Firmware
    ESP32_GENERIC_P4-C6_WIFI-20251209-v1.27.0.bin

 - Flash
    - fonts
    - images
    - ili9341.py
    - secret.py  (edit me)
    - xglcd_font.py
    - xpt2046.py

- Graphics
    - zip file from rdagger's GitHub
# Graphics

Obtain an up to date copy of rdagger's repository by visiting his github: https://github.com/rdagger/micropython-ili9341
