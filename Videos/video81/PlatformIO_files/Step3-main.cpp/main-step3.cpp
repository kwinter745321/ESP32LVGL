//  main.cpp (step 3)
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
#include <SPI.h>
#include <XPT2046_Touchscreen.h>


extern "C" {
  #include <simple_ui/ui.h>
}


////  TFT Initialize  /////////////////////////////////////////////

static const uint16_t screenWidth = TFT_WIDTH;
static const uint16_t screenHeight = TFT_HEIGHT;

TFT_eSPI tft = TFT_eSPI(screenWidth, screenHeight); 

///  Touchscreen Initilize ////////////////////////////////////////

XPT2046_Touchscreen ts(TOUCH_CS, TOUCH_IRQ);
SPIClass customSPI = SPIClass(VSPI);


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

//// INDEV callback for touchscreen /////////////////////////////////////////////////////////

#if TFT_ROTATION == 0
  #define ORIENTATION LV_DISP_ROTATION_0
#elif TFT_ROTATION == 1
  #define ORIENTATION LV_DISP_ROTATION_90
#elif TFT_ROTATION == 2
  #define ORIENTATION LV_DISP_ROTATION_180
#elif TFT_ROTATION == 3
  #define ORIENTATION LV_DISP_ROTATION_270
#endif

void my_touchpad_read(lv_indev_t *indev, lv_indev_data_t *data) {
  uint16_t x, y;
  if ( ts.tirqTouched() && ts.touched() ) {
        TS_Point p = ts.getPoint();

        switch(TFT_ROTATION) {
          case LV_DISPLAY_ROTATION_0 :                                            
            x = map(p.x, 280, 3850, 0, TFT_WIDTH);
            y = TFT_HEIGHT - map(p.y, 200, 3730, 0, TFT_HEIGHT);
            x = constrain(x, 0, TFT_WIDTH - 1);
            y = constrain(y, 0, TFT_HEIGHT - 1);
            break;

          case LV_DISPLAY_ROTATION_90:                                            
            x = TFT_HEIGHT - map(p.x, 180, 3750, 0, TFT_HEIGHT);
            y = TFT_WIDTH - map(p.y, 275, 3850, 0, TFT_WIDTH);
            x = constrain(x, 0, TFT_HEIGHT - 1);
            y = constrain(y, 0, TFT_WIDTH - 1);
            break;

          case LV_DISPLAY_ROTATION_180:                                         
            x = TFT_WIDTH - map(p.x, 280, 3850, 0, TFT_WIDTH);
            y = map(p.y, 200, 3730, 0, TFT_HEIGHT);
            x = constrain(x, 0, TFT_WIDTH - 1);
            y = constrain(y, 0, TFT_HEIGHT - 1);
            break;

          case LV_DISPLAY_ROTATION_270:                                          
            //x = TFT_HEIGHT - map(p.x, 180, 3750, 0, TFT_HEIGHT);
            ///y = map(p.y, 275, 3850, 0, TFT_WIDTH);
            x = TFT_HEIGHT - map(p.x, 280, 3600, 0, TFT_HEIGHT);
            y = map(p.y, 314, 3500, 0, TFT_WIDTH);
            x = constrain(x, 0, TFT_HEIGHT - 1);
            y = constrain(y, 0, TFT_WIDTH - 1);
            break;

          default:
              Serial.printf("Error: invalid rotation value = %d", TFT_ROTATION);
              x = 0;
              y = 0;
              break;
        }

        data->point.x = x;
        data->point.y = y;
	data->state = LV_INDEV_STATE_PRESSED;

        /////Serial.printf("touched: x:%d y:%d \n",data->point.x,data->point.y);
        
    } else {
        data->state = LV_INDEV_STATE_RELEASED;
    }
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
    Serial.begin(115200);
    Serial.printf("main.cpp start\n");
	
	
    ////  LVGL Initialize ///////////////////////////////////
    lv_init();
    Serial.printf("LVGL Version: %d.%d.%d\n", lv_version_major(),lv_version_minor(), lv_version_patch());


    //// TFT initialize ///////////////////////////////
    tft.begin();
    tft.setRotation(TFT_ROTATION);

    //// Touchscreen (ts) Initialize /////////////////////
    customSPI.begin(TOUCH_SCLK, TOUCH_MISO, TOUCH_MOSI, TOUCH_CS);
    ts.begin(customSPI);	
	

    //// Create display using buffers and flush ////////////////
    lv_display_t * disp = lv_display_create(screenWidth, screenHeight);
    lv_display_set_buffers(disp, draw_buf, NULL, BUF_SIZE, LV_DISPLAY_RENDER_MODE_PARTIAL);
    lv_display_set_flush_cb(disp, my_disp_flush);


    ////  ROTATION for Display and touchscreen
    lv_display_set_rotation(disp, ORIENTATION);
    ts.setRotation(TFT_ROTATION);

    /////Serial.printf("Display/Touch rotation:%d orientation:%d \n",TFT_ROTATION,ORIENTATION);

    //// Create INDEV for touchscreen //////////////////////////
    lv_indev_t *indev = lv_indev_create();
    lv_indev_set_type(indev, LV_INDEV_TYPE_POINTER);
    lv_indev_set_read_cb(indev, my_touchpad_read);



    // Basic UI element
    basic_ui();


    Serial.printf("simple_project Setup-end\n");
}


void loop() {
  ////lv_timer();
  lv_task_handler();
  lv_tick_inc(5);
  delay(5);
}
