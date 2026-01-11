// sketch_test_slider.ino
//
// Created: 07 January 2026
//
// Copyright (C) 2026 KW Services.
// MIT License
//
// Verified on:
// LVGL (9.3.0) Arduino 2.3.7
// Waveshare ESP32-P4-Module0-DEV-KIT

#ifndef BOARD_HAS_PSRAM
#error "Error: This program requires PSRAM enabled, please enable PSRAM option in 'Tools' menu of Arduino IDE"
#endif

#include <Arduino_GFX_Library.h>
#include "gt911.h"
#include <lvgl.h>
#include "lv_conf.h"
#include <demos/lv_demos.h>

static esp_lcd_touch_handle_t tp_handle = NULL;
#define MAX_TOUCH_POINTS 5

#ifndef CURRENT_SCREEN
#define CURRENT_SCREEN SCREEN_8_1_DSI_TOUCH_A
#endif
#include "displays_config.h"

Arduino_ESP32DSIPanel *dsipanel = new Arduino_ESP32DSIPanel(
  display_cfg.hsync_pulse_width,
  display_cfg.hsync_back_porch,
  display_cfg.hsync_front_porch,
  display_cfg.vsync_pulse_width,
  display_cfg.vsync_back_porch,
  display_cfg.vsync_front_porch,
  display_cfg.prefer_speed,
  display_cfg.lane_bit_rate);

// original
// Arduino_DSI_Display *gfx = new Arduino_DSI_Display(
//   display_cfg.width,
//   display_cfg.height,
//   dsipanel,
//   0,
//   true,
//   -1,
//   display_cfg.init_cmds,
//   display_cfg.init_cmds_size);

Arduino_DSI_Display *gfx = new Arduino_DSI_Display(
  display_cfg.width,
  display_cfg.height,
  dsipanel,
  1,
  true,
  -1,
  display_cfg.init_cmds,
  display_cfg.init_cmds_size);

#define LVGL_TICK_PERIOD 5  // ms
#define DRAW_BUF_HEIGHT 50
static lv_display_t *lv_display;
static lv_indev_t *indev_touchpad;
static lv_color_t *lv_draw_buf1;
static lv_color_t *lv_draw_buf2;
static uint16_t touch_x[MAX_TOUCH_POINTS] = { 0 };
static uint16_t touch_y[MAX_TOUCH_POINTS] = { 0 };
static uint16_t touch_strength[MAX_TOUCH_POINTS] = { 0 };
static uint8_t touch_cnt = 0;
static bool touch_pressed = false;

void my_disp_flush(lv_display_t *disp, const lv_area_t *area, uint8_t *px_map) {
  uint32_t w = (area->x2 - area->x1 + 1);
  uint32_t h = (area->y2 - area->y1 + 1);

  gfx->draw16bitRGBBitmap(area->x1, area->y1, (uint16_t *)px_map, w, h);
  lv_display_flush_ready(disp);
}

void my_touchpad_read(lv_indev_t *indev, lv_indev_data_t *data) {
  esp_lcd_touch_read_data(tp_handle);
  touch_pressed = esp_lcd_touch_get_coordinates(
    tp_handle, touch_x, touch_y, touch_strength, &touch_cnt, MAX_TOUCH_POINTS);

  if (touch_pressed && touch_cnt > 0) {
    data->point.x = touch_y[0];
    data->point.y = (800 - 1) - touch_x[0];
    data->state = LV_INDEV_STATE_PRESSED;
  } else {
    data->state = LV_INDEV_STATE_RELEASED;
  }
}

void lvglTick(void *param) {
  lv_tick_inc(LVGL_TICK_PERIOD);
}


// Global objects for the label, slider, and button so they can be accessed in event handlers
lv_obj_t * slider_label;
lv_obj_t * slider;

static void slider_event_cb(lv_event_t * e);
static void button_event_cb(lv_event_t * e);
///////////////////////////////////////


void setup(void) {
  Serial.begin(115200);
  Serial.println("Arduino GFX + LVGL Integration");

  delay(1000);

  DEV_I2C_Port port = DEV_I2C_Init();
  display_init(port);
  tp_handle = touch_gt911_init(port);

  if (!gfx->begin()) {
    Serial.println("gfx->begin() failed!");
  }

  for (int i = 0; i <= 240; i++) {
    set_display_backlight(port, i);
    delay(3);
  }

  lv_init();

  size_t draw_buf_size = display_cfg.width * DRAW_BUF_HEIGHT;
  lv_draw_buf1 = (lv_color_t *)heap_caps_malloc(draw_buf_size * sizeof(lv_color_t), MALLOC_CAP_SPIRAM);
  if (!lv_draw_buf1) {
    Serial.println("LVGL draw buffer 1 allocation failed!");
  }
  
  lv_draw_buf2 = (lv_color_t *)heap_caps_malloc(draw_buf_size * sizeof(lv_color_t), MALLOC_CAP_SPIRAM);
  if (!lv_draw_buf2) {
    Serial.println("LVGL draw buffer 2 allocation failed!");
    heap_caps_free(lv_draw_buf1);
  }
  //// display create ////////////////

  //lv_display = lv_display_create(display_cfg.width, display_cfg.height);
  lv_display = lv_display_create(display_cfg.height, display_cfg.width);

  Serial.print("display_cfg width, height:");
  Serial.print(display_cfg.height);
  Serial.print(" and ");
  Serial.println(display_cfg.width);

  lv_display_set_flush_cb(lv_display, my_disp_flush);
  lv_display_set_buffers(lv_display, lv_draw_buf1, lv_draw_buf2, draw_buf_size, LV_DISPLAY_RENDER_MODE_PARTIAL);

  lv_display_t *disp = lv_display_get_default();

  indev_touchpad = lv_indev_create();
  lv_indev_set_type(indev_touchpad, LV_INDEV_TYPE_POINTER);
  lv_indev_set_read_cb(indev_touchpad, my_touchpad_read);

  const esp_timer_create_args_t lvgl_timer_args = {
    .callback = &lvglTick,
    .name = "lvgl_timer"
  };
  esp_timer_handle_t lvgl_timer;
  esp_timer_create(&lvgl_timer_args, &lvgl_timer);
  esp_timer_start_periodic(lvgl_timer, LVGL_TICK_PERIOD * 1000);

  lv_display_set_dpi(lv_display, 150);
  lv_obj_set_style_bg_color(lv_screen_active(), lv_color_black(), 0);


  // Get the active screen
  lv_obj_t * scr = lv_screen_active();

  // Create a slider
  slider = lv_slider_create(scr);
  //lv_obj_set_width(slider, 200); // Set the width
  lv_obj_set_size(slider, 600, 40);
  lv_obj_center(slider); // Align to the center of the screen
  // Set the range of the slider
  lv_slider_set_range(slider, 0, 100);

  // Assign an event function to the slider
  lv_obj_add_event_cb(slider, slider_event_cb, LV_EVENT_VALUE_CHANGED, NULL);

  // Create a label above the slider to show its value
  slider_label = lv_label_create(scr);
  lv_label_set_text(slider_label, "Value: 0"); // Initial text
  lv_obj_align_to(slider_label, slider, LV_ALIGN_OUT_TOP_MID, 0, -65); // Align top of the slider
  lv_obj_set_style_text_color(slider_label, lv_color_white(), LV_PART_MAIN);
  lv_obj_set_style_text_font(slider_label, &lv_font_montserrat_32, LV_PART_MAIN);
  //--- Create Button ---

  // Create a button object
  lv_obj_t * button = lv_btn_create(scr);
  lv_obj_set_pos(button, 50, 200); // Set its position
  lv_obj_set_size(button, 240, 80); // Set its size
  // Add event callback for the button
  lv_obj_add_event_cb(button, button_event_cb, LV_EVENT_CLICKED, NULL);

  // Create a label inside the button
  lv_obj_t * btn_label = lv_label_create(button);
  lv_label_set_text(btn_label, "Reset Slider"); // Set the label's text
  lv_obj_center(btn_label); // Center the label within the button
  lv_obj_set_style_text_color(btn_label, lv_color_black(), LV_PART_MAIN);
  lv_obj_set_style_text_font(btn_label, &lv_font_montserrat_32, LV_PART_MAIN);

  Serial.println("Setup complete");
}

/* Function for the slider event callback */
static void slider_event_cb(lv_event_t * e) {
    // Get the slider object that triggered the event
    lv_obj_t * s = (lv_obj_t*)lv_event_get_target(e);
    // Get the current value of the slider
    int32_t value = lv_slider_get_value(s);
    // Update the label text to show the current value
    lv_label_set_text_fmt(slider_label, "Value: %d", value);
    // Reposition the label to be above the slider
    lv_obj_align_to(slider_label, slider, LV_ALIGN_OUT_TOP_MID, 0, -15);
}

/* Function for the button event callback */
static void button_event_cb(lv_event_t * e) {
    lv_event_code_t code = lv_event_get_code(e);
    if (code == LV_EVENT_CLICKED) {
        // Reset the slider value to 0 with animation
        lv_slider_set_value(slider, 0, LV_ANIM_ON);
        // Manually update the label text to "Value: 0"
        lv_label_set_text_fmt(slider_label, "Value: %d", 0);
        lv_obj_align_to(slider_label, slider, LV_ALIGN_OUT_TOP_MID, 0, -15);
    }
}


void loop() {
  lv_timer_handler();
  delay(5);
}