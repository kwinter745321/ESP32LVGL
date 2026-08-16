# README.md - video 102

15 August 2026

# Scope
This is video 102 on a MicroPython LVGL embedded solution. In today’s video we create a fun program that uses ESP-NOW.  Our Test Rigs are two ESP32-S3 N16R8 USB boards with a medium-size 320 by 480 pixel TFT touch displays.  This is a complete project; you will be able to transmit and receives message between a pair of devices. We put the single program on both devices, and configure them via touch buttons. The program has two LVGL screen pages.  Although just a few LVGL widgets, we do cover multiple types of LVGL objects and their interactions.
 
In this video, 
 - Demonstrate the chat_display.py program on two Test Rigs and their interactions.
 - Briefly review the ESP-NOW capabilities in MicroPython.
 - Describe the wiring of the Touch, Display, and the ESP32-S3 device.
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
 
# Abstract

# Project Overview
A two-way ESP-NOW chat application built with MicroPython and LVGL running on two ESP32-S3 boards equipped with 320×480 touch LCDs. The same codebase runs on both devices, with settings configured via touch UI.

# Key UI & Features
- Chat Page: Send/receive messages with color-coded responses (yellow = received, white = sent). Includes CLEAR and SEND buttons.
  - Smart Word Suggestions: Received words are parsed, added to an internal list, and sorted by frequency. Users can tap suggested words to quickly compose messages.
- Settings Page: Displays device name, MAC address, and communication rate. 
  - Editable via LVGL Text Areas + on-screen keyboard.
  - Swap Button: Easily reverses peer settings between the two devices, with a confirmation step (SAVE/RESET).

# ESP-NOW Protocol Details

- Connectionless, fast protocol using only 2 OSI layers.
- Limits: Max 20 registered peers, only 6 pairs support encryption, v1 message size capped at 250 bytes (v2 coming in future MicroPython).
- Each transmission returns the sender's MAC address and message payload.
# Setup & Implementation

- Initialize WLAN station mode (then leave it idle).
- Instantiate ESPNow object.
- Register a peer by converting its hex MAC address to a 6-byte array (bytes.fromhex()).
- Send/receive messages directly via the ESPNow object.
- MAC addresses can be obtained via esptool flash-id or printed at runtime.
# Hardware & Wiring

Displays: One uses ST7796, the other ILI9488 (18-bit → 16-bit conversion for LVGL; ILI9488 shows sharper graphics/shading).
ESP-NOW is handled internally by the ESP32, requiring no extra wiring. Only display/touch pins need connection.
# Conclusion
The project serves as a foundational, fully functional ESP-NOW communication demo with a polished LVGL interface. It's designed to be easily expanded for multi-peer use or additional features. Viewers are encouraged to subscribe and adapt the code for their own embedded projects.