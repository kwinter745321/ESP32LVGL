# README - Video 75

05 February 2026
06 February 2026 -  See Note below if your LCD will not display properly


# Scope
This is video 75 on a MicroPython/LVGL embedded solution. In this video, we look at the Waveshare device and find a simple way to setup the I2S audio to play sounds.  We are using a firmware built for ESP32-Generic-S3 N16R8 USB boards (which includes this device).  We demonstrate a simple audio test LVGL program.  In this video we focus on just getting the audio to play sounds.

One can modify the test program and change the Sample Rate of the audio file.  To change or add music files one can modify a small array called "songs" at the beginning.

You can fetch the firmware and programs from the GitHub, and begin using them immediately.  

In this video, 
 - Demonstrate the MicroPython audio program.
 - Present our research on the audio components of the Waveshare device.
 - Present our research on the MicroPython I2S function.
 - Discuss the driver changes and how to convert MP3s to WAV file.

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/ESP32LVGL/tree/main/Videos/video73

# Files

- Desktop

  - test_audio_display.py

- Firmware

  - firmware.bin (created in December 2025 for standard ESP32-S3 N16R8 usb module)

- Datasheets

  - several datasheets pertinent to the components

- Flash

  - Various middleware and hardware driver files

  Note: One viewer had trouble getting his LCD to reset.  If this happens to you then please use the display_driver.py found in FixedFlash of Video 73.

- Music

  - snippets oi the 7th Life MP3 file.  Sample Rate 44100  Mono 16-bit