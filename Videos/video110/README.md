# README.ms - Video110

09 October 2026

# Scope
This is video 110 on a MicroPython LVGL embedded solution. In today’s video we look at LCD Wizard (a commercial product) that creates Arduino, ESPHome, or MicroPython projects.  In fact, the MicroPython/LVGL code is based on LCD_Bus (last reviewed in Video108).  For this video, the owner bumped my account to Pro license. We built the firmware for an ESP32-S3 N16R8 device and the ST7796 display. But you can easily build the firmware for a different ESP32 variant or model. 

We use the LCD Wizard Designer to create three screens to showcase the capabilities of the tool: A screen with dropdown widget, a screen with a chart widget, and a screen with TextArea and keyboard widgets. We iterate through the design-deploy-edit-redeploy steps common to most projects. 
 
In this video, 
 - Briefly review the LCD Wizard technology.
 - Describe the Test Rig.
 - Demonstrate the LCD Wizard designer by walking step-by-step through three screens.
 - Demonstrate the LCD Wizard export and firmware install to our ESP32-S3 using esptool.
 - Demonstrate the LVGL program showing the three screens.
 - Demonstrate the LCD Wizard designer data binding and (Change Screen) event functions.

Here are various sections:
Designer       7:19
Export/Flash  37:25
Demo-1        40:00
Update design 44:00
Demo-2        49:25
Event Code    50:20

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video110

My LCD Wizard account was upgraded to Pro in order to test and evaluate the service.

# Files

 - Code 
   - The last zip exported.

- Firmware
  - MicroPython with LVGL for ESP32-S3 N16R8