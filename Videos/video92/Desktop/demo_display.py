# demo.py
#
import lvgl as lv
from machine import reset, Pin
from display_driver import disp, touch
#
backlight = Pin(17, Pin.OUT)
backlight.on()

import esp32
mydata = esp32.mcu_temperature()

scr = lv.screen_active()
scr.set_style_bg_color(lv.color_black(), lv.PART.MAIN)
scr.set_style_text_font(lv.font_montserrat_24,lv.PART.MAIN)

btn = lv.button(scr)
btn.set_pos(20, 10)
btn.set_style_bg_color(lv.palette_main(lv.PALETTE.BLUE), lv.PART.MAIN)
btnlbl = lv.label(btn)
btnlbl.set_text("Get Temperature")
btnlbl.set_style_text_color(lv.color_black(), lv.PART.MAIN)
btnlbl.center()

ta = lv.textarea(scr)
ta.set_pos(20, 70)
ta.set_size(150, 50)
ta.set_style_text_color(lv.color_black(), lv.PART.MAIN)

def btn_cp(event):
    content = str(esp32.mcu_temperature())+" °C"
    ta.set_text(content)

btn.add_event_cb(btn_cp, lv.EVENT.CLICKED, None)



