# README - Video 88

08 May 2026

# Scope
This is video 88 on a MicroPython/LVGL embedded solution. In this video, we demonstrate two features from LVGL 9.5 on MicroPython 1.28.0.  We built a new set ESP32-S3 firmware; our normal and support for OTA.

We use a Test Rigs: with an ILI9488 display or you can use ILI9341 (the code shrinks the objects if you use ILI9341.)  You can fetch the firmware and programs from our GitHub site, and begin using them immediately.  

In this video, 
 - We demonstrate our working ILI9488 display for two LVGL9.5 features
 - We discuss the Drop Shadow and Blur styles
 - We discuss the two Test Rigs and wiring
 - We explain the two firmware

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video88

# Files

- Desktop
  - test_button3_display.py
  - test_sdrop_display.py - Program shown in demo
  - test_ota_exists.py

- Flash
  - The usual driver files
    - display_driver.py  - Edit this one to switch displays
    - ili9xxx.py
    - lv_utils.py
    - st77xx.py
    - xpt2046.py

  - To support the Large Font file - If you do not use then comment the import fs_driver
    - fs_driver.py                  
    - montserrat-med-48-2.bin

- Firmware
  - ESP32-S3-N16R8 - This has about 13MB storage area for your drivers, etc.

  - ESP32-S3-N16R8-OTA  - This has about 5MB storage area for your drivers, etc.

# display_driver.py

We left the driver configured for ILI9341 Display.  Over time we have collected multiple ILI9341 displays.  These tend to have different touch positions sent by XPT2046 for "similar".  Whereas the ILI9488 has a consistent touch response regardless of the display.    We left the ILI9341 Transform as is, but you may need to adjust it.

# How we flashed the "OTA" firmware
python -m esptool --chip esp32s3 -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size 16MB --flash_freq 80m 0x0 bootloader.bin 0x8000 partition-table.bin 0xd000 ota_data_initial.bin 0x10000 micropython.bin