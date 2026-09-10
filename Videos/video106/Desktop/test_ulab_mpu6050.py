# test_ulab_mpu6050.py
#
# Created: 08 September 2026 
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.29.0-dirty on 2026-09-02;
# Generic ESP32S3 module with Octal-SPIRAM with ESP32-S3

# Using MPU6050 driver from
# https://github.com/Lezgend/MPU6050-MicroPython

# Example code for (GY-521) MPU6050 Accelerometer/Gyro Module
# Modified to use MicroPython ulab ndarrays/tensors
#
# The MPU6050 returns scalar values, so this version places the
# accelerometer readings into a 1-D ulab tensor and performs the
# vector math with ulab.numpy universal functions.

from MPU6050 import MPU6050
from ulab import numpy as np
from time import sleep_ms

mpu = MPU6050()

# Tensor containing [ax, ay, az].
# A float32 array 
accel = np.zeros(3)

# Reusable working tensors.
# accel_sq = [ax^2, ay^2, az^2]
accel_sq = np.zeros(3)

for i in range(0,1):
    # Read the accelerometer.
    data = mpu.read_accel_data()
    #print(f"Sensor Reading:{data}")
    # Put the three sensor axes into one ulab tensor.
    accel[0] = data["x"]
    accel[1] = data["y"]
    accel[2] = data["z"]
    #print(f"accel tensor:{accel}")

    # Tensor indexes:
    ax = accel[0]
    ay = accel[1]
    az = accel[2]

    # Square all three axes as an ndarray operation.
    accel_sq = accel * accel
    #print(f"accel_sq:{accel_sq}")

    # sqrt(ay^2 + az^2)
    # sqrt(ax^2 + az^2)
    yz_norm = np.sqrt(accel_sq[1] + accel_sq[2])
    xz_norm = np.sqrt(accel_sq[0] + accel_sq[2])

    # Calculate pitch and roll
    pitch = np.degrees(np.arctan2(ay, yz_norm))
    roll = np.degrees(np.arctan2(-ax, xz_norm))

    print(f"Pitch: {pitch} deg | Roll: {roll} deg")

    # Time interval delay in milliseconds.
    sleep_ms(1000)
    