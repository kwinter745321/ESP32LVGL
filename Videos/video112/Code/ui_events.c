// UI_events.c
// created: 21 October 2026
//
// Copyright (C) 2026 KW Services.
// MIT License
//
// Arduino IDE 2.3.10
// Arduino ESP32 Boards 2.0.18
// esp32 by Espressif 3.3.12
// TFT_eSPI 2.5.43
// XPowersLIB 0.3.4
// SensorLIB 0.5.0

#include "ui.h"

#include "esp_random.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

extern int32_t var_level;
int fill_count = 0;
int blue_score = 0;
int green_score = 0;
int red_score = 0;
int yellow_score = 0;
int grand_total = 0;

#define BLUE          lv_color_hex(0x8FA8FF)
#define GREEN         lv_color_hex(0x39FF14)
#define RED           lv_color_hex(0xFF8383)
#define YELLOW        lv_color_hex(0xFFF01F)

// Display totals
void update_totals()
{
    char buf[64];
    snprintf(buf, sizeof(buf),"%d",grand_total);
    lv_label_set_text(ui_lbl_score, buf);
    snprintf(buf, sizeof(buf),"Blue:   %d",blue_score);
    lv_label_set_text(ui_lbl_blue, buf);
    snprintf(buf, sizeof(buf),"Green:  %d",green_score);
    lv_label_set_text(ui_lbl_green, buf);
    snprintf(buf, sizeof(buf),"Red:    %d",red_score);
    lv_label_set_text(ui_lbl_red, buf);
    snprintf(buf, sizeof(buf),"Yellow: %d",yellow_score);
    lv_label_set_text(ui_lbl_yellow, buf);
}

// The callback when you touch a button
void item_cb(lv_event_t * e)
{
    lv_event_code_t event_code = lv_event_get_code(e);
    
    if (event_code == LV_EVENT_CLICKED) {
        lv_obj_t * btn = lv_event_get_target_obj(e); 
        lv_color_t color = lv_obj_get_style_bg_color(btn, LV_PART_MAIN);
        lv_obj_t * btn_lbl = lv_obj_get_child(btn, 0);
        if (btn_lbl != NULL) {
            const char * txt = lv_label_get_text(btn_lbl);
            lv_obj_delete_delayed(btn, 220);
            int score = atoi(txt);
            if (lv_color_eq(color,BLUE)) blue_score -= score;
            if (lv_color_eq(color,GREEN)) green_score -= score;
            if (lv_color_eq(color,RED)) red_score -= score;
            if (lv_color_eq(color,YELLOW)) yellow_score -= score;
            grand_total -= score;
            update_totals();
        }

    }
}

// The callback when you press the START button
void add_cb(lv_event_t * e)
{
    lv_event_code_t event_code = lv_event_get_code(e);
    
    if (event_code == LV_EVENT_CLICKED) {
        lv_color_t color;
        lv_color_t bcolor;
        srand(time(NULL));
        int32_t val = lv_slider_get_value(ui_slider_count);
        char buf[64];
        lv_obj_clean(ui_cont_number);
        fill_count = 0;
        blue_score = 0;
        green_score = 0;
        red_score = 0;
        yellow_score = 0;
        grand_total = 0;
    
        for (int i = 1; i <= val*2; i++) {
            memset(buf,0,sizeof(buf));
            int random_num = ( rand() % 40) + 25;
            int dice = ( rand() % 4);
            snprintf(buf, sizeof(buf), "%d", random_num);
            lv_obj_t * btn = lv_button_create(ui_cont_number);
            lv_obj_set_width(btn, random_num);
            lv_obj_set_height(btn, random_num);
            lv_obj_set_style_radius(btn, LV_RADIUS_CIRCLE, 0);
            switch (dice) {
                case 0:
                    color = BLUE;
                    blue_score += random_num;
                    break;
                case 1:
                    color = GREEN;
                    green_score += random_num;
                    break;
                case 2:
                    color = RED;
                    red_score += random_num;
                    break;
                case 3:
                    color = YELLOW;
                    yellow_score += random_num;
                    break;
            }
            grand_total += random_num;
            lv_obj_set_style_bg_color(btn, color, LV_PART_MAIN | LV_STATE_DEFAULT);
            lv_obj_t * btn_lbl = lv_label_create(btn);
            lv_obj_center(btn_lbl);
            lv_label_set_text(btn_lbl, buf);
            lv_obj_set_style_text_color(btn_lbl, lv_color_black(), LV_PART_MAIN | LV_STATE_DEFAULT);

            lv_obj_update_layout(ui_cont_number);
            int32_t btn_right = lv_obj_get_x2(btn);
            int32_t container_right = lv_obj_get_x2(ui_cont_number) - lv_obj_get_style_pad_right(ui_cont_number, LV_PART_MAIN);
            if(btn_right > container_right) {
                /* Remove hidden btn and stop adding buttons */
                lv_obj_delete(btn);
                break;
            }
            fill_count++;
            lv_obj_add_event_cb(btn, item_cb, LV_EVENT_CLICKED, NULL);

        }
        update_totals();
    }

}




