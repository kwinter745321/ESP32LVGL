# README - video 58

08 October 2025  (late 08 October 2025 update see below)

# Scope

This video discusses the LCD_BUS firmware. Our display_driver was developed for MicroPython 1.24 LVGL 9.2.2. And the maintainer modified the RGB driver module in the source. In this video, we show the simple update to fix the display_driver. Since that is easy; we also show how to update to the latest firmware.

In this video, 
 - Demonstrate the display_driver’s issue and update it
 - Discuss the different firmware building approachs
 - Explain the driver components needed for the Waveshare display
 - Show how to Build the latest firmware using docker

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video58

# Files

Desktop

 - The two test demonstration programs
 - Dockerfile
 - instructions to install the pre-requisite software

Firmware

 - The BIN file (use Thonny or the esptool to deploy this file to your esp32-s3 module)
 - partitions.csv   (provided by the build)
 - info-build-firmware.txt    (information to help you flash the bin file)

 Flash

 - various driver files
     - ch422g.py
     - display_driver.py      (fixed version of the display_driver)
     - sdcard_driver.py        in case you want to use the sd card (see the test_button2_lcdbus.py program as an example)
 - font           a directory of font files

 # Late Update - 08 October 2025

 A viewer (donpapa871) suggested that we build the firmware with the RGB and ch422g drivers.
 So we did.  Here is the command:

python3 make.py esp32 BOARD=ESP32_GENERIC_S3 BOARD_VARIANT=SPIRAM_OCT DISPLAY=ili9341 DISPLAY=rgb_display DISPLAY=st7796 EXPANDER=ch422g INDEV=gt911 INDEV=xpt2046 clean

We include this file in the firmware_alternate folder.

Thanks donpapa871 !
