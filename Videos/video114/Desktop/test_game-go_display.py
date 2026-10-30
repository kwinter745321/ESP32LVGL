# test_game-go_display.py
#
# Created: 29 October 2026
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.29.0-dirty on 2026-10-24;
# Raspberry Pi Pico 2 W with RP2350
# LVGL 9.6
#
import lvgl as lv
from machine import reset, Pin
#from display_driver import disp, touch, backlight
from dd import disp, touch, backlight
import gc
import time

#### Game Configuration ###################
BOARD_SIZE = 9
CELL_SIZE = 34 
BOARD_DIM = BOARD_SIZE * CELL_SIZE
BLACK = 1
WHITE = 2
EMPTY = 0
turn_lbl = None
actions = None
MAX_ACTIONS = 4
SCORE_BLACK = 0
SCORE_WHITE = 0

# Game State
board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
current_turn = BLACK
# To keep track of the actual LVGL stone objects
stones = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def set_turn(turn):
    if turn == BLACK:
        turn_lbl.set_text("BLACK")
    else:
        turn_lbl.set_text("WHITE")

def add_action(text):
    item = lv.label(actions)
    item.set_size(100,20)
    item.set_style_text_color(lv.color_black(),0)
    item.set_style_text_font(lv.font_montserrat_16,0)
    item.set_text(text)
    count = actions.get_child_count()
    if count> MAX_ACTIONS:
        obj = actions.get_child(0)
        obj.delete()

def capture_count(stone):
    global SCORE_BLACK, SCORE_WHITE
    lbl = stone.get_child(0)
    txt = lbl.get_text()
    if txt == "b":
        SCORE_WHITE += 1
        lbl_white.set_text("White: "+str(SCORE_WHITE))
    else:
        SCORE_BLACK += 1
        lbl_black.set_text("Black: "+str(SCORE_BLACK))
    start=gc.mem_free()
    gc.collect()
    end=gc.mem_free()
    print(f"After stone capture:{end} Difference:{start-end}")
    return txt

def get_group(r, c, color):
    stack = [(r, c)]
    group = set([(r, c)])
    while stack:
        curr_r, curr_c = stack.pop()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE:
                if board[nr][nc] == color and (nr, nc) not in group:
                    group.add((nr, nc))
                    stack.append((nr, nc))
    return group

def get_liberties(group):
    liberties = set()
    for r, c in group:
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE:
                if board[nr][nc] == EMPTY:
                    liberties.add((nr, nc))
    return liberties

def handle_touch(r, c):
    global current_turn
    #print(f"handle: column:{c} row:{r}")
    if board[r][c] != EMPTY:
        return 

    board[r][c] = current_turn
    captured_any = False
    opponent = 3 - current_turn
    
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE and board[nr][nc] == opponent:
            group = get_group(nr, nc, opponent)
            if not get_liberties(group):
                count = 0
                for gr, gc in group:
                    board[gr][gc] = EMPTY
                    # Remove the stone object
                    if stones[gr][gc]:
                        count += 1
                        color = capture_count(stones[gr][gc])
                        stones[gr][gc].delete()
                        stones[gr][gc] = None
                captured_any = True
                if color == "b":
                    add_action(f"Got: {count} Black")
                else:
                    add_action(f"Got: {count} White")

    if not captured_any:
        my_group = get_group(r, c, current_turn)
        if not get_liberties(my_group):
            board[r][c] = EMPTY 
            return 

    # Update turn 
    current_turn = opponent
    set_turn(current_turn)
    # Create the UI stone
    color = lv.color_hex(0x000000) if board[r][c] == BLACK else lv.color_hex(0xffffff)
    stone_obj = lv.button(board_container) # Create a container for the stone
    stone_obj.set_size(CELL_SIZE - 8, CELL_SIZE - 8)
    stone_obj.set_style_bg_color(color, 0)
    stone_obj.set_style_radius(lv.RADIUS_CIRCLE, 0)
    stone_obj.set_style_bg_opa(lv.OPA.COVER, 0)
    stone_obj.set_style_border_width(1,0)
    stone_lbl = lv.label(stone_obj)
    if board[r][c] == BLACK:
        stone_lbl.set_text("b")
        stone_lbl.set_style_text_color(lv.color_black(),0)
        stone_obj.set_style_border_color(lv.color_black(),0)
    else:
        stone_lbl.set_text("w")
        stone_lbl.set_style_text_color(lv.color_white(),0)
        stone_obj.set_style_border_color(lv.color_white(),0)
    # Position the stone 
    stone_obj.set_pos((c*35)+2,(r*35)+2)
    stones[r][c] = stone_obj


#### Main Setup ##############################################
scr = lv.obj()
scr.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
lv.screen_load(scr)
turn_cont = lv.obj(scr)
turn_cont.set_size(140,50)
turn_cont.set_pos(10,0)
turn_cont.set_style_border_width(1,0)
turn_cont.set_style_border_color(lv.color_black(),0)
turn_cont.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
turn_lbl = lv.label(turn_cont)
turn_lbl.center()
turn_lbl.set_style_text_color(lv.palette_main(lv.PALETTE.RED),0)
turn_lbl.set_style_text_font(lv.font_montserrat_24, 0)
action_title = lv.label(scr)
action_title.set_pos(10,60)
action_title.set_style_text_color(lv.color_black(),0)
action_title.set_style_text_font(lv.font_montserrat_16, 0)
action_title.set_text("Actions:")
actions = lv.obj(scr)
actions.set_size(140,130)
actions.set_pos(10, 90)
actions.set_style_pad_all(5,0)
actions.set_style_border_width(1,0)
actions.set_style_border_color(lv.color_black(),0)
actions.set_flex_flow(lv.FLEX_FLOW.COLUMN)
add_action("Black starts")
set_turn(current_turn)
score_cont = lv.obj(scr)
score_cont.set_size(140,80)
score_cont.set_pos(10,230)
score_cont.set_flex_flow(lv.FLEX_FLOW.COLUMN)
lbl_black = lv.label(score_cont)
lbl_black.set_style_text_color(lv.color_black(),0)
lbl_black.set_style_text_font(lv.font_montserrat_24, 0)
lbl_black.set_text("Black: 0")
lbl_white = lv.label(score_cont)
lbl_white.set_style_text_color(lv.color_black(),0)
lbl_white.set_style_text_font(lv.font_montserrat_24, 0)
lbl_white.set_text("White: 0")
board_container = lv.obj(scr)
board_container.set_size(315, 315)
#board_container.set_style_bg_color(lv.color_hex(0x808080), 0) # Wood color
board_container.set_style_bg_color(lv.color_hex(0xffffff), 0) # Wood color
board_container.set_pos(160,0)
board_container.set_style_pad_all(0,0)
board_container.set_style_bg_color(lv.color_hex(0x808080),0)
board_container.set_style_border_color(lv.color_hex(0x1F51FF),0)
board_container.set_style_border_width(2,0)

def btn_cb(event):
    obj = event.get_target_obj()
    child = obj.get_child(0)
    txt = child.get_text()
    sx,sy = txt.split(',')
    c = int(sx)
    r = int(sy)
    handle_touch(r,c)
    gc.collect()

# display board
for j in range(0,BOARD_SIZE):
    for i in range(0,BOARD_SIZE):
        btn = lv.button(board_container)
        btn.set_size(30,30)
        btn.set_style_radius(lv.RADIUS_CIRCLE, 0)
        btn.set_pos( i*35, j*35 )
        btn.set_style_bg_color(lv.color_hex(0x39FF14), 0)
        lbl_btn = lv.label(btn)
        txt = str(i)+","+str(j)
        lbl_btn.set_text(txt)
        lbl_btn.set_style_text_color(lv.color_hex(0x39FF14), 0)
        lbl_btn.set_style_text_opa(lv.OPA.TRANSP, 0)
        lbl_btn.set_style_text_font(lv.font_montserrat_14,0)
        btn.set_style_border_width(2,0)
        btn.set_style_border_color(lv.color_hex(0x39FF14), 0)
        btn.set_style_border_color(lv.color_black(), 0)
        btn.add_event_cb(btn_cb, lv.EVENT.PRESSED, None)




