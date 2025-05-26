# temp_humidity_display.py
#
# Updated: 19 May 2025 for MP on ESP32
# Original: https://github.com/fabse-hack/temp_humidity_micropython_lvgl
#
# MIT License
# MicroPython v1.20.0-2504.g9fe842956 on 2025-05-17; Generic ESP32S3 module with Octal-SPIRAM with ESP32S3
# ESP32-S3 with SPIRAM_OCT (N16R8)
# LVGL 9.3  <-------------------------------Note
# 
import lvgl as lv
# import lcd_bus
# import ili9341
from machine import SPI, Pin
import machine
import network
#### used by esp32 ############################################
#from lvgl import task_handler  #used by ESP32
#### exception handling (before any drivers, etc. #############
import lv_utils
event_loop = lv_utils.event_loop()
from machine import reset
###############################################################
#from umqtt.simple import MQTTClient
#import dht
#import asyncio
import uasyncio as asyncio
import utime
import ntptime
#### Using neopixel ############################
import neopixel
################################################
from display_driver import disp, disp_drv, touch
import sys
import gc
import time
import random

secretssid = ""
secretpwd = ""
try:
    from secret import secretssid, secretpwd
except:
    print("If you are missing the secret file, just update line 33-34 instead")

network_retries = 9

###################
print("PyLang", sys.version_info, ";", sys.implementation)

##############################################
# UI
###############################################
reset_button = Pin(45, Pin.IN) 
# current screen
scrn = lv.obj()
# try:
#     from display_driver import HardReset
#     h = HardReset(scrn)
# except ImportError:
#     pass


print("mem:",gc.mem_free() )
gc.collect()
print("mem:",gc.mem_free() )
#### Frame the screen #####################
#scrn.set_style_bg_color(lv.color_hex(0),0)
#scrn.set_style_border_width(2, 0)
#scrn.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),0)

dispp = lv.display_get_default()
#theme = lv.theme_default_init(dispp, lv.palette_main(lv.PALETTE.BLUE), lv.palette_main(lv.PALETTE.RED), True, lv.font_default())
theme = lv.theme_default_init(dispp, lv.palette_main(lv.PALETTE.BLUE), lv.palette_main(lv.PALETTE.RED), True, lv.font_montserrat_14)
dispp.set_theme(theme)

# ################################### temperature chart #####################
ui_TemperatureChart = lv.chart(scrn)
ui_TemperatureChart.set_width(184)
ui_TemperatureChart.set_height(63)
ui_TemperatureChart.set_x(60)
ui_TemperatureChart.set_y(-41)
ui_TemperatureChart.set_align(lv.ALIGN.CENTER)
ui_TemperatureChart.add_flag(lv.obj.FLAG.OVERFLOW_VISIBLE)
ui_TemperatureChart.set_type(lv.chart.TYPE.LINE)

ui_TemperatureChart_Xaxis = lv.scale(ui_TemperatureChart)
ui_TemperatureChart_Xaxis.set_mode(lv.scale.MODE.HORIZONTAL_BOTTOM)
ui_TemperatureChart_Xaxis.set_size(lv.pct(100), 50)
ui_TemperatureChart_Xaxis.set_align(lv.ALIGN.BOTTOM_MID)
ui_TemperatureChart_Xaxis.set_y(50 + ui_TemperatureChart.get_style_pad_bottom(lv.PART.MAIN) + ui_TemperatureChart.get_style_border_width(lv.PART.MAIN))

ui_TemperatureChart_Xaxis.set_total_tick_count(10)
ui_TemperatureChart_Xaxis.set_major_tick_every(2)
ui_TemperatureChart_Xaxis.set_style_line_width(0, lv.PART.MAIN)
ui_TemperatureChart_Xaxis.set_style_line_width(1, lv.PART.ITEMS)
ui_TemperatureChart_Xaxis.set_style_line_width(1, lv.PART.INDICATOR)
ui_TemperatureChart_Xaxis.set_style_length(8, lv.PART.INDICATOR)
ui_TemperatureChart_Xaxis.set_style_length(5, lv.PART.ITEMS)

ui_TemperatureChart_Yaxis1 = lv.scale(ui_TemperatureChart)
ui_TemperatureChart_Yaxis1.set_mode(lv.scale.MODE.VERTICAL_LEFT)
ui_TemperatureChart_Yaxis1.set_size(50, lv.pct(100))
ui_TemperatureChart_Yaxis1.set_align(lv.ALIGN.LEFT_MID)
ui_TemperatureChart_Yaxis1.set_x(-50 - ui_TemperatureChart.get_style_pad_left(lv.PART.MAIN) - ui_TemperatureChart.get_style_border_width(lv.PART.MAIN) + 2)

ui_TemperatureChart_Yaxis1.set_style_line_width(0, lv.PART.MAIN)
ui_TemperatureChart_Yaxis1.set_style_line_width(1, lv.PART.ITEMS)
ui_TemperatureChart_Yaxis1.set_style_line_width(1, lv.PART.INDICATOR)
ui_TemperatureChart_Yaxis1.set_style_length(10, lv.PART.INDICATOR)
ui_TemperatureChart_Yaxis1.set_style_length(5, lv.PART.ITEMS)

ui_TemperatureChart_series_1 = ui_TemperatureChart.add_series(lv.color_hex(0x0CFF00), lv.chart.AXIS.PRIMARY_Y)

ui_TemperatureChart.set_style_outline_pad(max(50, 50, 50), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_TemperatureChart.set_style_outline_width(-1, lv.PART.MAIN | lv.STATE.DEFAULT)

ui_TemperatureChart.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# ################################### temperature chart END ###################
# ################################### humidity chart ##########################

ui_HumidityChart = lv.chart(scrn)
ui_HumidityChart.set_width(184)
ui_HumidityChart.set_height(63)
ui_HumidityChart.set_x(60)
ui_HumidityChart.set_y(60)
ui_HumidityChart.set_align(lv.ALIGN.CENTER)
ui_HumidityChart.add_flag(lv.obj.FLAG.OVERFLOW_VISIBLE)
ui_HumidityChart.set_type(lv.chart.TYPE.LINE)

ui_HumidityChart_Xaxis = lv.scale(ui_HumidityChart)
ui_HumidityChart_Xaxis.set_mode(lv.scale.MODE.HORIZONTAL_BOTTOM)
ui_HumidityChart_Xaxis.set_size(lv.pct(100), 50)
ui_HumidityChart_Xaxis.set_align(lv.ALIGN.BOTTOM_MID)
ui_HumidityChart_Xaxis.set_y(50 + ui_HumidityChart.get_style_pad_bottom(lv.PART.MAIN) + ui_HumidityChart.get_style_border_width(lv.PART.MAIN))
ui_HumidityChart_Xaxis.set_total_tick_count(10)
ui_HumidityChart_Xaxis.set_major_tick_every(2)
ui_HumidityChart_Xaxis.set_style_line_width(0, lv.PART.MAIN)
ui_HumidityChart_Xaxis.set_style_line_width(1, lv.PART.ITEMS)
ui_HumidityChart_Xaxis.set_style_line_width(1, lv.PART.INDICATOR)
ui_HumidityChart_Xaxis.set_style_length(10, lv.PART.INDICATOR)
ui_HumidityChart_Xaxis.set_style_length(5, lv.PART.ITEMS)

ui_HumidityChart_Yaxis1 = lv.scale(ui_HumidityChart)
ui_HumidityChart_Yaxis1.set_mode(lv.scale.MODE.VERTICAL_LEFT)
ui_HumidityChart_Yaxis1.set_size(50, lv.pct(100))
ui_HumidityChart_Yaxis1.set_align(lv.ALIGN.LEFT_MID)

ui_HumidityChart_Yaxis1.set_x(-50 - ui_HumidityChart.get_style_pad_left(lv.PART.MAIN) - ui_HumidityChart.get_style_border_width(lv.PART.MAIN) + 2)

ui_HumidityChart_Yaxis1.set_style_line_width(0, lv.PART.MAIN)
ui_HumidityChart_Yaxis1.set_style_line_width(1, lv.PART.ITEMS)
ui_HumidityChart_Yaxis1.set_style_line_width(1, lv.PART.INDICATOR)
ui_HumidityChart_Yaxis1.set_style_length(10, lv.PART.INDICATOR)
ui_HumidityChart_Yaxis1.set_style_length(5, lv.PART.ITEMS)

ui_HumidityChart_series_1 = ui_HumidityChart.add_series(lv.color_hex(0xFFFF00), lv.chart.AXIS.PRIMARY_Y)

ui_HumidityChart.set_style_outline_pad(max(50, 50, 50), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_HumidityChart.set_style_outline_width(-1, lv.PART.MAIN | lv.STATE.DEFAULT)

ui_HumidityChart.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)

# ################################### humidity chart END ######################
ui_Temperature = lv.label(scrn)
ui_Temperature.set_text("Temperature")
ui_Temperature.set_width(lv.SIZE_CONTENT)
ui_Temperature.set_height(lv.SIZE_CONTENT) 
ui_Temperature.set_x(-99)
ui_Temperature.set_y(2)
ui_Temperature.set_align(lv.ALIGN.CENTER)
ui_Temperature.set_style_text_color(lv.color_hex(0x0CFF00), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_Temperature.set_style_text_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT)

ui_Temp_data = lv.label(scrn)
ui_Temp_data.set_width(lv.SIZE_CONTENT)
ui_Temp_data.set_height(lv.SIZE_CONTENT)
ui_Temp_data.set_x(-102)
ui_Temp_data.set_y(-38)
ui_Temp_data.set_align(lv.ALIGN.CENTER)
ui_Temp_data.set_style_text_color(lv.color_hex(0x0CFF00), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_Temp_data.set_style_text_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT)
ui_Temp_data.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN | lv.STATE.DEFAULT)

ui_Humidity = lv.label(scrn)
ui_Humidity.set_text("Humidity")
ui_Humidity.set_width(lv.SIZE_CONTENT)
ui_Humidity.set_height(lv.SIZE_CONTENT)
ui_Humidity.set_x(-104)
ui_Humidity.set_y(39)
ui_Humidity.set_align(lv.ALIGN.CENTER)
ui_Humidity.set_style_text_color(lv.color_hex(0xFFFF00), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_Humidity.set_style_text_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT)

ui_Humidity_data = lv.label(scrn)
ui_Humidity_data.set_width(lv.SIZE_CONTENT)
ui_Humidity_data.set_height(lv.SIZE_CONTENT)
ui_Humidity_data.set_x(-104)
ui_Humidity_data.set_y(74)
ui_Humidity_data.set_align(lv.ALIGN.CENTER)
ui_Humidity_data.set_style_text_color(lv.color_hex(0xFFFF00), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_Humidity_data.set_style_text_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT)
ui_Humidity_data.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN | lv.STATE.DEFAULT)

ui_Time = lv.label(scrn)
ui_Time.set_width(lv.SIZE_CONTENT)
ui_Time.set_height(lv.SIZE_CONTENT)
ui_Time.set_x(-76)
ui_Time.set_y(-108)
ui_Time.set_align(lv.ALIGN.CENTER)

ui_Wifi = lv.label(scrn)
ui_Wifi.set_text("WiFi:")
ui_Wifi.set_width(lv.SIZE_CONTENT)
ui_Wifi.set_height(lv.SIZE_CONTENT)
ui_Wifi.set_x(-121)
ui_Wifi.set_y(-91)
ui_Wifi.set_align(lv.ALIGN.CENTER)

ui_connected = lv.label(scrn)
ui_connected.set_width(lv.SIZE_CONTENT)
ui_connected.set_height(lv.SIZE_CONTENT)
ui_connected.set_x(-60)
ui_connected.set_y(-91)
ui_connected.set_align(lv.ALIGN.CENTER)

ui_MQTT = lv.label(scrn)
ui_MQTT.set_text("MQTT:")
ui_MQTT.set_width(lv.SIZE_CONTENT)
ui_MQTT.set_height(lv.SIZE_CONTENT)
ui_MQTT.set_x(29)
ui_MQTT.set_y(-107)
ui_MQTT.set_align(lv.ALIGN.CENTER)

ui_enabled = lv.label(scrn)
ui_enabled.set_width(lv.SIZE_CONTENT)
ui_enabled.set_height(lv.SIZE_CONTENT)
ui_enabled.set_x(104)
ui_enabled.set_y(-107)
ui_enabled.set_align(lv.ALIGN.CENTER)

ui_IP_ = lv.label(scrn)
ui_IP_.set_text("IP:")
ui_IP_.set_width(lv.SIZE_CONTENT)
ui_IP_.set_height(lv.SIZE_CONTENT)
ui_IP_.set_x(14)
ui_IP_.set_y(-91)
ui_IP_.set_align(lv.ALIGN.CENTER)

ui_ip_data = lv.label(scrn)
ui_ip_data.set_width(lv.SIZE_CONTENT)
ui_ip_data.set_height(lv.SIZE_CONTENT)
ui_ip_data.set_x(104)
ui_ip_data.set_y(-91)
ui_ip_data.set_align(lv.ALIGN.CENTER)

ui_punkt1 = lv.obj(scrn)
ui_punkt1.set_width(10)
ui_punkt1.set_height(10)
ui_punkt1.set_x(-1)
ui_punkt1.set_y(-107)
ui_punkt1.set_align(lv.ALIGN.CENTER)

ui_punkt2 = lv.obj(scrn)
ui_punkt2.set_width(10)
ui_punkt2.set_height(10)
ui_punkt2.set_x(-1)
ui_punkt2.set_y(-91)
ui_punkt2.set_align(lv.ALIGN.CENTER)

ui_punkt3 = lv.obj(scrn)
ui_punkt3.set_width(10)
ui_punkt3.set_height(10)
ui_punkt3.set_x(-150)
ui_punkt3.set_y(-107)
ui_punkt3.set_align(lv.ALIGN.CENTER)

ui_punkt4 = lv.obj(scrn)
ui_punkt4.set_width(10)
ui_punkt4.set_height(10)
ui_punkt4.set_x(-150)
ui_punkt4.set_y(-91)
ui_punkt4.set_align(lv.ALIGN.CENTER)

ui_frame_status = lv.obj(scrn)
ui_frame_status.set_width(318)
ui_frame_status.set_height(39)
ui_frame_status.set_x(0)
ui_frame_status.set_y(-100)
ui_frame_status.set_align(lv.ALIGN.CENTER)
ui_frame_status.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_frame_status.set_style_bg_opa(5, lv.PART.MAIN| lv.STATE.DEFAULT)

ui_frame_temp = lv.obj(scrn)
ui_frame_temp.set_width(318)
ui_frame_temp.set_height(100)
ui_frame_temp.set_x(0)
ui_frame_temp.set_y(-28)
ui_frame_temp.set_align(lv.ALIGN.CENTER)
ui_frame_temp.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_frame_temp.set_style_bg_opa(5, lv.PART.MAIN| lv.STATE.DEFAULT)

ui_frame_humidity = lv.obj(scrn)
ui_frame_humidity.set_width(318)
ui_frame_humidity.set_height(95)
ui_frame_humidity.set_x(0)
ui_frame_humidity.set_y(71)
ui_frame_humidity.set_align(lv.ALIGN.CENTER)
ui_frame_humidity.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_frame_humidity.set_style_bg_opa(5, lv.PART.MAIN| lv.STATE.DEFAULT)

lv.screen_load(scrn)

print("mem:",gc.mem_free() )
gc.collect()
print("mem:",gc.mem_free() )
##############################################
# UI END
###############################################

class WiFiManager:
    def __init__(self, wifi_ssid, wifi_password, ap_ssid, ap_password):
        self.wifi_ssid = wifi_ssid
        self.wifi_password = wifi_password
        self.ap_ssid = ap_ssid
        self.ap_password = ap_password
        self.ssid = None
        self.ip_address = None
        self.status = None

    def connect_to_wifi(self):
        try:
            wlan = network.WLAN(network.STA_IF)
            wlan.active(True)
            cnt = 0
            if not wlan.isconnected():
                print("Wifi - testing connection")
                wlan.connect(self.wifi_ssid, self.wifi_password)
                while not wlan.isconnected():
                    time.sleep(1)
                    print(".",end="")
                    cnt += 1
                    if cnt > network_retries:
                        raise print("Failed to connect after %d tries." % cnt)
            #print("Wifi - connected with:", self.wifi_ssid)
            print("Wifi - connected with: secretssid")
            self.ssid = self.wifi_ssid
            self.ip_address = wlan.ifconfig()[0]
            print("Wifi - IP-Address:", self.ip_address)
            self.status = "connected"
        except Exception as e:
            print(f"Wifi connection failed with msg: {e}")

    def create_access_point(self):
        try:
            ap = network.WLAN(network.AP_IF)
            ap.active(True)
            ap.config(essid=self.ap_ssid, password=self.ap_password)
            print("Wifi - access point created:")
            print("Wifi - SSID:", self.ap_ssid)
            print("Wifi - Password:", self.ap_password)
            print("Wifi - IP-Address:", ap.ifconfig()[0])
            self.ssid = self.ap_ssid
            self.ip_address = ap.ifconfig()[0]
            self.status = "access point"
        except Exception as e:
            print(f"Wifi Access Point failed to open - msg: {e}")

    def configure_wifi(self):
        try:
            self.connect_to_wifi()
        except Exception as e:
            print(f"Wifi cannot connect - create access point - msg: {e})")
            self.create_access_point()

        return self.ssid, self.ip_address, self.status

class German_time:
    def __init__(self):
        self.hour_list = [0]
        self.stelle_zeit_ein()
        self.aktualisiere_zeit()

    def stelle_zeit_ein(self):
        try:
            print("NTP synchronize time over..")
            ntptime.host = "de.pool.ntp.org"
            ntptime.settime()
            print("NTP time synchronized")
        except Exception as e:
            print(f"NTP Time Server Error with msg: {e})")

    def aktualisiere_zeit(self):
        zeit_utc = utime.localtime()

        # offset = 1 Normalzeit (MEZ)
        offset = -5 # ESD 
        if self.is_summertime(zeit_utc):
            offset += 1

        self.jahr, self.monat, self.tag, self.stunde, self.minute, self.sekunde, _, _ = zeit_utc
        self.stunde = (self.stunde + offset) % 24

    def is_summertime(self, zeit):
        monat, tag = zeit[1], zeit[2]

        if monat > 3 and monat < 10:
            return True
        elif monat == 3:
            return tag >= 8
        elif monat == 10:
            return tag < 25
        return False

    def update_hour_list(self):
        #self.hour_list.append(self.stunde)  #update x-axis by hour
        self.hour_list.append(self.minute)
        if len(self.hour_list) > 8:
            self.hour_list.pop(0)
        return self.hour_list

    def __str__(self):
        return self.zeige_zeit()

    def zeige_zeit(self):
        return f"{self.tag:02d}.{self.monat:02d}.{self.jahr} {self.stunde:02d}:{self.minute:02d}:{self.sekunde:02d}"

    async def tick(self):
        while True:
            self.aktualisiere_zeit()
            zeit = self.zeige_zeit()
            ui_Time.set_text(zeit)
            #lv.task_handler()
            lv.timer_handler()
            await asyncio.sleep(1)

async def update_temperature_list(temp_list, humidity_list):
    d.measure()
    temperature = int(d.temperature())
    humidity = int(d.humidity())
    #temperature = 24
    #humidity = 22
    temperature_int = temperature
    humidity_int = humidity

    temp_list.append(temperature_int)
    if len(temp_list) > 10:
        temp_list.pop(0)

    humidity_list.append(humidity_int)
    if len(humidity_list) > 10:
        humidity_list.pop(0)
        

async def data_to_lvgl_every_hours():

    get_hour = German_time()
    while True:
        get_hour.aktualisiere_zeit()
        await update_temperature_list(temperature_list, humidity_list)
        print("......temperature list:", temperature_list,get_hour)
        print("......humidity list:", humidity_list)

        # ################# temp chart #########################
        range_down_temp = min(temperature_list) - 1
        range_up_temp = max(temperature_list) + 1
        #use this instead if LVGL 9.3+
        ui_TemperatureChart.set_series_ext_y_array(ui_TemperatureChart_series_1, temperature_list)
        #ui_TemperatureChart.set_ext_y_array(ui_TemperatureChart_series_1, temperature_list)

        ui_TemperatureChart_Yaxis1.set_range(range_down_temp, range_up_temp)

        range_span_temp = range_up_temp - range_down_temp
        desired_major_ticks_temp = 3
        major_tick_every_temp = max(1, range_span_temp // (desired_major_ticks_temp - 1))
        total_tick_count_temp = (desired_major_ticks_temp - 1) * major_tick_every_temp + 1

        ui_TemperatureChart_Yaxis1.set_total_tick_count(total_tick_count_temp)
        ui_TemperatureChart_Yaxis1.set_major_tick_every(major_tick_every_temp)

        ui_TemperatureChart.set_axis_range(lv.chart.AXIS.PRIMARY_Y, range_down_temp, range_up_temp)
        ui_TemperatureChart.set_axis_range(lv.chart.AXIS.SECONDARY_Y, range_down_temp, range_up_temp)
        #ui_TemperatureChart.set_range(lv.chart.AXIS.PRIMARY_Y, range_down_temp, range_up_temp)
        #ui_TemperatureChart.set_range(lv.chart.AXIS.SECONDARY_Y, range_down_temp, range_up_temp)

        # ################# temp chart END #####################

        # ################# humidity chart #####################
        range_down_humi = min(humidity_list) - 1
        range_up_humi = max(humidity_list) + 1
        #use this instead if LVGL 9.3+
        ui_HumidityChart.set_series_ext_y_array(ui_HumidityChart_series_1, humidity_list)
        #ui_HumidityChart.set_ext_y_array(ui_HumidityChart_series_1, humidity_list)

        ui_HumidityChart_Yaxis1.set_range(range_down_humi, range_up_humi)

        range_span_humi = range_up_humi - range_down_humi
        desired_major_ticks_humi = 3
        major_tick_every_humi = max(1, range_span_humi // (desired_major_ticks_humi - 1))
        total_tick_count_humi = (desired_major_ticks_humi - 1) * major_tick_every_humi + 1

        ui_HumidityChart_Yaxis1.set_total_tick_count(total_tick_count_humi)
        ui_HumidityChart_Yaxis1.set_major_tick_every(major_tick_every_humi)

        #use this instead if LVGL 9.3+
        ui_HumidityChart.set_axis_range(lv.chart.AXIS.PRIMARY_Y, range_down_humi, range_up_humi)
        ui_HumidityChart.set_axis_range(lv.chart.AXIS.SECONDARY_Y, range_down_humi, range_up_humi)
        #ui_HumidityChart.set_range(lv.chart.AXIS.PRIMARY_Y, range_down_humi, range_up_humi)
        #ui_HumidityChart.set_range(lv.chart.AXIS.SECONDARY_Y, range_down_humi, range_up_humi)

        # ################# humidtiy chart END #################

        hour_list = get_hour.update_hour_list()

        hour_min = hour_list[0]
        hour_max = hour_list[-1]

        ui_HumidityChart_Xaxis.set_range(hour_min, hour_max)
        ui_TemperatureChart_Xaxis.set_range(hour_min, hour_max)

        ui_ip_data.set_text(ip_address)
        ui_connected.set_text(status)
        temperature = d.last_temp   #int(d.temperature())
        ui_Temp_data.set_text(f"{temperature} °C")
        humidity = d.last_humi      #int(d.humidity())
        ui_Humidity_data.set_text(f"{humidity} %")

#         mqtt_publisher = MQTTSensorPublisher(
#                                         broker_address="192.168.178.103",
#                                         port=1883,
#                                         topic="humi_temp",
#                                         username="homeassisant",
#                                         password="dumdidum"
#                                         )
#         await mqtt_publisher.publish_sensor_data(temperature=temperature, humidity=humidity)
        led.fill((0, 0, 50))
        led.write()
        #await asyncio.sleep(1800)
        await asyncio.sleep(30)
        
        led.fill((0, 50, 0))
        led.write()
        #await asyncio.sleep(1800)
        await asyncio.sleep(10)

async def data_to_lvgl_every_second():

    while True:
        ui_punkt1.set_style_bg_color(lv.color_make(255, 0, 0), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_punkt2.set_style_bg_color(lv.color_make(0, 0, 255), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_punkt3.set_style_bg_color(lv.color_make(0, 0, 255), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_punkt4.set_style_bg_color(lv.color_make(255, 0, 0), lv.PART.MAIN | lv.STATE.DEFAULT)
        #lv.task_handler()
        lv.timer_handler()
        await asyncio.sleep(1)
        ui_punkt1.set_style_bg_color(lv.color_make(0, 0, 255), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_punkt2.set_style_bg_color(lv.color_make(255, 0, 0), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_punkt3.set_style_bg_color(lv.color_make(255, 0, 0), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_punkt4.set_style_bg_color(lv.color_make(0, 0, 255), lv.PART.MAIN | lv.STATE.DEFAULT)
        #lv.task_handler()
        lv.timer_handler()
        await asyncio.sleep(1)

def do_closing():
    led.fill((50, 50, 50))
    led.write()
    time.sleep(0.5)
    led.fill((0, 0, 0))
    led.write()
    # could clear the display as well
    event_loop.disable()
    event_loop.deinit()
    reset()
        
async def do_reset():
    # waits for other tasks 
    while True:
        rb = reset_button.value()
        await asyncio.sleep(0.2)
        #rb = reset_button.value()
        if rb == 1:   # slightly diff now: pressed == 1
            print("pressed reset",rb)
            do_closing()
            
async def task_0():
    global event_loop
    await asyncio.sleep(1)
    try:
        print("*",end="")
    except Exception:
        print("Exception task_0.")
        do_closing()
        
async def main():
    task0 = asyncio.create_task(task_0())
    task4 = asyncio.create_task(do_reset())
    task1 = asyncio.create_task(data_to_lvgl_every_hours())
    task2 = asyncio.create_task(data_to_lvgl_every_second())
    mytime = German_time()
    task3 = asyncio.create_task(mytime.tick())
    await asyncio.gather(task1, task2, task4, task0, task3)
    
# class LED:
#     
#     def __init__(self):
#         self.led = [1,2,3]
#         self.led[0] = Pin("LED", Pin.OUT) #GP25
#         self.led[1] = Pin(26, Pin.OUT)
#         self.led[2] = Pin(27, Pin.OUT)
#         for i in range(0,3):
#             self.led[i].on()
#             time.sleep(0.5)
#             self.led[i].off()
#             
#     def turn_off(self):
#         for i in range(0,3):
#             self.led[i].off()
#             
#     def fill(self,setting):
#         l1,l2,l3 = setting
#         self.turn_off()
#         if l1>0: self.led[0].on()
#         if l2>0: self.led[1].on()
#         if l3>0: self.led[2].on()
#         time.sleep(3)
#         self.turn_off()
#         
#     def write(self):
#         pass
    
class simDHT:
    
    def __init__(self,pin):
        self.simulator = True
        self.dht = None
        self.last_temp = 22
        self.last_humi = 20
        if pin > 0:
            print("Analysis performed by dht instead of simulator")
            self.sim = False
            self.dht = dht.DHT11(machine.Pin(pin))
    
    def measure(self):
        if self.simulator:
            ui_enabled.set_text("simulator")
            return
        
    def temperature(self):
        if self.simulator:
            self.last_temp = 22 + random.randint(-5,10)
            return self.last_temp
        
    def humidity(self):
        if self.simulator:
            self.last_humi = 30 + random.randint(-5,15)
            return self.last_humi



if __name__ == "__main__":

    led = neopixel.NeoPixel(Pin(48), Pin.OUT)
    led.fill((50, 50, 50))
    led.write()
    #led = LED()

    ui_enabled.set_text("booting")
    ui_connected.set_text("booting")
    ui_ip_data.set_text("booting")
    utime.sleep(1)
    
    # used by ESP32
    #th = task_handler.TaskHandler()

    #d = dht.DHT11(machine.Pin(40))
    d = simDHT(0)
    d.measure()
    temp_init = d.temperature()
    humidity_init = d.humidity()
    
    #temp_init = 22
    #humidity_init = 20
    
    print("initial temperature: {:.2f} °C".format(temp_init))
    print("initial humidity: {:.2f} %".format(humidity_init))

    wifi_manager = WiFiManager(secretssid, secretpwd, 'temp_humidity', '12345678')
    ssid, ip_address, status = wifi_manager.configure_wifi()
    ssid = "secret"
    #ssid, ip_address, status = ("ssid","1.2.3.4","disabled")
    print(f'SSID: {ssid}, IP: {ip_address}, Status: {status}')

    ui_enabled.set_text("disabled")  # MQTT status
    ui_connected.set_text(status)    # Wifi status
    ui_ip_data.set_text(ip_address)
    utime.sleep(1)

    led.fill((60, 0, 0))
    led.write()

    temperature_list = []
    humidity_list = []
    for i in range(0,10):
        temperature_list.append(d.temperature() )
        humidity_list.append(d.humidity() )

    asyncio.run(main())    
