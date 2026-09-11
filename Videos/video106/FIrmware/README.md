# README - Firmware

# Note

You should only need the firmware.bin, (which can be installed with thonny), but just in case I give you every BIN..
There is an info file that describes the procedure:

that describes flashing with esptool

 python -m esptool --chip esp32h2 -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size 4MB --flash_freq 48m 0x0 build-ESP32_GENERIC_H2/bootloader/bootloader.bin 0x8000 build-ESP32_GENERIC_H2/partition_table/partition-table.bin 0xd000 build-ESP32_GENERIC_H2/ota_data_initial.bin 0x10000 build-ESP32_GENERIC_H2/micropython.bin

 I pip installed esptool, and cd to the directory with the files, then I only need to do:
 esptool --chip esp32h2 -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size 4MB --flash_freq 48m 0x0 bootloader.bin 0x8000 partition-table.bin 0xd000 ota_data_initial.bin 0x10000 micropython.bin

 You can also reduce speed to 230400 (which is still fast).
