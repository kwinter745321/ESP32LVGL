# test_network.py
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
import machine
import time

lan = network.LAN(
    mdc=machine.Pin(31),
    mdio=machine.Pin(52),
    phy_type=network.PHY_IP101,
    phy_addr=1,
    #ref_clk=machine.Pin(50),
    #ref_clk_mode=machine.Pin.OUT
)

lan.active(True)                      # activate the interface
print("Activate Ethernet")
time.sleep(2)
addr = lan.ipconfig('addr4')                 # get the interface's IPv4 addresses
print("Ethernet IP Address:",addr)