# chat2_display.py
#
# Created: 10 August 2026
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.28.0-dirty on 2026-06-28;
# Generic ESP32S3 module with Octal-SPIRAM with ESP32S3
# LVGL 9.5

import lvgl as lv
from machine import reset, Pin
from display_driver import disp, touch
from micropython import const
from collections import OrderedDict
import gc
import network
import espnow
import asyncio
import time

# globals
init_my_name =   "Peer00"
init_my_mac =    "dcb4d914532c"
init_peer_name = "Peer01"
init_peer_mac =  "dcb4d91445e0"
init_send_list = ["hello","help", "repeat", "test"]

# ==========================
# Theme
# ==========================
class Theme:
    DARK = 0
    LIGHT = 1

    def __init__(self, mode=None):
        if mode == None:
            self.mode = self.DARK
        else:
            self.mode = mode
        self._apply()

    def _apply(self):
        if self.mode == self.DARK:
            self.bg = lv.color_black()
            self.panel = lv.color_hex(0x353D47)  # dark cloudy
            self.shadow = lv.color_hex(0xffffff)
            self.primary = lv.color_hex(0x467FE5) # blue
            self.text = lv.color_white()
            self.text2 = lv.color_black()
            self.btn = lv.color_hex(0x46E54F)     # Green
            self.btn2 = lv.color_hex(0xFAA18F)   # red ED54F46
            self.border = lv.color_hex(0x467FE5)  # blue
        else:
            self.bg = lv.color_hex(0xF5F5F5)
            self.panel = lv.color_hex(0xEEEEEE)
            self.shadow = lv.color_hex(0xDDDDDD)
            self.primary = lv.color_hex(0x1976D2)
            self.text = lv.color_black()
            self.text2 = lv.color_hex(0x404040)
            self.btn = lv.color_hex(0xDDDDDD)
            self.btn2 = lv.color_hex(0xFF5252)
            self.border = lv.color_hex(0x000000)

    @staticmethod
    def style_text(obj, color, font, align=lv.TEXT_ALIGN.LEFT):
        obj.set_style_text_color(color, 0)
        obj.set_style_text_font(font, 0)
        obj.set_style_text_align(align, 0)

# ==========================
# ESP-NOW manager
# ==========================
class ESPNowManager:
    def __init__(self, app):
        self.sta_if = None
        self.edge = None
        self.app = app
        self.my_mac = None
        self.peer_mac = None
        self.peer_bytes = None
        self.peer_added = False
        self.sending = False
        self.comm_rate = "0"

    def flush(self):
        while self.edge.any():
            self.edge.recv(0)

    def setup(self):
        self.sta_if = network.WLAN(network.WLAN.IF_STA)
        self.sta_if.active(True)
        self.my_mac = self.sta_if.config('mac').hex()
        self.edge = espnow.ESPNow()
        self.edge.active(True)
        gc.collect()
        print(f"My MAC is: [{self.my_mac}] Bytes:{bytes.fromhex(self.my_mac)}")
        print(25*'#')

    def set_peer_bytes(self, mac_hex):
        self.peer_bytes = bytes.fromhex(mac_hex)
        print(f"Set Peer Bytes:  MAC:{mac_hex} Bytes:{self.peer_bytes}")

    def get_comm_rate(self):
        return self.comm_rate

    def set_comm_rate(self, comm_rate):
        self.comm_rate = comm_rate
        print(f"This peer's send communication rate: {comm_rate}")

    def send_message(self, text, send_list_ref):
        self.set_peer_bytes(self.app.peer_mac)
        print(f"send_message: text:{text}")
        if self.edge == None:
            self.setup()
            print("Edge Setup")
        if self.peer_added == False:
            print(f"Adding Peer at {self.peer_bytes}")
            self.edge.add_peer(self.peer_bytes)
            self.peer_added = True
        cleaned = text.replace(",", " ")
        words = cleaned.split()
        for w in words:
            send_list_ref.append(w)
        self.flush()
        self.edge.config(rate=int(self.comm_rate))
        print(f"Text:{text}")
        print(f"Current: Me:{self.app.my_name} MAC:{self.app.my_mac} Bytes:{bytes.fromhex(self.app.my_mac)}")
        print(f"       - Peer:{self.app.peer_name} MAC:{self.app.peer_mac} Bytes:{self.peer_bytes}")
        print(f"       - Rate:{self.app.comm_rate}")
        try:
            self.sending = True
            for char in text:
                self.edge.send(self.peer_bytes, str(char))
            self.edge.send(self.peer_bytes, b'\n')
            
            self.app._page_instance.update_response(text, self.app.my_name)
        except:
            print("Peer not connected.") #OSError: (-12393, 'ESP_ERR_ESPNOW_NOT_FOUND')
        # debounce
        time.sleep_ms(300)
        self.sending = False

# ==========================
# Pages UI
# ==========================
class ChatPage:
    def __init__(self, parent, theme, app):
        self.parent = parent
        self.theme = theme
        self.app = app
        self.container = None
        self.entry = None
        self.resp = None
        self.keybd = None
        self.helper = None
        self.send_btn = None
        self.clear_btn = None
        self._build()
        self._bind_events()
        self._update_shortlist()

    def _build(self):
        self.container = lv.obj(self.parent)
        self.container.set_size(lv.pct(100), lv.pct(100))
        self.container.set_style_bg_color(self.theme.bg, lv.PART.MAIN)
        self.container.set_flex_flow(lv.FLEX_FLOW.ROW_WRAP)
        self.container.set_flex_align(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START)
        self.container.set_style_border_color(self.theme.border, 0)
        self.container.set_style_border_width(2, 0)
        self.container.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
        self.container.remove_flag(lv.obj.FLAG.SCROLLABLE)

        # Title
        title = lv.label(self.container)
        title.set_size(lv.pct(86), 32)
        title.set_text(f"{self.app.my_name} -> {self.app.peer_name}")
        Theme.style_text(title, self.theme.text, lv.font_montserrat_24, lv.TEXT_ALIGN.CENTER)
        title.set_style_bg_color(self.theme.panel, 0)
        title.set_align(lv.ALIGN.TOP_MID)

        self.settings_btn = lv.button(self.container)
        self.settings_btn.set_size(lv.pct(10), 32)
        self.settings_btn.set_align(lv.ALIGN.TOP_RIGHT)
        self.settings_btn.set_style_bg_color(self.theme.bg, 0)
        self.settings_btn_lbl = lv.label(self.settings_btn)
        self.settings_btn_lbl.set_text(lv.SYMBOL.BARS)
        self.settings_btn_lbl.set_style_text_color(self.theme.text, 0)
        self.settings_btn_lbl.set_style_text_font(lv.font_montserrat_24, 0)
        self.settings_btn_lbl.center()

        # Response Box
        resp_box = lv.obj(self.container)
        resp_box.set_size(lv.pct(98), lv.pct(30))
        resp_box.set_style_bg_color(self.theme.bg, lv.PART.MAIN)
        resp_box.set_style_border_color(self.theme.border, 0)
        

        self.resp = lv.label(resp_box)
        self.resp.set_long_mode(lv.label.LONG_MODE.SCROLL)
        self.resp.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        self.resp.set_text("initial")
        self.resp.set_recolor(True) # permits inline color text
        Theme.style_text(self.resp, self.theme.text, lv.font_montserrat_16)

        # Input
        self.entry = lv.textarea(self.container)
        self.entry.set_style_bg_color(self.theme.shadow, lv.PART.MAIN)
        self.entry.set_style_border_color(self.theme.border, 0)
        self.entry.set_size(lv.pct(70), 80)
        self.entry.set_text("tester")
        Theme.style_text(self.entry, self.theme.text2, lv.font_montserrat_16)

        # Buttons
        btn_box = lv.obj(self.container)
        btn_box.set_size(lv.pct(25), 80)
        btn_box.set_style_bg_color(self.theme.bg, lv.PART.MAIN)
        btn_box.set_flex_flow(lv.FLEX_FLOW.COLUMN)
        btn_box.set_flex_align(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START)
        btn_box.set_style_pad_all(0, 0)
        btn_box.set_style_border_width(0, 0)
        btn_box.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
        btn_box.remove_flag(lv.obj.FLAG.SCROLLABLE)

        self.send_btn = lv.button(btn_box)
        self.send_btn.set_size(lv.pct(100), 35)
        self.send_btn.set_style_text_color(lv.color_black(), 0)
        self.send_btn.set_style_text_font(lv.font_montserrat_16, 0)
        lbl = lv.label(self.send_btn)
        lbl.set_text("SEND")
        lbl.center()

        self.clear_btn = lv.button(btn_box)
        self.clear_btn.set_style_bg_color(self.theme.btn2, 0)
        self.clear_btn.set_size(lv.pct(100), 35)
        self.clear_btn.set_style_text_color(lv.color_black(), 0)
        self.clear_btn.set_style_text_font(lv.font_montserrat_16, 0)
        lbl = lv.label(self.clear_btn)
        lbl.set_text("CLEAR")
        lbl.center()

        # Keyboard
        self.keybd = lv.keyboard(self.container)
        self.keybd.set_style_bg_color(lv.color_black(), 0)
        #self.keybd.set_x(-10)
        self.keybd.set_width(lv.pct(100))
        self.keybd.set_height(lv.pct(40))
        self.keybd.set_style_pad_all(0, 0)
        self.keybd.align(lv.ALIGN.BOTTOM_MID, 0, 0)
        self.keybd.set_textarea(self.entry)

        # Helper/Shortlist
        self.helper = lv.obj(self.container)
        self.helper.set_size(lv.pct(98), lv.pct(40))
        self.helper.set_style_bg_color(self.theme.bg, lv.PART.MAIN)
        self.helper.set_flex_flow(lv.FLEX_FLOW.ROW_WRAP)
        self.helper.set_flex_align(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START)
        self.helper.add_flag(lv.obj.FLAG.HIDDEN)

    def update_response(self,text,me):
        if self.theme.mode == Theme.DARK:
            newtext = "#ffff00 " + me + ": " + text +"#\n"
        else:
            newtext = "#ff0000 " + me + ": " + text +"#\n"
        self.resp.ins_text(0,newtext)

    def _bind_events(self):
        self.settings_btn.add_event_cb(self._settings_btn_cb, lv.EVENT.CLICKED, None)
        self.entry.add_event_cb(self._ta_event_cb, lv.EVENT.ALL, None)
        self.keybd.add_event_cb(self._kb_event_cb, lv.EVENT.ALL, None)
        self.send_btn.add_event_cb(self._send_cb, lv.EVENT.CLICKED, None)
        self.clear_btn.add_event_cb(self._clear_cb, lv.EVENT.CLICKED, None)

    def _settings_btn_cb(self, event):
        #print("Goto Page")
        self.app.navigate_to("settings")

    def _ta_event_cb(self, e):
        code = e.get_code()
        if code == lv.EVENT.CLICKED:
            lv.group_focus_obj(self.entry)
            self.keybd.set_textarea(self.entry)
            self.keybd.remove_flag(lv.obj.FLAG.HIDDEN)
        elif code == lv.EVENT.DEFOCUSED:
            self.keybd.add_flag(lv.obj.FLAG.HIDDEN)

    def _kb_event_cb(self, e):
        if e.get_code() in (lv.EVENT.READY, lv.EVENT.CANCEL):
            self.keybd.add_flag(lv.obj.FLAG.HIDDEN)

    def _send_cb(self, e):
        text = self.entry.get_text()
        if not text.strip():
            return
        self.app.espnow.send_message(text, self.app.send_list)
        self._update_shortlist()

    def _clear_cb(self, e):
        self.entry.set_text("")

    def _update_shortlist(self):
        if self.helper:
            self.helper.clean()
        unique_words = list(OrderedDict.fromkeys(sorted(self.app.send_list)))
        for word in unique_words:
            btn = lv.button(self.helper)
            btn.set_style_bg_color(self.theme.shadow, 0)
            lbl = lv.label(btn)
            lbl.set_text(word.strip())
            lbl.set_style_text_color(self.theme.text2, 0)
            # Capture current `word` in closure to avoid late binding issues
            btn.add_event_cb(lambda e, w=word: self._append_word(w), lv.EVENT.CLICKED, None)

    def _append_word(self, word):
        current = self.entry.get_text()
        self.entry.set_text(f"{current} {word}".strip())


class SettingsPage:
    def __init__(self, parent, theme, app):
        self.parent = parent
        self.theme = theme
        self.app = app
        self.container = None
        self.my_entry = None
        self.my_mac_lbl = None
        self.peer_entry = None
        self.peer_mac_entry = None
        self.rate_val_lbl = None
        self.dropdown = None
        self.keybd = None
        self.orig_color = None
        #self._build()
        self.clear_settings()
        self._bind_events()
        

    def clear_settings(self):
        self.my_name = self.app.my_name
        self.my_mac = self.app.my_mac
        self.peer_name = self.app.peer_name
        self.peer_mac = self.app.peer_mac
        self.comm_rate = self.app.comm_rate
        if self.container != None:
            self.container.clean()
        self._build()
        self._bind_events()

    def _build(self):
        self.container = lv.obj(self.parent)
        self.container.set_size(lv.pct(100), lv.pct(100))
        self.container.set_style_bg_color(self.theme.bg, lv.PART.MAIN)
        self.container.set_flex_flow(lv.FLEX_FLOW.ROW_WRAP)
        self.container.set_flex_align(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START)
        self.container.set_style_border_color(self.theme.border, 0)
        self.container.set_style_border_width(1, 0)
        self.container.set_style_pad_all(0, 0)
        self.container.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
        self.container.remove_flag(lv.obj.FLAG.SCROLLABLE)

        # Title
        title = lv.label(self.container)
        title.set_size(lv.pct(86), lv.SIZE_CONTENT)
        title.set_text("Settings")
        Theme.style_text(title, self.theme.text, lv.font_montserrat_24, lv.TEXT_ALIGN.CENTER)
        title.set_style_bg_color(self.theme.panel, 0)
        title.set_align(lv.ALIGN.CENTER)

        self.chat_btn = lv.button(self.container )
        self.chat_btn.set_size(lv.pct(10), 32)
        self.chat_btn.set_align(lv.ALIGN.TOP_RIGHT)
        self.chat_btn.set_style_bg_color(self.theme.bg, 0)
        self.chat_btn_lbl = lv.label(self.chat_btn)
        self.chat_btn_lbl.set_text(lv.SYMBOL.BARS)
        self.chat_btn_lbl.set_style_text_color(self.theme.text, 0)
        self.chat_btn_lbl.set_style_text_font(lv.font_montserrat_24, 0)
        self.chat_btn_lbl.center()

        # My Name
        lbl = lv.label(self.container)
        lbl.set_size(lv.pct(15), lv.SIZE_CONTENT)
        lbl.set_text("Me:")
        Theme.style_text(lbl, self.theme.text, lv.font_montserrat_16, lv.TEXT_ALIGN.CENTER)
        lbl.set_style_bg_color(self.theme.panel, 0)
        lbl.set_align(lv.ALIGN.CENTER)

        self.my_entry = lv.textarea(self.container)
        self._setup_textarea(self.my_entry, self.my_name)
        self.my_entry.set_align(lv.ALIGN.CENTER)

        # My MAC
        self.my_mac_lbl = lv.label(self.container)
        self.my_mac_lbl.set_size(lv.pct(47), 40)
        self.my_mac_lbl.set_text(self.my_mac)
        Theme.style_text(self.my_mac_lbl, self.theme.text2, lv.font_montserrat_16, lv.TEXT_ALIGN.CENTER)
        self.my_mac_lbl.set_style_bg_color(self.theme.shadow, 0)
        self.my_mac_lbl.set_style_bg_opa(lv.OPA.COVER, 0)
        self.my_mac_lbl.set_align(lv.ALIGN.CENTER)

        # Peer Name
        lbl = lv.label(self.container)
        lbl.set_size(lv.pct(15), lv.SIZE_CONTENT)
        lbl.set_text("Peer:")
        Theme.style_text(lbl, self.theme.text, lv.font_montserrat_16, lv.TEXT_ALIGN.CENTER)
        lbl.set_style_bg_color(self.theme.panel, 0)
        lbl.set_align(lv.ALIGN.CENTER)

        self.peer_entry = lv.textarea(self.container)
        self._setup_textarea(self.peer_entry, self.peer_name)
        self.peer_entry.set_align(lv.ALIGN.CENTER)

        # Peer MAC
        self.peer_mac_entry = lv.textarea(self.container)
        self._setup_textarea(self.peer_mac_entry, self.peer_mac)
        self.peer_mac_entry.set_size(lv.pct(47),40)
        self.peer_mac_entry.set_align(lv.ALIGN.CENTER)

        # Rate
        lbl = lv.label(self.container)
        lbl.set_size(lv.pct(15), lv.SIZE_CONTENT)
        lbl.set_text("Rate:")
        Theme.style_text(lbl, self.theme.text, lv.font_montserrat_16, lv.TEXT_ALIGN.CENTER)
        lbl.set_style_bg_color(self.theme.panel, 0)

        self.rate_val_lbl = lv.label(self.container)
        self.rate_val_lbl.set_size(lv.pct(28), 40)
        self.rate_val_lbl.set_text(self.comm_rate)
        Theme.style_text(self.rate_val_lbl, self.theme.text2, lv.font_montserrat_16, lv.TEXT_ALIGN.CENTER)
        self.rate_val_lbl.set_style_bg_color(self.theme.shadow, 0)
        self.rate_val_lbl.set_style_bg_opa(lv.OPA.COVER, 0)
        self.rate_val_lbl.set_align(lv.ALIGN.CENTER)

        # Dropdown
        options = ["RATE_1M", "RATE_2M", "RATE_4M", "RATE_5M", "RATE_11M", "RATE_54M"]
        self.dropdown = lv.dropdown(self.container)
        self.dropdown.set_size(120, 40)
        self.dropdown.align_to(lbl, lv.ALIGN.OUT_RIGHT_MID, 0, 0)
        self.dropdown.set_options("\n".join(options))

        dummy1_lbl = lv.label(self.container)
        dummy1_lbl.set_size(lv.pct(15), 32)

        # Swap Button
        self.chg_btn = lv.button(self.container)
        self.chg_btn.set_size(lv.pct(68), 30)
        self.chg_btn.set_style_bg_color(self.theme.btn2, 0)
        self.chg_btn.set_style_text_color(lv.color_black(), 0)
        self.chg_btn.set_style_text_font(lv.font_montserrat_16, 0)
        
        lbl = lv.label(self.chg_btn)
        lbl.set_text("SWAP PEERS")
        lbl.center()
        lbl.add_event_cb(self._swap_cb, lv.EVENT.CLICKED, None)

        # Bottom Buttons
        btn_box = lv.obj(self.container)
        btn_box.set_size(lv.pct(98), 45)
        btn_box.set_flex_flow(lv.FLEX_FLOW.ROW)
        btn_box.set_flex_align(lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)
        btn_box.set_style_bg_color(self.theme.bg, 0)
        btn_box.set_style_border_color(self.theme.bg, 0)
        btn_box.set_style_border_width(1, 0)
        btn_box.set_style_pad_all(0, 0)
        btn_box.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
        btn_box.remove_flag(lv.obj.FLAG.SCROLLABLE)

        self.save_btn = lv.button(btn_box)
        self.save_btn.set_size(lv.pct(45), 45)
        self.save_btn.set_style_text_color(lv.color_black(), 0)
        self.save_btn.set_style_text_font(lv.font_montserrat_16, 0)
        lbl = lv.label(self.save_btn)
        lbl.set_text("SAVE")
        lbl.center()
        lbl.add_event_cb(self._save_cb, lv.EVENT.CLICKED, None)
        if self.orig_color == None:
            self.orig_color = self.save_btn.get_style_bg_color(0)
        

        self.reset_btn = lv.button(btn_box)
        self.reset_btn.set_style_bg_color(self.theme.btn2, 0)
        self.reset_btn.set_style_text_color(lv.color_black(), 0)
        self.reset_btn.set_style_text_font(lv.font_montserrat_16, 0)
        self.reset_btn.set_size(lv.pct(45), 45)
        lbl = lv.label(self.reset_btn)
        lbl.set_text("RESET")
        lbl.center()
        lbl.add_event_cb(self._reset_cb, lv.EVENT.CLICKED, None)

        # Keyboard
        self.keybd = lv.keyboard(self.container)
        self.keybd.set_style_bg_color(lv.color_black(), 0)
        self.keybd.set_x(5)
        self.keybd.set_width(lv.pct(98))
        self.keybd.set_height(lv.pct(39))
        self.keybd.set_style_pad_all(1, 0)
        self.keybd.align(lv.ALIGN.BOTTOM_MID, 0, 0)
        self.keybd.set_textarea(self.my_entry)

        self.my_entry.add_event_cb(self._entry_focus_cb, lv.EVENT.ALL, None)
        self.peer_entry.add_event_cb(self._entry_focus_cb, lv.EVENT.ALL, None)
        self.peer_mac_entry.add_event_cb(self._entry_focus_cb, lv.EVENT.ALL, None)

    def _setup_textarea(self, ta, text):
        ta.set_style_bg_color(self.theme.shadow, lv.PART.MAIN)
        ta.set_style_border_color(self.theme.border, 0)
        ta.set_size(lv.pct(28), 40)
        ta.set_text(text)
        Theme.style_text(ta, self.theme.text2, lv.font_montserrat_16)

    def _chat_btn_cb(self, event):
        #print("Goto Chat Page")
        self.app.navigate_to("chat")

    def _bind_events(self):
        self.dropdown.add_event_cb(self._dropdown_cb, lv.EVENT.VALUE_CHANGED, None)
        self.chat_btn.add_event_cb(self._chat_btn_cb, lv.EVENT.CLICKED, None)
        self.chg_btn.add_event_cb(self._swap_cb, lv.EVENT.CLICKED, None)
        self.save_btn.add_event_cb(self._save_cb, lv.EVENT.CLICKED, None)
        self.reset_btn.add_event_cb(self._reset_cb, lv.EVENT.CLICKED, None)

    def _entry_focus_cb(self, e):
        code = e.get_code()
        target = e.get_target_obj()  #kw
        if code == lv.EVENT.CLICKED:
            lv.group_focus_obj(target)
            self.keybd.set_textarea(target)

    def _dropdown_cb(self, e):
        if e.get_code() == lv.EVENT.VALUE_CHANGED:
            sel_buf = bytearray(32)
            self.dropdown.get_selected_str(sel_buf, len(sel_buf))
            selected = sel_buf.decode('utf-8').strip('\x00')
            index = self.dropdown.get_option_index(selected)
            self.dropdown.set_selected(index)
            self.rate_val_lbl.set_text(str(index))
            self.app.espnow.set_comm_rate(str(index))
            self.dropdown.close()

    def _swap_cb(self, e):
        hold_name, hold_mac = self.my_name, self.my_mac
        self.my_name, self.my_mac = self.peer_name, self.peer_mac
        self.peer_name, self.peer_mac = hold_name, hold_mac
        self.my_entry.set_text(self.my_name)
        self.my_mac_lbl.set_text(self.my_mac)
        self.peer_entry.set_text(self.peer_name)
        self.peer_mac_entry.set_text(self.peer_mac)
        self.container.clean()
        self._build()
        self.save_btn.set_style_bg_color(self.theme.btn, 0)
        self._bind_events()
        print(f"Swapped: Me:{self.my_name} Peer:{self.peer_name}")
        # debounce
        time.sleep_ms(300)

    def _save_cb(self, e):
        time.sleep_ms(300)
        self.app.my_name = self.my_entry.get_text()
        self.app.my_mac = self.my_mac_lbl.get_text()
        self.app.peer_name = self.peer_entry.get_text()
        self.app.peer_mac = self.peer_mac_entry.get_text()
        self.app.comm_rate = self.rate_val_lbl.get_text()
        self.save_btn.set_style_bg_color(self.orig_color, 0)
        print(f"Saved: Me:{self.app.my_name} MAC:{self.app.my_mac} Bytes:{bytes.fromhex(self.app.my_mac)}")
        print(f"     - Peer:{self.app.peer_name} MAC:{self.app.peer_mac} Bytes:{bytes.fromhex(self.app.peer_mac)}")
        print(f"     - Rate:{self.app.comm_rate}")
        # debounce
        time.sleep_ms(300)

    def _reset_cb(self, e):
        hold_name = self.my_name
        hold_mac = self.my_mac
        self.my_name = self.peer_name
        self.my_mac = self.peer_mac
        self.peer_name = hold_name
        self.peer_mac = hold_mac
        self.container.clean()
        self._build()
        self.save_btn.set_style_bg_color(self.orig_color, 0)
        #self.save_btn.set_style_bg_color(self.theme.btn, 0)
        self._bind_events()
        self.app.comm_rate = self.app.hold_rate
        self.rate_val_lbl.set_text(self.app.comm_rate)
        print(f"Reset: Me:{self.my_name} MAC:{self.my_mac} Bytes:{bytes.fromhex(self.my_mac)}")
        print(f"     - Peer:{self.peer_name} MAC:{self.peer_mac} Bytes:{bytes.fromhex(self.peer_mac)}")
        print(f"     - Rate:{self.comm_rate}")
        # debounce
        time.sleep_ms(300)

# ==========================
# Application
# ==========================
class App:
    def __init__(self):
        self.theme = Theme()
        self.espnow = None
        self.my_name = init_my_name
        self.my_mac = init_my_mac
        self.peer_name = init_peer_name
        self.peer_mac = init_peer_mac
        self.comm_rate = "0"
        print(f"Init:  Me:{self.my_name} MAC:{self.my_mac} Bytes:{bytes.fromhex(self.my_mac)}")
        print(f"     - Peer:{self.peer_name} MAC:{self.peer_mac} Bytes:{bytes.fromhex(self.peer_mac)}")
        print(f"     - Rate:{self.comm_rate}")
        self.hold_name = self.my_name
        self.hold_mac = self.my_mac
        self.hold_rate = self.comm_rate
        self.send_list = init_send_list
        self.current_page = None
        self.sending = False
        self._page_instance = ChatPage(lv.screen_active(), self.theme, self)
        self.current_page = "chat"
        self._init_espnow()
        self.start()
        

    def _init_espnow(self):
        self.espnow = ESPNowManager(self)
        self.espnow.set_peer_bytes(self.peer_mac)
        self.espnow.setup()

    def navigate_to(self, page_type):
        if self._page_instance:
            self._page_instance.container.clean()
            del self._page_instance
        self.current_page = page_type
        if page_type == "chat":
            self._page_instance = ChatPage(lv.screen_active(), self.theme, self)
        elif page_type == "settings":
            self._page_instance = SettingsPage(lv.screen_active(), self.theme, self)
        self._setup_gestures()

    def start(self):
        self._setup_gestures()
        asyncio.run(self._main_loop())

    def _setup_gestures(self):
        scr = lv.screen_active()
        scr.add_event_cb(self._swipe_cb, lv.EVENT.GESTURE, None)

    def _swipe_cb(self, e):
        indev = lv.indev_active()
        ges_dir = indev.get_gesture_dir()
        # if not ges_dir:
        #     return
        if ges_dir == lv.DIR.TOP:
            #self.navigate_to("chat")
            pass
        elif ges_dir == lv.DIR.LEFT:
            print(f"Gesture Left page:{self.current_page}")
            if self.current_page == "chat":
                self._page_instance.keybd.add_flag(lv.obj.FLAG.HIDDEN)
                self._page_instance.helper.remove_flag(lv.obj.FLAG.HIDDEN)
                print("Removed hidden")
            else:
                self.sending = False
        elif ges_dir == lv.DIR.RIGHT:
            print(f"Gesture Right page:{self.current_page}")
            if self.current_page == "chat":
                self._page_instance.keybd.remove_flag(lv.obj.FLAG.HIDDEN)
                self._page_instance.helper.add_flag(lv.obj.FLAG.HIDDEN)
                self._page_instance.keybd.set_textarea(self._page_instance.entry)
                lv.group_focus_obj(self._page_instance.entry)
            else:
                self.sending = True
        elif ges_dir == lv.DIR.BOTTOM:
            #self.navigate_to("settings")
            pass


    async def _main_loop(self):
        asyncio.create_task(self._reader_task())
        while True:
            await asyncio.sleep_ms(100)

    async def _reader_task(self):
        buf = bytearray(250)
        cnt = 0
        while self.current_page == "settings":
            print(f"setting {self.current_page}")
            await asyncio.sleep_ms(100)
        #### current_page must be "chat" here ####
        # while self.current_page == "chat" and not hasattr(self._page_instance, 'resp'):
        #     await asyncio.sleep_ms(100)
        self._page_instance.resp.set_text("started")
        while True:
            host, msg = self.espnow.edge.recv()
            if msg:
                if msg == b'\n':
                    data = self.espnow.edge.peers_table
                    peer_key, int_list = list(data.items())[0]
                    rssi,tim = int_list 
                    print(f"buf: {buf[:cnt]} cnt:{cnt} from:{peer_key.hex()} rssi:{rssi}")
                    text = buf[:cnt].decode('utf-8').rstrip('\x00')
                    if self.current_page == "chat" and hasattr(self._page_instance, 'resp'):
                        self._page_instance.resp.ins_text(0, text+"\n")
                    # Clear the buf
                    buf[:] = b'\x00' * len(buf)
                    cnt = 0
                    self.sending = False
                else:
                    if cnt < len(buf):
                        buf[cnt] = msg[0]
                        cnt += 1
            gc.collect()
            await asyncio.sleep_ms(100)

# ==========================
# Execute
# ==========================
#if __name__ == "__main__":
done = False
try:
    app = App()
    #app.start()
    #asyncio.run(app._main_loop())
except KeyboardInterrupt:
    print("Program stopped by user.")
