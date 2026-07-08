# test_wifi_connect2.py
# Updated: 29 March 2026 for txpower=8.5
#
# Verified on ESP32-C3 mini
#
import network
import ntptime
import time
from secrets import ssid, password
import gc

gc.collect()
print("GC free:",gc.mem_free() )
sta_if = None

def do_connect():
    import network
    global sta_if
    sta_if = network.WLAN(network.WLAN.IF_STA)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        # Set Tx power to 8.5 dBm
        sta_if.config(txpower=8.5)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ipconfig('addr4'))
    
do_connect()





