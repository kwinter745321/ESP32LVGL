# test_mdot_ssd1306.py
#
# Starts a MicroDot service and displays messages to OLED
#    Open a web browser at http://<your ip>:5000/
#    for example:  http://192.168.68.57:5000/
#    After the slash you can type choices:
#          ip   display ESP32-C3's network IP
#          clear OLED is cleared
#          gpio  Page to manage GPIO pin values
#          on    Turn on ESP32-C3's LED
#          off   Turn off ESP32-C3's LED
#
# Created: 07 July 2025
#
# Contains GPIO example MicroDot code from Miguel Grinberg
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.28.0-dirty on 2026-05-06;
# ESP32C3 module with ESP32C3
# LVGL 9.5
#
import sys
import network
import machine
from machine import Pin,SoftI2C
import time
from secrets import ssid, password
import gc
import ssd1306
from microdot import Microdot, Request, Response, abort, redirect, send_file

# --- GPIO INITIALIZATION ---
for i in range(0,10):
    out=Pin(i, Pin.OUT)
    out.value(0)

for i in range(20,22):
    out=Pin(i, Pin.OUT)
    out.value(0)

# GPIO8 (LED) needs to be inverted
out=Pin(8, Pin.OUT)
out.value(1)

# --- DISPLAY INITIALIZATION ---
i2c = SoftI2C(sda=Pin(5), scl=Pin(6), freq=400000)
oled = ssd1306.SSD1306_I2C(72, 40, i2c)
oled.rotate(0)
oled.fill(0)

# --- GLOBALS ---
message = ""
ip = ""

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
ip_tuple = sta_if.ipconfig('addr4')
ip = ip_tuple[0]

def display():
    global message
    parts = [message[i:i+9] for i in range(0, len(message), 9)]
    row = 0
    oled.fill(0)
    for part in parts:
        oled.text(part, 0, row)
        row += 8
    oled.show()

#############################################
        
# --- WEBSERVER INITIALIZATION  ---
app = Microdot()
app.debug = True
Response.default_content_type = 'text/html'

message = "IP= " + ip
display()

# --- SHOW MESSAGE on OLED ---
@app.after_request
async def after_request(request,e):
    global message
    display()

@app.route('/')
async def index(request):
    global message
    message = 'Hello'
    return message

@app.route('/ip')
async def show_ip(request):
    global message, ip
    message = "IP= " + ip
    return message

@app.route('/clear')
async def clear_display(request):
    global message
    message = ""
    return message

@app.route('/gpio', methods=['GET', 'POST'])
async def show_gpio(request):
    global count, message
    form_cookie = None
    message_cookie = None
    if request.method == 'POST':
        form_cookie = '{pin},{pull}'.format(pin=request.form['pin'],
                                            pull=request.form['pull'])
        if 'read' in request.form:
            pull = None
            if request.form['pull'] == 'pullup':
                pull = machine.Pin.PULL_UP
            elif request.form['pull'] == 'pulldown':
                pull = machine.Pin.PULL_DOWN
            pin = machine.Pin(int(request.form['pin']), machine.Pin.IN, pull)          
            message_cookie = 'Input pin {pin} is {state}.'.format(
                pin=request.form['pin'],
                state='high' if pin.value() else 'low')
            state = 'high' if pin.value() else 'low'
            message = f"Read:{request.form['pin']}   as {state}"
        else:
            pin = machine.Pin(int(request.form['pin']), machine.Pin.OUT)
            value = 0 if 'set-low' in request.form else 1
            
            pin.value(value)
            message_cookie = 'Output pin {pin} is now {state}.'.format(
                pin=request.form['pin'],
                state='high' if value else 'low')
            state = 'high' if value else 'low'
            message = f"Set:{request.form['pin']} to {state}"
        response = redirect('/gpio')
    else:
        if 'message' not in request.cookies:
            message_cookie = 'Select a pin and an operation below.'
        response = send_file('gpio.html')
    if form_cookie:
        response.set_cookie('form', form_cookie)
    if message_cookie:
        response.set_cookie('message', message_cookie)
    return response

@app.route('/on')
async def on(request):
    global message
    message = 'LED on'
    out.value(0)    
    return "Turned Relay On - Power to PC Off"

@app.route('/off')
async def off(request):
    global message
    message = 'LED off'
    out.value(1)    
    return "Turned Relay Off - Power to PC On"


@app.route('/bad')
async def bad(request):
    global message
    message = 'BAD Request'
    return '<h2>Bad Request</h2>', 400




# --- WEBSERVER START  ---
print("Begin app.run using default port 5000")
app.run()