FROM ubuntu:noble-20250925

RUN apt-get update && apt-get -y install \
     build-essential cmake ninja-build git \
     libusb-1.0-0-dev \
     gcc-arm-none-eabi \ 
     net-tools nano mc \
     python3-venv && \
     rm -rf /var/lib/apt/lists/*
     
WORKDIR /home/ubuntu
USER root

RUN git clone https://github.com/lvgl_micropython.git

WORKDIR  /home/ubuntu/lvgl_micropython
