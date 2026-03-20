//  main.cpp (step 1)
//  created: 15 March 2026
//  
//  Copyright (C) 2026 KW Services.
//  MIT License
//  Visual Studio Code 1.111.0 2026-03-06
//  PlatformIO Core 6.1.19 Home 3.4.4
//  TFT_eSPI 2.5.43 Bodmer
//  XPT2046 Touchscreen 1.4  Paul Stoffregen
//  LVGL 9.2.2
//  SquareLine Studios 1.5.4
//
#include <Arduino.h>
#include <TFT_eSPI.h>

// put function declarations here:
static const uint16_t screenWidth = TFT_WIDTH;
static const uint16_t screenHeight = TFT_HEIGHT;

TFT_eSPI tft = TFT_eSPI(screenWidth, screenHeight); // Initialize TFT display 

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.printf("main.cpp start\n");
  tft.begin();
  tft.setRotation(0); // Set display orientation
  tft.fillScreen(TFT_BLACK); // Clear the screen
  tft.setCursor(0, 0); // Set cursor to top-left corner
  tft.setTextColor(TFT_WHITE); // Set text color to white 
  tft.println("Hello World!");
}

void loop() {
  // put your main code here, to run repeatedly:
}

