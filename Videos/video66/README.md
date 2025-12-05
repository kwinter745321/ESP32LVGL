# README.md - Video 66

04 December 2025
05 Dec 2025 - Included the firmware I used in the video.

# Scope
This is video 66 on embedded solutions. In this video, we learn to improve our LVGL widgets. We start with one of our simple test programs and enhance its widgets with images and styles. The result is a colorful display that is also functional.  Our Test Rig is an ESP32-S3-N16R8 USB Board wired to an integrated ILI9341 display and xpt2046 touchscreen.

You can fetch the programs from the Github, and begin using them immediately. 

In this video, 
 - Demonstrate our test program and the enhanced version.
 - Discuss our research approach and code snippet.
 - Discuss the Test Rig wiring.
 - Walk through the test code.

As mentioned, the code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video66

Background music is 7th Life by Adam MacDougall which is You Tube Licensed as not requiring an attribution.

Some images used in this video and code were freely obtained at www.freepik.com

# Files

 - Desktop

    - test_slider_display.py            - Our test slider program
    - test_slider2_display.py           - The enhanced version

 - Firmware
    - firmware.bin                      - firmware: MicroPython v1.20.0-2510.gacfeb7b7e.dirty on 2025-11-23; Generic ESP32S3 module with ESP32S3
    - info-esp32-20250517.txt           - Information generated during build


 - Flash

    - display_driver.py             - Edit this for different display type or pin definitions
    - ili9xxx.py                    - ILI9xxx display type classes
    - lv_utils.py                   - a LVGL utility
    - st77xx.py                     - ST77xx display type classes
    - widget.py                     - Three classes to enhance a screen of LVGL widgets
    - xpt2046.py                    - XPT2046 touchscreen driver

    Images
    - Arrow.png                     - Red arrow shape (32x32 pixels)
    - Button48.pbg                  - Custom button "Right"  (48x48 pixels)
    - Button48L.png                 - Custom button "Left"  (48x48 pixels)
 