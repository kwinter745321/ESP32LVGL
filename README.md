# ESP32LVGL
Repository for ESP32 Projects

MicroPython LVGL for ESP32 and variants

This GitHub Repository (Repo) provides MicroPython LVGL 9.x information regarding the ESP32. Here I have collected datasheets, firmware and programs for each YouTube video.

The firmware are files that result from the build of "micropython_lv". Although several output files are generated, the most useful is the "firmware.bin" file. 

One can load their ESP32 board, by using ESPtool or by an IDE that utilizes esptool. For firmware developed using Kevin Schlosser's LVGL Binding, I include an information text file that provides the esptool deployment instruction. I found that Thonny has an integrated feature to deploy the bin that only requires you to specify the COM Port and the filename.
