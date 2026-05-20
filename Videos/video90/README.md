# README - Video 90

20 May 2026

# Scope
This is video 90 on a MicroPython LVGL embedded solution. In this video, we feature upyOS. We wonder if this software can replace REPL. This is a complete Operating System (OS) that resides on an ESP32 microcontroller.  We look at an implementation on our Test Rig which consists of an ESP32-S3 N16R8 USB Dev Board and an ILI9341 Touch Display.

You can fetch the test program from our ESP32LVGL GitHub site. 

In this video, 
 - Look at upyOS.
 - Review our Test Rig and wiring.
 - Discuss the major components of upyOS.
 - Demonstrate command line, the HTTP service, and our GUI test programs.

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video90

# Files

 - Firmware 
   - copy of firmware information from video 88

 - Flash

   - etc 
     - system.conf
     - default.board

   - home
     - lib - with our typical drivers
     - various MicroPython programs

# Caution

During an OTA upgrade the upyOS files overwrite what ever resides in their directories.
Meaning the default.board may be reverted to their original file.  Make a backup of the file
and replace.  Then run "loadboard etc/default.board"