# README.md - video109

03 October 2026

# Scope
This is video 109 on a MicroPython/OpenThread embedded solution. This tutorial should help you deploy your own Thread network using MicroPython.  This project demonstrates an IPv6 Node sending a message to another IPv6 Node to turn on a LED using MicroPython.  We walk you though the steps to deploy firmware, configure the nodes and execute remotely using a WebRepl service.  Additionally, a Generic ESP32-C6-DevKit demonstrates a HTTP service to request a color change on the boards RGB led.  

Note: To get node's IPv6 addresses: avahi-browse -rt _webrepl._tcp | grep address

In this video:
 - We briefly explain OpenThread Terminology
 - We explain the hardware stack which includes the OTBR from Video-107
 - Walk you through the configuration of each component
 - Demonstrate our sender/receiver MicroPython programs that control a LED via a button.
 - Demonstrate Caricardio's MicroPython HTTP service to control a RGB LED.  

The code for this video is available at the GitHub site:https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video109

# Files
- Firmware files for the OTBR are discussed in Video107
- A for Coracardio's file please visit his web site and download the whole rep (its not that big).  The zip contains 
the firmware for ESP32-C6 DevKit (4MB) which has a RGB LED.


 - Firmware with MicroPython 1.29 and OpenThread
   - Firmware for Xiao ESP32-C6 (4MB).  Use the esptool to flash it.
   - Firmware for a generic ESP32-C6-Devkit (16MB) which a;so has a RGB LED. Use the esptool to flash it.

 - Flash
   - sender.py  - Place on Node-1
   - receiver.py - Place on Node-2

```
By the way, you can run either file by doing an import x  (do not include the extension)
for example:
  import sender
  or 
  import receiver

  At the top of each program, the code prints its IPv6 address.
  So you can then replace our IPv6 address with your actual.  In both files only the Node 2 address is needed
```