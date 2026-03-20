# README - Video 81

19 March 2026

# Scope
This is video 81 on a SquareLine Studio Tutorial to generate an PlatformIO LVGL embedded solution. In this video, we walk-through a simple LVGL touchscreen build in SquareLine Studio. We describe our development approach and the hardware.  The Test Rig is an ILI9341 Integrated Display and and ESP32 Dev Board. After generating the GUI, we use the PlatformIO IDE to build and deploy the firmware.  The project uses both LVGL 9.2.2 library, the Bodmer's TFT_eSPI 2.5.43 library and the Paul Stoffregen XPT2046 Touchscreen library that are available at GitHub and managed through the PlatformIO (PIO) IDE Manager.

The goal is to keep the process simple and iterative to improve understanding. So we create and deploy the various steps in a live demonstration.

You can fetch the firmware and programs from our GitHub site, and begin using them immediately.  

In this video, We:
 - Describe the PlatformIO approach.
 - Discuss the Test Rig and wiring.
 - Iteratively create and deploy a basic LVGL UI.
 - Create two test GUI screens in SquareLine Studios software.
 - Interface the GUI to the PlatformIO project and show the resulting screens.

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video81

The video Demonstrates:
 - PlatformIO
 - LVGL 9.2.2 Library
 - TFT_eSPI library from Bodmer
 - XPT2046 Touchscreen library from Paul Stoffregen
 - SquareLine Studios Software from SquareLine Kft.

 # Files

 - PlatformIO Files
   - platform.ini
   - sample_ui/ui_events.c - This has the countClicks() function
   - main.cpp (three seperate folders)

 - SquareLine Studio Files
   - Export UI Files (zip)
   - Project (zip)
