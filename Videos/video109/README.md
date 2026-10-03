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

