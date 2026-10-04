# receiver.py
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

#### GLOBAL VARIABLES (EDIT THIS SECTION) ##################

# You must replace this with your IPv6 for node-2
#MY_IPV6_ADDR = "<YOUR_LOCAL_MAC_ADDRESS>"
MY_IPV6_ADDR = "fd79:1ce0:8577:1:1ad0:fe08:5c71:be4b"
MY_PORT = 5000
LED_PIN_OUTPUT = 22  
SOCKET_BUFFER_SIZE = 1024
print(f"[MCU2] Initializing LED Controller...")
print(f"[MCU2] Listening on: {MY_IPV6_ADDR}:{MY_PORT}")

#### Setup ####################################################
led = machine.Pin(LED_PIN_OUTPUT, machine.Pin.OUT, value=0)

# Initialize UDP Socket (IPv6) - Listen Mode
# AF_INET6 for IPv6, SOCK_DGRAM for UDP
try:
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    print_status = lambda msg: print(f"[MCU2] {msg}")
    sock.bind((MY_IPV6_ADDR, MY_PORT))
    print_status("Socket Bound and Listening.")

except Exception as e:
    print(f"[MCU2] CRITICAL ERROR: Could not bind socket. Check IPv6 address. Error: {e}")
    
#### MAIN LOGIC ###################################################

async def listen_loop():
    try:
        while True:
            data, addr = sock.recvfrom(SOCKET_BUFFER_SIZE)
            print(f"[MCU2] Received Payload from {addr}: {data}")
            # Decode Data to string 
            try:
                msg_text = data.decode('utf-8')
                if msg_text.strip() == "LIGHT_REQUEST":
                    # Turn on LED
                    led.value(1)
                    print_status("LED ON (Received Signal)")
                    time.sleep(2.0)
                    led.value(0)
                    print_status("LED OFF")
                else:
                    print_status(f"Ignored unknown message: {msg_text}")
            except UnicodeDecodeError:
                print_status("Received binary/non-text data, ignoring.")

    except KeyboardInterrupt:
        print_status("Stopping Controller...")
    except Exception as e:
        print_status(f"Socket Error: {e}")

asyncio.run(listen_loop())
