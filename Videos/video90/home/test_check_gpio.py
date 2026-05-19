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

import utls
import sdata

def check():
    print("check.py")
    gpio=sdata.board["gpio"][0]
    g=utls.getgpio(5)
    g=utls.getgpios("i2c", 0)
    print(g)

def __main__(args):     # Entry point and command line arguments
    try: 
        check()
        while True:          # Main loop (for, while, etc)
            if proc.sts=="H":       # Mechanism to hold and resume the process if it is launched in batch (&) and held
                time.sleep(1)
                continue
            if proc.sts=="S":
                print("Program Stopped.")
                break
            lv.timer_handler()
            time.sleep_ms(10)
    except:
        print("Exception")
    finally:
        print("Program end.")