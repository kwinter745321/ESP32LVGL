#
# Dockerfile
# 
# Creates development environment to build ESP32 firmware
#
# Copyright (C) 2025 KW Services.
# MIT License
# Docker version 28.1.1, build 4eba377
# LVGL source pulled 25 September 2025
# MicroPython v1.20.0-2510.gacfeb7b7e on 2025-09-25; Generic ESP32S3 module with ESP32S3
# LVGL 9.3
#
#
###############################################################################
FROM espressif/idf:v5.2.2

RUN apt-get update && apt-get -y install \
     build-essential cmake ninja-build \
     libusb-1.0-0-dev \
     gcc-arm-none-eabi \ 
     net-tools \
     python3-venv \
     openssh-server \
     nano \
     mc && \
     rm -rf /var/lib/apt/lists/*
     
RUN . /opt/esp/idf/export.sh

WORKDIR /home
USER root

RUN git clone https://github.com/lvgl/lv_micropython.git

WORKDIR /home/lv_micropython/mpy-cross
RUN make

WORKDIR /home/lv_micropython/user_modules
RUN rmdir /home/lv_micropython/user_modules/lv_binding_micropython
RUN git clone https://github.com/lvgl/lv_binding_micropython.git

WORKDIR /home/lv_micropython
RUN git submodule update --init --recursive
###############################################################################


