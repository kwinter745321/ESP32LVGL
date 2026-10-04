# sender.py
#
# Created: 01 October 2026
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# MicroPython ff4121d889-dirty on 2026-10-01esp32c6-10bda3fffe9d9098
# Seeed XIAO ESP32C6 with ESP32-C6
#
import machine
import time
import socket
import asyncio

import openthread

#### Print Node Information #####################
print(openthread.state())
print(openthread.ipaddr())

#### GLOBAL VARIABLES (EDIT THIS SECTION) ##############

# You must replace with your IP Address for node-2
#TARGET_IPV6_ADDR = "<YOUR_TARGET_MAC_ADDRESS>"
TARGET_IPV6_ADDR = "fd79:1ce0:8577:1:1ad0:fe08:5c71:be4b"
TARGET_PORT = 5000
BUTTON_PIN = 21 
LED_PIN_TO_SHOW_STATUS = 22  
SOCKET_TIMEOUT_SECONDS = 10
print(f"[MCU1] Initializing Button Controller...")
print(f"[MCU1] Target Address: {TARGET_IPV6_ADDR}:{TARGET_PORT}")

#### Setup #########################################################
button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
status_led = machine.Pin(LED_PIN_TO_SHOW_STATUS, machine.Pin.OUT, value=0)

loop = asyncio.get_event_loop()
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sock.settimeout(SOCKET_TIMEOUT_SECONDS)
status_led_value = 0

def print_status(msg):
    print(f"[MCU1] {msg}")

#### MAIN LOGIC ###################################################

async def main_task():
    print_status("Network Socket Ready. Listening for button...")

    while True:
        current_time = time.ticks_ms()
        # Using PULL_UP, 0 means Pressed, 1 means Released
        if button.value() == 0: 
            print_status("Button Pressed!")
            if status_led:
                status_led.value(1)
            payload = b"LIGHT_REQUEST" 
            
            # Send UDP Packet
            try:
                sock.sendto(payload, (TARGET_IPV6_ADDR, TARGET_PORT))
                print_status(f"Packet sent to {TARGET_IPV6_ADDR}")
                
            except Exception as e:
                print(f"[MCU1] ERROR: {e}")
            finally:
                if status_led:
                    status_led.value(0)
                    
        # Debounce 
        time.sleep(0.5) 

    # Note: The loop never exits, so MCU1 stays alive

asyncio.run(main_task())
