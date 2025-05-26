# README.md - firmware for ESP32-S3 with 8MB PSRAM


#ESPTOOL Instruction

replace (PORT) with your serial device port.  Like COM5

esptool --chip esp32s3 -p (PORT) -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size 8MB --flash_freq 80m --erase-all 0x0 lvgl_micropy_ESP32_GENERIC_S3-SPIRAM_OCT-8.bin