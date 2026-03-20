//  main.cpp (step 2)
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
#include <lvgl.h>

////  TFT Initialize  /////////////////////////////////////////////

static const uint16_t screenWidth = TFT_WIDTH;
static const uint16_t screenHeight = TFT_HEIGHT;

TFT_eSPI tft = TFT_eSPI(screenWidth, screenHeight); 




////  LVGL Display buffer and flush  ///////////////////////////////////////////////////////////////

////  LVGL Display buffer and flush  ///////////////////////////////////////////////////////////////

#define BUF_SIZE (screenWidth * screenHeight) / 10 
uint32_t draw_buf[BUF_SIZE / 4]; // LVGL uses 32-bit aligned buffers

void my_disp_flush(lv_display_t *disp, const lv_area_t *area, uint8_t *px_map) {
    uint32_t w = (area->x2 - area->x1 + 1);
    uint32_t h = (area->y2 - area->y1 + 1);

    tft.startWrite();                           /* Start new SPI transaction */
    tft.setAddrWindow(area->x1, area->y1, w, h); /* set the display window */
    tft.pushColors((uint16_t*)px_map, w * h, true); /* push pixel buffer to screen */
    tft.endWrite();                             /* terminate SPI transaction */
    lv_display_flush_ready(disp);               /* tell LVGL that flush is ready */
}


//// Simple LVGL test button callback

int cnt = 0;

static void btn1_cb(lv_event_t *e)
{
  lv_event_code_t code = lv_event_get_code(e);
  lv_obj_t *btn = lv_event_get_target_obj(e);
  if ( code == LV_EVENT_CLICKED)
  {
      static uint8_t cnt = 0;
      cnt++;
      Serial.printf("Pressed");
      lv_obj_t *lbl = lv_obj_get_child(btn, 0);
      lv_label_set_text_fmt(lbl, "%d", cnt);
  }
}

static void basic_ui() {
    lv_obj_t *scr = lv_obj_create(lv_screen_active());
    lv_obj_set_size(scr, 240, 320);
    lv_obj_t *btn1 = lv_button_create(scr);
    lv_obj_center(btn1);
    lv_color_t black = lv_color_black();
    lv_color_t white = lv_color_white();
    lv_obj_t *lbl1 = lv_label_create(btn1);
    lv_label_set_text(lbl1, "Press Me");
    lv_obj_set_width(lbl1, 150);
    lv_obj_set_style_text_font(lbl1, &lv_font_montserrat_24, 0);
    lv_obj_center(lbl1);
    lv_obj_t *slider = lv_slider_create(scr);
    lv_obj_set_width(slider, 200);
    lv_obj_set_pos(slider, 1, 1);
    lv_obj_add_event_cb(btn1, btn1_cb, LV_EVENT_ALL, NULL);
}



void setup() {
  // put your setup code here, to run once:
    Serial.begin(115200);
    Serial.printf("main.cpp start\n");
	
	
	////  LVGL Initialize ///////////////////////////////////
    lv_init();
    Serial.printf("LVGL Version: %d.%d.%d\n", lv_version_major(),lv_version_minor(), lv_version_patch());


	//// TFT initialize ///////////////////////////////
    tft.begin();
    tft.setRotation(TFT_ROTATION);
	
	

    //// Initialize display hardware, buffer, and driver ////////////////
    lv_display_t * disp = lv_display_create(screenWidth, screenHeight);
    lv_display_set_buffers(disp, draw_buf, NULL, BUF_SIZE, LV_DISPLAY_RENDER_MODE_PARTIAL);
    lv_display_set_flush_cb(disp, my_disp_flush);



    // Basic UI element
	basic_ui();


    Serial.printf("simple_project Setup-end\n");
}

void loop() {
  lv_task_handler();
  lv_tick_inc(5);
  delay(5);
}
