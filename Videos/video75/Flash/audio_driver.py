# audio_driver.py
#
# Created: 03 February 2026 (custom to the device)
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# Waveshare ESP32-S3-Touch-LCD-3.5C
# MicroPython v1.20.0-2510.gacfeb7b7e.dirty on 2025-11-23;
# Generic ESP32S3 module with ESP32S3
#

from machine import reset, Pin, PWM
from display_driver import disp, touch
import time

from machine import SoftI2C
from machine import I2S
import tca9554
import es8311

i2c = SoftI2C( scl=Pin(7), sda=Pin(8), freq=100_000)


TCA9554_ADDR = 0x20
tca = tca9554.TCA9554(TCA9554_ADDR)
#tca.write_config_port(3, tca9554.OUTPUT)
tca.write_config_port(7, tca9554.OUTPUT)
tca.write_port(7, True)


codec = es8311.ES8311(i2c)
codec.init_es8311()

# Configuration

#### I2S ####################
mck_pin = Pin(12)   # master clock
sck_pin = Pin(13)   # Serial clock output
ws_pin = Pin(15)    # Word clock output
sd_pin = Pin(16)    # Serial data output

SAMPLE_RATE = 44100   #16000   #44100
BUFFER_SIZE = 1024  #1024 # Buffer size for reading file chunks

CLOCK_PIN = 12                     # MCK pin
MASTER_FREQ_HZ = SAMPLE_RATE*256   # Set the required master clock frequency in Hz (e.g., 44100)
DUTY_CYCLE_50_PERCENT = 32768      # 50% duty cycle for 16-bit resolution (65535 / 2)
mck_pwm = PWM(mck_pin, freq=MASTER_FREQ_HZ, duty_u16=DUTY_CYCLE_50_PERCENT)
print(f"Master clock running on Pin {CLOCK_PIN} at {mck_pwm.freq()} Hz with 50% duty cycle.")

#### Globals
dac_volume = 60
audio_out = None
done = False
paused = False
file = ""

def reset_globals():
    global dac_volume, done, paused, file
    dac_volume = 60
    done = False
    paused = False
    file = ""

def set_volume(volume):
    global dac_volume
    if volume < 50:
        volume = 50
    dac_volume = volume
                
def send_audio(filename):
    global sck_pin, ws_pin, sd_pin, SAMPLE_RATE, BUFFER_SIZE
    chunk = 0
    pa_status = tca.write_port(7, 1)
    print("Power Amplifier Status:",pa_status)
    
    audio_out = I2S(0,
                sck=sck_pin, ws=ws_pin, sd=sd_pin,
                mode=I2S.TX,
                bits=16,
                format=I2S.MONO,
                rate=SAMPLE_RATE,
                ibuf=BUFFER_SIZE
                )
    print("Audio DAC volume:",dac_volume)
    codec.set_dac_volume(dac_volume)
    try:
        if filename == "":
            filename = "test_7thlife-7.wav"
        file = filename
        if filename[0] == "7":
            filename = "test_" + filename
        print("audio_out playing",filename)
        with open(filename, 'rb') as f:
            f.seek(44)  #skip WAV header
            wav_sample = bytearray(BUFFER_SIZE)
            wav_sample_mv = memoryview(wav_sample)
            while True:
                # Read a chunk of data from the file into the buffer
                chunk += 1
                num_read = f.readinto(wav_sample_mv)
                # Check for end of file
                if num_read == 0:
                    break
                # Use a slice if the buffer wasn't completely filled
                audio_out.write(wav_sample_mv[:num_read])
    except OSError as e:
        print(f"Error opening/reading file: {e}")
    finally:
        # Deinitialize I2S after playback is complete
        print("Blocks read:[{}]".format(chunk))
        audio_out.deinit()
        pa_status = tca.write_port(7, 0)
        