# README.md - Video 92

03 June 2026

# Scope


# Files

- Desktop
    - vscode - this is the settings we use
    - demo_display.py just simple code to show micropython and lvgl stub actions

- Firmware
    - ESP32-S3_SPIRAM_OCT_N16R8
    - ESP32-S3_SPIRAM_OCT_N32R16

- Flash  
    - display_driver.py  - Edit this one to setup Pins, display type, and touch
    - various driver files

- Stubs
    - lvgl-9x - this folder contains a single text file - modified slight for our fonts
    - ulab - These are old files (hopefully we will find better)


# Deploy Firmware

This firmware was built recently with MicroPython 1.28.0, LVGL 9.5.0, and ulab 6.12.0-2D-c.
The firmware can be flashed using the esptool.  Below is the coomand we used.

N16R8
esptool --chip esp32s3 -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size 16MB --flash_freq 80m 0x0 bootloader.bin 0x8000 partition-table.bin 0xd000 ota_data_initial.bin 0x10000 micropython.bin

N32R16
esptool --chip esp32s3 -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size 32MB --flash_freq 80m 0x0 bootloader.bin 0x8000 partition-table.bin 0xd000 ota_data_initial.bin 0x10000 micropython.bin