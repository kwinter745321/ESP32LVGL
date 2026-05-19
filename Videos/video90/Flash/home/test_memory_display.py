# show_memory.py
#
# Created: 14 May 2026
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.28.0-dirty on 2026-05-08; 
# Generic ESP32S3 module with Octal-SPIRAM with ESP32S3
# LVGL 9.5
# 
import sys
sys.path.append("/home/lib")
import proc
proc=None

import lvgl as lv
from machine import reset, Pin
from display_driver import disp, touch
import time
import gc
import micropython
import machine

lv.init()

bl = Pin(17, Pin.OUT)
bl.on()

tim = machine.Timer(1)

###############################################
# UI
###############################################

# current screen
scr = lv.obj()

blue=lv.palette_main(lv.PALETTE.BLUE)
yellow=lv.palette_main(lv.PALETTE.YELLOW)
green=lv.palette_main(lv.PALETTE.GREEN)
orange=lv.palette_main(lv.PALETTE.ORANGE)
black=lv.color_black()
white=lv.color_white()

scr.set_style_bg_color(white,lv.PART.MAIN)
scr.set_style_border_width(2, lv.PART.MAIN)
scr.set_style_border_color(blue,lv.PART.MAIN)

tot="0"
alc="0"
fre="0"
pct="0"
stk="0"
dt=""

#### Button ##################
btn = lv.button(scr)
btn.set_size(140,40)
btn.set_pos(80,3)
btn.set_style_bg_color(green,lv.PART.MAIN )
btn.set_style_bg_color(orange,lv.PART.MAIN | lv.STATE.PRESSED)

lbl = lv.label(btn)
lbl.set_text("Memory")
lbl.center()
lbl.set_style_text_color(black, lv.PART.MAIN)
lbl.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN)

dropstyle = lv.style_t()
dropstyle.init()
dropstyle.set_drop_shadow_opa(lv.OPA._50)
dropstyle.set_drop_shadow_color(lv.palette_main(lv.PALETTE.GREY))
dropstyle.set_drop_shadow_radius(8)
dropstyle.set_drop_shadow_offset_x(4)
dropstyle.set_drop_shadow_offset_y(8)

def place_lbl(name, row):
    lbl = lv.label(scr)
    lbl.set_pos(3,row)
    lbl.set_text(name)
    lbl.set_style_text_color(black, lv.PART.MAIN)
    lbl.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN)

def place_val(row):
    lbl = lv.label(scr)
    lbl.set_pos(100,row)
    lbl.set_style_text_color(blue, lv.PART.MAIN)
    lbl.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN)
    lbl.add_style(dropstyle, lv.PART.MAIN )
    return lbl

def place_dat():
    lbl = lv.label(scr)
    lbl.set_pos(3, 210)
    lbl.set_style_text_color(green, lv.PART.MAIN)
    lbl.set_style_text_font(lv.font_montserrat_14, lv.PART.MAIN)
    return lbl

place_lbl("Total",60)
place_lbl("Alloc",90)
place_lbl("Free",120)
place_lbl("Stack",150)

totlbl = place_val(60)
alclbl = place_val(90)
frelbl = place_val(120)
stklbl = place_val(150)
datlbl = place_dat()

def place_val(value,row):
    global dt
    tim = f"{dt[3]:02d}:{dt[4]:02d}:{dt[5]:02d}"
    datlbl.set_text(tim)
    if row == 60:
        totlbl.set_text(value)
    if row == 90:
        alclbl.set_text(value)
    if row == 120:
        frelbl.set_text(value)
    if row == 150:
       stklbl.set_text(value)

### free  ###################
def free(event):
    calc_free()
    
def calc_free():
    global tot,alc,fre,stk,dt
    dt = time.localtime()
    gc.collect()
    f = gc.mem_free()
    a = gc.mem_alloc()
    t = f + a
    s = micropython.stack_use()
    tot = f"{t/(1024*1024):.2f} M"
    alc = f"{a/1024:.2f} K"
    fre = f"{f/(1024*1024):.2f} M  ({f/t*100:.2f} %)"
    stk = f"{s/1024:.2f} K"
    # #ret = {"Total": t, "Alloc": a, "Free": f, "%": f"{f/t*100:.2f}%", "Stack": s}
    place_val(tot,60)
    place_val(alc,90)
    place_val(fre,120)
    place_val(stk,150)
    

btn.add_event_cb(free, lv.EVENT.CLICKED, None)
calc_free()
###################################################
lv.screen_load(scr)

# Configure the timer to trigger every 60,000 ms (60 seconds)
tim.init(mode=machine.Timer.PERIODIC, period=30000, callback=free)

def __main__(args):     # Entry point and command line arguments
    try: 
        while True:          # Main loop (for, while, etc)
            #if proc.sts=="S":break  # Mechanism to stop the process if it is launched in batch (&)
            if proc.sts=="H":       # Mechanism to hold and resume the process if it is launched in batch (&) and held
                time.sleep(1)
                continue
            if proc.sts=="S":
                print("Program stopped.")
                break
            lv.timer_handler()
            time.sleep_ms(10)
    except:
        print("Exception")
        scr.clean()

    finally:
        tim.deinit()
        print("Timer stopped.")
        scr.clean()
        bl.off()
        print("Program end.")

