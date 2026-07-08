# README.md - Video96

08 July 2026

# Scope
This is video 96 on a MicroPython embedded solution. We show an ESP32-C3 Development board with a 0.49inch OLED.  The ESP32-C3 chip is a single core RISC-V module with 4MB that includes WIFI and Bluetooth 5 (LE). Online retailers have $3-$10 development boards; our Test Rig module uses the chip with an in-built OLED and LED. The ESP32-C3 is very capable. We show this by using both the OLED and the WIFI simultaneously.  

Our WIFI test program uses MicroDot web server software deployed on the board.  The whole unit is small and can be used in small projects that have minimal GPIO needs.  We provide a recent firmware that also includes the LVGL library. You can fetch the firmware file and test programs from our ESP32LVGL GitHub site. 

In this video, 
 - Look at the ESP32-C3 development board with a built-in OLED and LED.
 - Demonstrate our modified copy of Miguel Grinberg's GPIO example MicroDot program.
 - Review the OLED features and briefly discuss MicroDot software.
 - Demonstrate test of the several test programs we built.

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video96

# Files

 - Firmware
   - firmware.bin file for an ESP32-C3 built on 06 May 2026

 - Desktop
   - test_mdot_ssd1306.py  - First demo using MicroDot
   - test_simple_ssd1306.py  Second demo just showing some simple OLED commands
   - test_charset_ssd1306.py -   Third demo showing each of the text characters across 3 screen pages
   - Other -  Other helpful test prgrams

 - Flash
    - various driver files.  Load these driver files onto the virtual flash drive of the ESP32
    