# menu.py
#
# Created: 28 June 2026
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.28.0-dirty on 2026-06-28;
# Generic ESP32S3 module with Octal-SPIRAM with ESP32S3

import lvgl as lv
from machine import reset, Pin
from display_driver import disp, touch
import machine
import time
import sys
import select

lv.init()

import time
from machine import Pin, I2C, SoftI2C
from qmi8658 import QMI8658
i2c = SoftI2C(scl=Pin(10), sda=Pin(11), freq=400000)

try:
    imu = QMI8658(i2c)
    #print("QMI8658 initialized successfully!")
except RuntimeError as e:
    print(e)

###############################################
# UI
###############################################

# Globals
current_list = []
start_x = 0
start_y = 0

# current screen
scr = lv.obj()
lv.screen_load(scr)
scr.set_style_bg_color(lv.color_hex(0x0),lv.PART.MAIN)

blue = lv.palette_main(lv.PALETTE.BLUE)
ltblue = lv.color_hex(0x1e90ff)
dkblue = lv.color_hex(0x0000e6)
red = lv.palette_main(lv.PALETTE.RED)
green = lv.color_hex(0x00ff99)
gold = lv.palette_main(lv.PALETTE.YELLOW)
orange = lv.color_hex(0xffa500)
grey = lv.color_hex(0xd3d3d3)
ltgrey = lv.color_hex(0xe3e3e3)
black  = lv.color_black()
white = lv.color_white()

bubble_colors = [white, blue, red, green, gold, grey]

cont_ver_style = lv.style_t()
cont_ver_style.init()
cont_ver_style.set_bg_opa(lv.OPA.COVER)
cont_ver_style.set_bg_grad_dir(lv.GRAD_DIR.VER) 
cont_ver_style.set_bg_color(grey)  
cont_ver_style.set_bg_grad_color(ltgrey) 

btn_ver_style = lv.style_t()
btn_ver_style.init()
btn_ver_style.set_bg_opa(lv.OPA.COVER)
btn_ver_style.set_bg_grad_dir(lv.GRAD_DIR.VER) 
btn_ver_style.set_bg_color(dkblue)  
btn_ver_style.set_bg_grad_color(blue) 

btn_hor_style = lv.style_t()
btn_hor_style.init()
btn_hor_style.set_bg_opa(lv.OPA.COVER)
btn_hor_style.set_bg_grad_dir(lv.GRAD_DIR.HOR) 
btn_hor_style.set_bg_color(dkblue) 
btn_hor_style.set_bg_grad_color(blue) 

btn_lhor_style = lv.style_t()
btn_lhor_style.init()
btn_lhor_style.set_bg_opa(lv.OPA.COVER)
btn_lhor_style.set_bg_grad_dir(lv.GRAD_DIR.HOR) 
btn_lhor_style.set_bg_color(blue) 
btn_lhor_style.set_bg_grad_color(dkblue)

btn_pressed_style = lv.style_t()
btn_pressed_style.init()
btn_pressed_style.set_bg_opa(lv.OPA.COVER)
#btn_pressed_style.set_bg_grad_dir(lv.GRAD_DIR.HOR) 
btn_pressed_style.set_bg_color(orange) 
#btn_pressed_style.set_bg_grad_color(blue)

page = 0
max_page = 1

def left_cb(event):
    global page
    page -= 1 # type: ignore
    if page < 0:
        page = 0
    #print("page is now: {}".format(page))
    show_page(page)

def right_cb(event):
    global page
    page += 1
    if page > max_page: # type: ignore
        page = max_page
    #print("page is now: {}".format(page))
    show_page(page)

profile = {}

with open('profile.txt', 'r') as file:
    content = file.read()

profile = eval(content)
        
max_page = max(profile, default=1)
#print("Max pages in profile: {}".format(max_page))

# --- Modernized Styling Definitions ---
# Colors
bg_color = lv.color_hex(0x1A1A24)       # Dark premium purple-grey background
card_color = lv.color_hex(0x282836)     # Slightly lighter for containers
accent_color = lv.color_hex(0x6A5ACD)   # Modern Lavender/Accent
text_light = lv.color_hex(0xFFFFFF)     # White text
text_dim = lv.color_hex(0xA0A0B5)       # Muted text

# Radius
rad_card = 16                           # for card-like container edges

# Main Screen
cont_main = lv.obj(scr)
cont_main.set_size(240, 280)
cont_main.set_style_bg_color(black, 0)
cont_main.center()
cont_main.set_flex_flow(lv.FLEX_FLOW.ROW_WRAP)
cont_main.set_flex_align(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START)
cont_main.set_style_pad_all(8, 0)
cont_main.set_style_border_width(0, lv.PART.MAIN)
cont_main.remove_flag(lv.obj.FLAG.SCROLLABLE)

# --- Top Container (cont1) ---
cont1 = lv.obj(cont_main)
cont1.set_size(lv.pct(100), lv.pct(20))
cont1.set_style_bg_color(card_color, 0)
cont1.set_style_opa(lv.OPA._100, 0)
cont1.set_style_radius(rad_card, 0)
cont1.set_style_pad_hor(12, 0)
cont1.set_style_border_width(0, lv.PART.MAIN) # Removed harsh border
cont1.set_flex_flow(lv.FLEX_FLOW.ROW)
cont1.set_flex_align(lv.FLEX_ALIGN.SPACE_BETWEEN, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)
cont1.remove_flag(lv.obj.FLAG.SCROLLABLE)

lbl_cont1 = lv.label(cont1)
lbl_cont1.set_text("")
lbl_cont1.set_style_text_color(text_light, 0)
lbl_cont1.set_style_text_font(lv.font_montserrat_24, 0) # Slightly smaller, cleaner font

# Modern Flat LED
led1_cont1 = lv.led(cont1)
led1_cont1.set_size(16, 16)
led1_cont1.set_color(lv.color_hex(0x00FF99)) # Modern green/teal
led1_cont1.set_brightness(255)

# --- Bottom Container (cont2) ---
cont2 = lv.obj(cont_main)
cont2.set_size(lv.pct(100), lv.pct(75)) # slightly reduced to account for gaps
cont2.set_style_bg_color(black, 0) # transparent to let main bg show
cont2.set_style_opa(lv.OPA._90, 0)
cont2.set_flex_flow(lv.FLEX_FLOW.ROW)
cont2.set_flex_align(lv.FLEX_ALIGN.SPACE_BETWEEN, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)
cont2.set_style_pad_all(0, 0)
cont2.set_style_border_width(0, lv.PART.MAIN)
cont2.remove_flag(lv.obj.FLAG.SCROLLABLE)

# --- Navigation Buttons ---
# Left Button
left = lv.button(cont2)
left.set_size(lv.pct(22), lv.pct(100))
left.set_style_bg_color(card_color, lv.STATE.DEFAULT)
left.set_style_bg_color(accent_color, lv.STATE.PRESSED) # Highlight accent on press
left.set_style_radius(rad_card, 0)
left.set_style_border_width(0, lv.PART.MAIN)
left_lbl = lv.label(left)
left_lbl.center()
left_lbl.set_text(lv.SYMBOL.LEFT)
left_lbl.set_style_text_color(text_light, 0)
left_lbl.set_style_text_font(lv.font_montserrat_24, 0)
left.add_event_cb(left_cb, lv.EVENT.CLICKED, None)

# Middle Content Area (Card)
mid = lv.obj(cont2)
mid.set_style_bg_color(card_color, 0)
mid.set_style_radius(rad_card, 0)
mid.set_style_border_width(0, lv.PART.MAIN)
mid.set_size(lv.pct(51), lv.pct(100))
mid.set_flex_flow(lv.FLEX_FLOW.ROW_WRAP)
mid.set_flex_align(lv.FLEX_ALIGN.START,lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START)
mid.remove_flag(lv.obj.FLAG.SCROLLABLE)

# Right Button
right = lv.button(cont2)
right.set_size(lv.pct(22), lv.pct(100))
right.set_style_bg_color(card_color, lv.STATE.DEFAULT)
right.set_style_bg_color(accent_color, lv.STATE.PRESSED) # Highlight accent on press
right.set_style_radius(rad_card, 0)
right.set_style_border_width(0, lv.PART.MAIN)
right_lbl = lv.label(right)
right_lbl.center()
right_lbl.set_text(lv.SYMBOL.RIGHT)
right_lbl.set_style_text_color(text_light, 0)
right_lbl.set_style_text_font(lv.font_montserrat_24, 0)
right.add_event_cb(right_cb, lv.EVENT.CLICKED, None)


def receive_time(data):
    rtc = machine.RTC()
    if data.startswith("TIME"):
        try:
            #print("trying...",data)
            # Extract the numbers: "TIME Y,M,D,W,H,M,S,SS"
            parts = data.split(" ")[1].split(",")
            dt = tuple(int(x) for x in parts)
            print(dt)
            # Set the RTC: (year, month, day, weekday, hours, minutes, seconds, subseconds)
            rtc.init(dt)
            print("RTC successfully synchronized!")
        except Exception as e:
            print("Error setting time:", e)

def gyro():
    acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z = imu.read_xyz()
    print(f"Accel: X:{acc_x: .2f}g, Y:{acc_y: .2f}g, Z:{acc_z: .2f}g")
    print(f"Gyro:  X:{gyro_x: .2f}°/s, Y:{gyro_y: .2f}°/s, Z:{gyro_z: .2f}°/s")
    print("-" * 40)

def btn_cb(event):
    global start_x, start_y
    code = event.get_code()
    if code == lv.EVENT.CLICKED:
        btn = event.get_target_obj()
        lbl = btn.get_child(0)
        txt = lbl.get_text()
        print(txt)
        if txt == "Red":
            led1_cont1.set_color(red)
            sys.stdout.write("LED is now ON\n")
        if txt == "Green":
            led1_cont1.set_color(green)
        if txt == "exit":
            sys.exit()
        if txt == "time":
            current_time = time.localtime()
            year, month, mday, hour, minute, second, weekday, yearday = current_time # type: ignore
            print(f"ESP32S3 Time: {year:04d}-{month:02d}-{mday:02d} {hour:02d}:{minute:02d}:{second:02d}")
        if txt == "gyro":
            gyro()
    if code == lv.EVENT.RELEASED:
            # forces scroll list back to start
            mid.scroll_to(start_x, start_y, 0)
            
def show_page(page):
    global current_list, start_x, start_y
    # Get menu items
    current_list = profile.get(page)
    # clear 'card'
    if mid.get_child_count() > 0:
        mid.clean()
    # First item is the menu Title
    lbl_cont1.set_text(current_list[0] if current_list else "Empty")
    # Allow scrolling if more than three (title makes it 4) menu items
    if len(current_list) > 4:
        mid.add_flag(lv.obj.FLAG.SCROLLABLE)
    else:
        mid.remove_flag(lv.obj.FLAG.SCROLLABLE)
    # Place buttons in 'card'
    for i in range(1,len(current_list)):
        btn = lv.button(mid)
        btn.set_size(lv.pct(100), 58)
        # make scrolled menu items round
        if len(current_list) > 4:
            btn.set_size(55, 55)
            # start of scroll region
            if i == 1:
                start_x = btn.get_x()
                start_y = btn.get_y()
            btn.set_style_bg_color(bubble_colors[i],0)
            btn.set_style_opa(lv.OPA.COVER, 0)
            btn.set_style_radius(55,0)
            mid.set_style_width(30, lv.PART.SCROLLBAR)
        else:
            btn.add_style(btn_ver_style, lv.PART.MAIN | lv.STATE.DEFAULT)
        btn.add_style(btn_pressed_style, lv.PART.MAIN | lv.STATE.PRESSED)
        # Write menu item inside the button
        label = lv.label(btn)
        txt = current_list[i] if current_list else ""
        label.set_text(f"{txt}")
        label.set_style_text_font(lv.font_montserrat_24,0)
        label.set_style_text_color(gold,0)
        label.center()
        # Attach a callback to any button press
        btn.add_event_cb(btn_cb, lv.EVENT.ALL, None)

show_page(page)

###################################################
lv.screen_load(scr)

if __name__ == "__main__":
    # Run the event loop
    print("Running independent of Desktop.")
else:
    # Run the event loop
    while True:
        lv.timer_handler()
        time.sleep_ms(10)
        if select.select([sys.stdin], [], [], 0.1)[0]:
            line = sys.stdin.readline().strip()
            print("\nPC sent:{}".format(line))
            if line.startswith("TIME"):
                receive_time(line)
