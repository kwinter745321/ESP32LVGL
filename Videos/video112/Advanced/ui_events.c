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

// events to create and pop the balloons with animation

#include "ui.h"

#include "app_logic.h"
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

#define BLUE_BORDER   lv_color_hex(0x2B324C)
#define GREEN_BORDER  lv_color_hex(0x114C06)
#define RED_BORDER    lv_color_hex(0x4C2727)
#define YELLOW_BORDER lv_color_hex(0x4C4809)

//function prototype
void update_totals(void);

void pop_anim_ready_cb(lv_anim_t * a) 
{
    // Get the button object from the animation handle
    lv_obj_t * btn_balloon = (lv_obj_t *)a->var;
    if (btn_balloon == NULL) return;

    lv_color_t color = lv_obj_get_style_bg_color(btn_balloon, LV_PART_MAIN);

    lv_obj_remove_flag(btn_balloon, LV_OBJ_FLAG_CLICKABLE);
    lv_obj_set_style_bg_opa(btn_balloon, LV_OPA_TRANSP, LV_PART_MAIN);
    lv_obj_set_style_border_width(btn_balloon, 3, LV_PART_MAIN);
    lv_obj_set_style_border_color(btn_balloon, color, LV_PART_MAIN);
    lv_obj_set_style_radius(btn_balloon, 0, LV_PART_MAIN);
    uint32_t child_cnt = lv_obj_get_child_count(btn_balloon);
    for(uint32_t i = 0; i < child_cnt; i++) {
        lv_obj_t * child = lv_obj_get_child(btn_balloon, i);
        lv_obj_add_flag(child, LV_OBJ_FLAG_HIDDEN);
    }
    int32_t final_w = lv_obj_get_width(btn_balloon);
    lv_obj_set_size(btn_balloon, final_w, 12); 
    lv_obj_delete_delayed(btn_balloon, 220); 
    
}


void trigger_balloon_pop(lv_obj_t * balloon) {
    if (balloon == NULL) return;
    int32_t start_width = lv_obj_get_width(balloon);
    int32_t start_height = lv_obj_get_height(balloon);

    lv_anim_t a_width;
    lv_anim_init(&a_width);
    lv_anim_set_var(&a_width, balloon);
    lv_anim_set_values(&a_width, start_width, (int32_t)(start_width * 2.0));
    lv_anim_set_duration(&a_width, 150);
    lv_anim_set_exec_cb(&a_width, (lv_anim_exec_xcb_t)lv_obj_set_width);
    lv_anim_set_ready_cb(&a_width, pop_anim_ready_cb); 
    lv_anim_start(&a_width);

    lv_anim_t a_height;
    lv_anim_init(&a_height);
    lv_anim_set_var(&a_height, balloon);
    lv_anim_set_values(&a_height, start_height, (int32_t)(start_height * 1.5));
    lv_anim_set_duration(&a_height, 150);
    lv_anim_set_exec_cb(&a_height, (lv_anim_exec_xcb_t)lv_obj_set_height);
    lv_anim_start(&a_height);
}


void item_cb(lv_event_t * e)
{
    lv_event_code_t event_code = lv_event_get_code(e);
    
    if (event_code == LV_EVENT_CLICKED) {
        lv_obj_t * btn = lv_event_get_target_obj(e); 
        lv_color_t color = lv_obj_get_style_bg_color(btn, LV_PART_MAIN);
        lv_obj_t * btn_lbl = lv_obj_get_child(btn, 0);
        if (btn_lbl != NULL) {
            const char * txt = lv_label_get_text(btn_lbl);
            trigger_balloon_pop(btn);
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
            int random_num = ( rand() % 30) + 25;
            int dice = ( rand() % 4);
            snprintf(buf, sizeof(buf), "%d", random_num);
            lv_obj_t * btn = lv_button_create(ui_cont_number);
            lv_obj_set_width(btn, random_num);
            lv_obj_set_height(btn, random_num);
            lv_obj_set_style_radius(btn, LV_RADIUS_CIRCLE, 0);
            switch (dice) {
                case 0:
                    color = BLUE;
                    bcolor = BLUE_BORDER;
                    blue_score += random_num;
                    break;
                case 1:
                    color = GREEN;
                    bcolor =  GREEN_BORDER;
                    green_score += random_num;
                    break;
                case 2:
                    color = RED;
                    bcolor = RED_BORDER;
                    red_score += random_num;
                    break;
                case 3:
                    color = YELLOW;
                    bcolor = YELLOW_BORDER;
                    yellow_score += random_num;
                    break;
            }
            grand_total += random_num;
            lv_obj_set_style_bg_color(btn, color, LV_PART_MAIN | LV_STATE_DEFAULT);
            lv_obj_set_style_border_color(btn, bcolor, LV_PART_MAIN | LV_STATE_DEFAULT);
            lv_obj_t * btn_lbl = lv_label_create(btn);
            lv_obj_center(btn_lbl);
            lv_label_set_text(btn_lbl, buf);
            lv_obj_set_style_text_color(btn_lbl, lv_color_black(), LV_PART_MAIN | LV_STATE_DEFAULT);

            lv_obj_update_layout(ui_cont_number);
            int32_t btn_right = lv_obj_get_x2(btn);
            int32_t container_right = lv_obj_get_x2(ui_cont_number) - lv_obj_get_style_pad_right(ui_cont_number, LV_PART_MAIN);
            if(btn_right > container_right) {
                /* The button overflowed! Delete it and stop the loop */
                lv_obj_delete(btn);
                break;
            }
            fill_count++;
            lv_obj_add_event_cb(btn, item_cb, LV_EVENT_CLICKED, NULL);

        }
        update_totals();
    }

}

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

void update_cb(lv_event_t * e)
{
    update_totals();
}

