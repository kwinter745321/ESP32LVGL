# README.md - Video 56

26 September 2025

# Topic

This is video 56 on building the ESP32 firmware with MicroPython/LVGL using Docker.  We verify the firmware build by flashing it to an ESP32-S3 USB board. We describe the approach.  Then we show the steps that Docker takes to build the development environment. Finally we start a Docker container and interactively perform the build.

In this video, 
 - Demonstrate flashing the firmware
 - Discuss the source kits
 - Review the build approach
 - Walk through the build

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video56


# Files

 - Firmware

    - firmware.bin - The MicroPython/LVGL firmware for an ESP32-S3 Octal (8MB PSRAM) device.

 - Desktop

    - Dockerfile - Source for the Docker build. 