# test_ota_exists.py
# Created: 08 May 2026
# MIT License
#
from esp32 import Partition

# Get the currently running partition
current = Partition(Partition.RUNNING)
print("Running from:", current.info()) 

# Get the target partition for the next update
next_ota = current.get_next_update()
print("Next update target:", next_ota.info())

# WHAT WE GET WHEN WE RUN THIS UTILITY
#MPY: soft reboot
#Running from: (0, 0, 65536, 3145728, 'factory', False)
#Next update target: (0, 16, 3211264, 3145728, 'ota_0', False)

# Confirming a Successful Boot (Validation)
# If your firmware is built with the Rollback feature enabled
# (standard for robust OTA), the system will automatically
# roll back to the previous version on the next reboot unless
# the new partition is explicitly marked as valid. 
# 
# Action: Call mark_app_valid_cancel_rollback() immediately
# after a successful boot to "verify" the partition as functional.
# Safety: If your app crashes before this call, the ESP32-S3
# bootloader will treat it as a failure and revert to the
# last known good state.

############################
### Call this once your app has initialized successfully
#current.mark_app_valid_cancel_rollback()
############################
#import machine
### Set the new partition as the default for next boot
#next_ota.set_boot()
### Restart the device to switch partitions
#machine.reset()

