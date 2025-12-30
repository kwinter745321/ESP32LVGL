# test_wifi.py
#
# Updated: 24 December 2025
#
# License: MIT
#
# https://docs.micropython.org/en/latest/esp32/quickref.html#networking
#
# verified: MicroPython v1.27.0 on 2025-12-09;
#   Generic ESP32P4 module with WIFI module
#   of external ESP32C6 with ESP32P4
#
import network
import secret  # Edit and load to flash drive
import time

wlan = network.WLAN()       # create station interface (the default, see below for an access point interface)
wlan.active(True)           # activate the interface
print("Activate Wifi")
time.sleep(2)
wlan.scan()                 # scan for access points
wlan.isconnected()          # check if the station is connected to an AP
wlan.connect(secret.secretssid, secret.secretpwd) # connect to an AP
print("Wifi connected")
mac = wlan.config('mac')          # get the interface's MAC address
addr = wlan.ipconfig('addr4')      # get the interface's IPv4 addresses
print("WiFI address:",addr)
