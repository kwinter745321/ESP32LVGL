// sketch_test_chart.ino
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

void create_chart(void);
void update_chart_data(lv_timer_t * timer);
// Global objects for chart and series
/* Change to your screen resolution */
#define SCREEN_WIDTH 1280
#define SCREEN_HEIGHT 800

lv_obj_t * chart;
lv_chart_series_t * ser1;
void lv_example_chart_1(lv_obj_t *parent);
void lv_example_chart_2(lv_obj_t *parent);
void lv_example_chart_7(lv_obj_t *parent);
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

  create_chart();
  // Get the active screen
  lv_obj_t * scr = lv_screen_active();

  // Create a timer to periodically update the chart data
  // The timer will call 'update_chart_data' every 1000ms
  //lv_timer_create(update_chart_data, 1000, NULL);

  Serial.println("Setup complete");
}

void create_chart(void) {
  /* Create a chart object on the active screen */

  static lv_style_t tab_btn_style;
  lv_style_init(&tab_btn_style);
  lv_style_set_text_font(&tab_btn_style, &lv_font_montserrat_40); // Use your desired font

  /*Create a Tab view object*/
  lv_obj_t * tabview;
  tabview = lv_tabview_create(lv_screen_active());
  // Set the background color of the main content area for ALL tabs
  lv_obj_set_style_bg_color(lv_tabview_get_content(tabview), lv_color_black(), LV_PART_MAIN);
  lv_obj_set_style_bg_opa(lv_tabview_get_content(tabview), LV_OPA_COVER, LV_PART_MAIN); // Ensure full opacity
 

  /*Add 3 tabs (the tabs are page (lv_page) and can be scrolled*/
  lv_obj_t * tab1 = lv_tabview_add_tab(tabview, "Line Chart");
  lv_obj_t * tab2 = lv_tabview_add_tab(tabview, "Bar Chart");
  lv_obj_t * tab3 = lv_tabview_add_tab(tabview, "Scatter Chart");
  lv_obj_add_style(lv_tabview_get_tab_btns(tabview), &tab_btn_style, LV_PART_MAIN);

  // lv_obj_set_style_bg_color(tab1, lv_color_black(), LV_PART_MAIN);
  // lv_obj_set_style_bg_color(tab2, lv_color_black(), LV_PART_MAIN);
  // lv_obj_set_style_bg_color(tab3, lv_color_black(), LV_PART_MAIN);
  // lv_obj_set_style_text_font(tab1, &lv_font_montserrat_32, LV_PART_MAIN);
  // lv_obj_set_style_text_font(tab2, &lv_font_montserrat_32, LV_PART_MAIN);
  // lv_obj_set_style_text_font(tab3, &lv_font_montserrat_32, LV_PART_MAIN);
  //lv_obj_add_style(lv_tabview_get_tab_btns(tabview), &tab_btn_style, LV_PART_ITEMS);

  /*Add content to the tabs*/
  lv_example_chart_1(tab1);
  lv_example_chart_2(tab2);
  lv_example_chart_7(tab3);
   
}

void lv_example_chart_1(lv_obj_t  *parent)
{
    lv_obj_t * main_cont = lv_obj_create(parent);
    lv_obj_set_size(main_cont, 1200, 600);
    lv_obj_center(main_cont);

    /*Create a transparent wrapper for the chart and the scale.
     *Set a large width, to make it scrollable on the main container*/
    lv_obj_t * wrapper = lv_obj_create(main_cont);
    lv_obj_remove_style_all(wrapper);
    //  change size to 100%
    lv_obj_set_size(wrapper, lv_pct(100), lv_pct(100));
    lv_obj_set_flex_flow(wrapper, LV_FLEX_FLOW_ROW);

    // lv_obj_t * yaxis = lv_scale_create(wrapper);
    // lv_obj_set_size(yaxis, 50, LV_PCT(90));
    // //lv_obj_set_style_pad_all(chart, 0, LV_PART_MAIN);
    // lv_obj_set_style_line_width(yaxis, 0, LV_PART_MAIN);
    // lv_scale_set_mode(yaxis, LV_SCALE_MODE_VERTICAL_LEFT);
    // lv_obj_set_align(yaxis, LV_ALIGN_LEFT_MID);
    // lv_obj_set_y(yaxis, 30);
    // lv_scale_set_range(yaxis, 0, 100);
    // lv_scale_set_total_tick_count(yaxis, 5);
    // lv_scale_set_major_tick_every(yaxis, 1);
    // //lv_scale_set_label_show(yaxis, true);
    // lv_obj_set_style_text_font(yaxis, &lv_font_montserrat_30, LV_PART_MAIN);

    /*Create a chart*/
    lv_obj_t * chart;
    chart = lv_chart_create(wrapper);
    lv_obj_set_size(chart, 1200, LV_PCT(90));
    //lv_obj_align_to(chart, yaxis, LV_ALIGN_OUT_RIGHT_TOP, 0, 0);
    //lv_obj_set_style_pad_all(chart, 0, LV_PART_MAIN);
    //lv_obj_set_height(chart, lv_pct(90));
    lv_obj_set_flex_grow(chart, 1);
    //lv_obj_set_y(yaxis, 30);
    //lv_obj_center(chart);
    lv_chart_set_type(chart, LV_CHART_TYPE_LINE);   /*Show lines and points too*/
    lv_obj_set_style_line_color(chart, lv_palette_main(LV_PALETTE_BLUE), LV_PART_MAIN);
    lv_obj_set_style_line_width(chart, 3, LV_PART_MAIN); 
    lv_obj_set_style_line_opa(chart, LV_OPA_50, LV_PART_MAIN);

    lv_chart_set_axis_range(chart, LV_CHART_AXIS_PRIMARY_Y, 0, 100);
    lv_chart_set_div_line_count(chart, 5, 5);



    /*Add two data series*/
    lv_chart_series_t * ser1 = lv_chart_add_series(chart, lv_palette_main(LV_PALETTE_GREEN), LV_CHART_AXIS_PRIMARY_Y);
    lv_chart_series_t * ser2 = lv_chart_add_series(chart, lv_palette_main(LV_PALETTE_RED), LV_CHART_AXIS_SECONDARY_Y);
    int32_t * ser2_y_points = lv_chart_get_series_y_array(chart, ser2);

    uint32_t i;
    for(i = 0; i < 10; i++) {
        /*Set the next points on 'ser1'*/
        lv_chart_set_next_value(chart, ser1, (int32_t)lv_rand(10, 50));

        /*Directly set points on 'ser2'*/
        ser2_y_points[i] = (int32_t)lv_rand(50, 90);
    }

    lv_chart_refresh(chart); /*Required after direct set*/
}

void lv_example_chart_2(lv_obj_t  *parent)
{
    /*Create a container*/
    lv_obj_t * main_cont = lv_obj_create(parent);
    lv_obj_set_size(main_cont, 1200, 600);
    lv_obj_center(main_cont);

    /*Create a transparent wrapper for the chart and the scale.
     *Set a large width, to make it scrollable on the main container*/
    lv_obj_t * wrapper = lv_obj_create(main_cont);
    lv_obj_remove_style_all(wrapper);
    //  change size to 100%
    lv_obj_set_size(wrapper, lv_pct(100), lv_pct(100));
    lv_obj_set_flex_flow(wrapper, LV_FLEX_FLOW_COLUMN);

    /*Create a chart on the wrapper
     *Set it's width to 100% to fill the large wrapper*/
    lv_obj_t * chart = lv_chart_create(wrapper);
    lv_obj_set_width(chart, lv_pct(100));
    lv_obj_set_flex_grow(chart, 1);
    lv_chart_set_type(chart, LV_CHART_TYPE_BAR);
    lv_chart_set_axis_range(chart, LV_CHART_AXIS_PRIMARY_Y, 0, 100);
    lv_chart_set_axis_range(chart, LV_CHART_AXIS_SECONDARY_Y, 0, 400);
    lv_chart_set_point_count(chart, 12);
    lv_obj_set_style_radius(chart, 0, 0);
    lv_obj_set_style_line_color(chart, lv_palette_main(LV_PALETTE_BLUE), LV_PART_MAIN);  //change division lines to blue
    lv_obj_set_style_line_width(chart, 3, LV_PART_MAIN); 
    lv_obj_set_style_line_opa(chart, LV_OPA_50, LV_PART_MAIN);

    /*Create a scale also with 100% width*/
    lv_obj_t * scale_bottom = lv_scale_create(wrapper);
    lv_scale_set_mode(scale_bottom, LV_SCALE_MODE_HORIZONTAL_BOTTOM);
    lv_obj_set_size(scale_bottom, lv_pct(100), 50);  //changed from 25
    lv_scale_set_total_tick_count(scale_bottom, 12);
    lv_scale_set_major_tick_every(scale_bottom, 1);
    lv_obj_set_style_pad_hor(scale_bottom, lv_chart_get_first_point_center_offset(chart), 0);

    static const char * month[] = {"Jan", "Febr", "March", "Apr", "May", "Jun", "July", "Aug", "Sept", "Oct", "Nov", "Dec", NULL};
    lv_scale_set_text_src(scale_bottom, month);

    lv_obj_set_style_text_font(scale_bottom, &lv_font_montserrat_30, LV_PART_MAIN);

    /*Add two data series*/
    lv_chart_series_t * ser1 = lv_chart_add_series(chart, lv_palette_lighten(LV_PALETTE_GREEN, 2), LV_CHART_AXIS_PRIMARY_Y);
    lv_chart_series_t * ser2 = lv_chart_add_series(chart, lv_palette_darken(LV_PALETTE_GREEN, 2), LV_CHART_AXIS_PRIMARY_Y);

    /*Set the next points on 'ser1'*/
    uint32_t i;
    for(i = 0; i < 12; i++) {
        lv_chart_set_next_value(chart, ser1, (int32_t)lv_rand(10, 60));
        lv_chart_set_next_value(chart, ser2, (int32_t)lv_rand(50, 90));
    }
    lv_chart_refresh(chart); /*Required after direct set*/
}

static void draw_event_cb(lv_event_t * e)
{
    lv_draw_task_t * draw_task = lv_event_get_draw_task(e);
    lv_draw_dsc_base_t * base_dsc = (lv_draw_dsc_base_t *)lv_draw_task_get_draw_dsc(draw_task);
    if(base_dsc->part == LV_PART_INDICATOR) {
        lv_obj_t * obj = lv_event_get_target_obj(e);
        lv_chart_series_t * ser = lv_chart_get_series_next(obj, NULL);
        lv_draw_rect_dsc_t * rect_draw_dsc = (lv_draw_rect_dsc_t *)lv_draw_task_get_draw_dsc(draw_task);
        uint32_t cnt = lv_chart_get_point_count(obj);

        /*Make older value more transparent*/
        rect_draw_dsc->bg_opa = (lv_opa_t)((LV_OPA_COVER * base_dsc->id2) / (cnt - 1));

        /*Make smaller values blue, higher values red*/
        int32_t * x_array = lv_chart_get_series_x_array(obj, ser);
        int32_t * y_array = lv_chart_get_series_y_array(obj, ser);
        /*dsc->id is the tells drawing order, but we need the ID of the point being drawn.*/
        uint32_t start_point = lv_chart_get_x_start_point(obj, ser);
        uint32_t p_act = (start_point + base_dsc->id2) % cnt; /*Consider start point to get the index of the array*/
        lv_opa_t x_opa = (lv_opa_t)((x_array[p_act] * LV_OPA_50) / 200);
        lv_opa_t y_opa = (lv_opa_t)((y_array[p_act] * LV_OPA_50) / 1000);

        rect_draw_dsc->bg_color = lv_color_mix(lv_palette_main(LV_PALETTE_RED),
                                               lv_palette_main(LV_PALETTE_BLUE),
                                               x_opa + y_opa);
    }
}

static void add_data(lv_timer_t * timer)
{
    lv_obj_t * chart = (lv_obj_t *)lv_timer_get_user_data(timer);
    lv_chart_set_next_value2(chart, lv_chart_get_series_next(chart, NULL), (int32_t)lv_rand(0, 200),
                             (int32_t)lv_rand(0, 1000));
}

/**
 * A scatter chart
 */
void lv_example_chart_7(lv_obj_t  *parent)
{
    lv_obj_t * chart = lv_chart_create(parent);
    lv_obj_set_size(chart, 1200, 600);
    lv_obj_align(chart, LV_ALIGN_CENTER, 0, 0);
    lv_obj_add_event_cb(chart, draw_event_cb, LV_EVENT_DRAW_TASK_ADDED, NULL);
    lv_obj_add_flag(chart, LV_OBJ_FLAG_SEND_DRAW_TASK_EVENTS);
    lv_obj_set_style_line_width(chart, 0, LV_PART_ITEMS);   /*Remove the lines*/
    lv_obj_set_style_line_color(chart, lv_palette_main(LV_PALETTE_BLUE), LV_PART_MAIN);  //division lines
    lv_obj_set_style_line_width(chart, 3, LV_PART_MAIN); 
    lv_obj_set_style_line_opa(chart, LV_OPA_50, LV_PART_MAIN);

    lv_chart_set_type(chart, LV_CHART_TYPE_SCATTER);

    lv_chart_set_axis_range(chart, LV_CHART_AXIS_PRIMARY_X, 0, 200);
    lv_chart_set_axis_range(chart, LV_CHART_AXIS_PRIMARY_Y, 0, 1000);

    lv_chart_set_point_count(chart, 50);

    lv_chart_series_t * ser = lv_chart_add_series(chart, lv_palette_main(LV_PALETTE_RED), LV_CHART_AXIS_PRIMARY_Y);
    uint32_t i;
    for(i = 0; i < 50; i++) {
        lv_chart_set_next_value2(chart, ser, (int32_t)lv_rand(0, 200), (int32_t)lv_rand(0, 1000));
    }

    lv_timer_create(add_data, 100, chart);
}

void loop() {
  lv_timer_handler();
  delay(5);
}