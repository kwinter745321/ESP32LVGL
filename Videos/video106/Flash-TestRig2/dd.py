# ==============================================================================
# File:       display_driver.py
# Author:     KWServices
# Version:    2.0
# License:    MIT
# Platform:   ESP32-S3 N16R8
# Updated:    2025-09-05
# ==============================================================================

"""
Enhanced Display Driver Module for MicroPython Projects
Supports:
  - SPI TFT Displays (ST7735, ST7789, GC9A01, ILI9341, ST7796, ILI9488)
  - Multiple Touch Controllers (XPT2046, CST328, CST816, FT6X36)

Usage:
    import display_driver
"""

import lvgl as lv
# various display_type drivers are inline below
import machine
from machine import reset, Pin
import sys

print("Running LVGL %d.%d" % (lv.version_major(), lv.version_minor() )  )
# ================= Orientation Modes =================
PORTRAIT           = 0
LANDSCAPE          = 1
INV_PORTRAIT       = 2
INV_LANDSCAPE      = 3

DISPLAY_ROTATION   = PORTRAIT
# =============================================================================
# DISPLAY TYPE SELECTOR 
# =============================================================================
# type    touch      resolution     model        bgr    Comment
# st7735  resistive   (128,128)      "1.44"      False
# st7735  resistive   (128,160)      "greentab"  False
# st7735  resistive   (128,160)      "redtab"    False
# st7735  resistive   (128,160)      "blacktab"  False

# gc9a01  resistive   (240,240)      None        False

# st7789  resistive   (135,240)      "odd"       False
# st7789  resistive   (240,240)      "square"    False
# st7789  resistive   (240,280)      "280"       False
# st7789  resistive   (240,320)      "big"       False

# ili9341 resistive  (240,320)       None        False  2.4
# ili9341 resistive  (240,320)       "big"       False  2.8,3.2

# st7796  resistive  (320,480)       None        False  3.5,4.0
# st7796  capacitive (320,480)       None        False  3.5,4.0

# ili9488 resistive  (320,480)       None        False 16bit
# ili9488b resistive  (320,480)       None        False 18bit
# =============================================================================
# TOUCH TYPE SELECTOR 
# =============================================================================
# type    touch      
# xpt2046 resistive
# cst328  capacitive
# cst816  capacitive
# ft6x36  capacitive

DISPLAY_TYPE = "st7796"
DISPLAY_MODEL = None
DISPLAY_BGR = False
TOUCH_CNTR = "xpt2046"  #  None

print(f"DISPLAY type:[{DISPLAY_TYPE}] model:{DISPLAY_MODEL} bgr:{DISPLAY_BGR}")
# =============================================================================
# PIN CONFIGURATION CONSTANTS
# =============================================================================

# ================= SPI for Display Configuration =================
LCD_SCLK            = 4
LCD_MOSI            = 5
LCD_MISO            = 0
LCD_SPI_PORT        = 1    # -1 for SoftSPI
LCD_SPI_FREQ        = 40_000_000
# ================= Display Configuration =================
LCD_RST         = 2
LCD_DC          = 3
LCD_CS          = 1
# LED Backlight
LCD_BL          = 10  # -1 means you wired BL to VCC
print(f"LCD rst:{LCD_RST} dc:{LCD_DC} cs:{LCD_CS} Backlight:{LCD_BL}")

# ================= Touch Configuration ================
if TOUCH_CNTR == "xpt2046":
    # ================= SPI for Touch Resistive Configuration =================
    TCS_SCLK        = LCD_SCLK   
    TCS_MOSI        = LCD_MOSI
    TCS_MISO        = LCD_MISO
    TCS_CS          = 11
    TCS_SPI_PORT    = 1    # -1 for SoftSPI
    TCS_SPI_FREQ    = 2_000_000
else:  
    # ================= I2C for Touch Capacitive Configuration =================
    TCS_SDA         = 8   
    TCS_SCL         = 9
    TCS_RESET       = 6
    TCS_INT         = 7
    TCS_I2C_PORT    = -1   # -1 for SoftI2c
    TCS_I2C_FREQ    = 400_000

###################################################################################
####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#### Do not edit below
####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
###################################################################################

# =============================================================================
# SPI INITIALIZATION
# =============================================================================
def fix_st7796_rotation(rot):
    if rot == 0: fix = 1
    if rot == 1: fix = 0
    if rot == 2: fix = 3
    if rot == 3: fix = 2
    return fix

backlight = None
if LCD_BL > 0:
    backlight = Pin(LCD_BL, Pin.OUT)
    backlight.on()
    print(f"Turned on backlight at Pin:{LCD_BL}")

spi = None
if LCD_SPI_PORT > 0:
    from machine import SPI
    spi = SPI(1, baudrate=LCD_SPI_FREQ, sck=Pin(LCD_SCLK), mosi=Pin(LCD_MOSI), miso=Pin(LCD_MISO))
else:
    from machine import SoftSPI
    spi = SoftSPI(baudrate=LCD_SPI_FREQ, sck=Pin(LCD_SCLK), mosi=Pin(LCD_MOSI), miso=Pin(LCD_MISO))
print(spi)

disp = None
hold = None
    
if DISPLAY_TYPE.lower() in ["gc9a01", "ili9341", "st7796", "ili9488", "ili9488b"]:
    import ili9xxx
    import st77xx
    if DISPLAY_TYPE.lower() == "gc9a01":
        disp = ili9xxx.Gc9a01(
            spi=spi, dc=LCD_DC, cs=LCD_CS, rst=LCD_RST,
            bl=LCD_BL, rot=DISPLAY_ROTATION,
        )
    if DISPLAY_TYPE.lower() == "ili9341":
        print("set d-type: ili9341")
        disp = ili9xxx.Ili9341(
            spi=spi, dc=LCD_DC, cs=LCD_CS, rst=LCD_RST,
            bl=LCD_BL, rot=DISPLAY_ROTATION, 
        )
        if DISPLAY_MODEL:
            disp.set_model(DISPLAY_MODEL)

    if DISPLAY_TYPE.lower() == "st7796":
        fix = fix_st7796_rotation(DISPLAY_ROTATION)
        disp = ili9xxx.St7796(
            spi=spi, dc=LCD_DC, cs=LCD_CS, rst=LCD_RST,
            bl=LCD_BL, rot=fix
        )
    if DISPLAY_TYPE.lower() == "ili9488":
        disp = ili9xxx.Ili9488(
            spi=spi, dc=LCD_DC, cs=LCD_CS, rst=LCD_RST,
            bl=LCD_BL, rot=DISPLAY_ROTATION
        )
        
    if DISPLAY_TYPE.lower() == "ili9488b":
        print("here",DISPLAY_TYPE)
        disp = ili9xxx.Ili9488b(
            spi=spi, dc=LCD_DC, cs=LCD_CS, rst=LCD_RST,
            bl=LCD_BL, rot=DISPLAY_ROTATION
        )

if DISPLAY_TYPE.lower() in ["st7735", "st7789"]:
    import st77xx
    # resolution = (240,240)
    # if DISPLAY_MODEL.lower() == "big":
    #     resolution = (240,320)

    if DISPLAY_TYPE.lower() == "st7735":
        disp = st77xx.St7735(
            spi=spi, dc=LCD_DC, cs=LCD_CS, rst=LCD_RST,
            bl=LCD_BL, rot=DISPLAY_ROTATION, res=(240,240), model=DISPLAY_MODEL
        )
    
    if DISPLAY_TYPE.lower() == "st7789":
        disp = st77xx.St7789(
            spi=spi, dc=LCD_DC, cs=LCD_CS, rst=LCD_RST,
            bl=LCD_BL, rot=DISPLAY_ROTATION, res=(240,240), model=DISPLAY_MODEL
        )

if disp == None:
    print(f"✗ Here's the display_type that failed: {DISPLAY_TYPE}")
    sys.exit()

# Verify
hres, vres = disp.width, disp.height
WIDTH=min(hres,vres)
HEIGHT=max(hres,vres)
print(f"Portrait mode width:{WIDTH} height:{HEIGHT}")
print(f"✓ SPI Display: {disp.display_type }, Current Resolution: {hres}x{vres}, Rotation: {disp.rot}")

# Create LVGL display driver
disp_drv = lv.display_create(hres, vres)
scr = lv.screen_active()
scr.set_style_bg_color(lv.color_hex(0x0),lv.PART.MAIN)    
# =============================================================================
# TOUCHSCREEN INITIALIZATION 
# =============================================================================

tspi = None
ti2c = None
touch = None

if TOUCH_CNTR == "xpt2046":
    print("Touchscreen using resistive touch")
    from xpt2046 import Xpt2046_hw
    if TCS_SPI_PORT >= 0:
        from machine import SPI
        tspi = SPI(1, baudrate=TCS_SPI_FREQ, sck=Pin(TCS_SCLK), mosi=Pin(TCS_MOSI), miso=Pin(TCS_MISO))
    else:
        from machine import SoftSPI
        tspi = SoftSPI(baudrate=TCS_SPI_FREQ, sck=Pin(LCD_SCLK), mosi=Pin(LCD_MOSI), miso=Pin(LCD_MISO))
    print(tspi)
    
    touch = Xpt2046_hw( spi=tspi, cs=TCS_CS, width=hres, height=vres, rot=disp.rot)
    print("Touch device configured for xpt2046:",touch)
    
    if touch:
        print("✓ XPT2046 Touchscreen initialized")
        print("Touch using pin:",TCS_CS,"rot:",disp.rot)
    else:
        print(f"✗ XPT2046 touchscreen failed")

if TOUCH_CNTR == "cst816":
    print("Touchscreen using capacitive touch")
    from cst816 import Touch_CST816S
    from machine import I2C
    if TCS_I2C_PORT >= 0:
        from machine import I2C
        i2c = I2C(TCS_I2C_PORT, scl=Pin(TCS_SCL), sda=Pin(TCS_SDA), freq=TCS_I2C_FREQ, timeout= 1000)
    else:
        from machine import SoftI2C
        i2c = SoftI2C(scl = Pin(TCS_SCL), sda=Pin(TCS_SDA), freq=TCS_I2C_FREQ, timeout= 1000)
    print(i2c)
    
    touch = Touch_CST816S(i2c=i2c,int_pin=TCS_INT,rst_pin=TCS_RESET)
    print("Touch device configured:",touch)

    if touch:
        print("✓ CST816S Touchscreen initialized")
        print(f"Touch using INT pin:{TCS_INT} Reset pin: {TCS_RESET} rot:{disp.rot}")
    else:
        print(f"✗ CST816S touchscreen failed")
# =============================================================================
# TRANSFORMATION
# =============================================================================
coords = None
dim = (hres,vres)

def scale(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# def transformGCA901(coords,rot):



@micropython.native
def transform9488(coords,rot):
    if coords != None:
        x,y = coords
        if rot == 0:
            x = disp.width - x - 1
            y = disp.height - y - 1
        if rot == 1:
            y = disp.height - y - 1
        if rot == 2:
            x = disp.width - x - 1
            y = disp.height - y - 1
        if rot == 3:
            y = disp.height - y - 1
        coords = (x,y)
    return coords

@micropython.native
def transform9341(p,rot):
    x, y = p
    if   rot==0: coords = x,dim[1]-y-1       
    elif rot==1: coords = x,y      
    elif rot==2: coords = x,dim[1]-y-1 
    else:        coords = x,y
    return coords

@micropython.native
def transform9341big(p,rot):
    x, y = p
    if   rot==0: coords = dim[0]-x,dim[1]-y     
    elif rot==1: coords = x,dim[1]-y     
    elif rot==2: coords = dim[0]-x,dim[1]-y 
    else:        coords = x,dim[1]-y
    #print(x,y,coords)
    return coords

@micropython.native
def transform7796(p,rot):
    x, y = p
    if   rot==0: coords = dim[0]-y,x            
    elif rot==1: coords = y,x
    elif rot==2: coords = dim[0]-y,x         
    else:        coords = y,x       
    return coords



# @micropython.native
# def transform(x, y, rotation):
#     """
#     Transform raw touchscreen coordinates (x, y) from the native portrait 
#     orientation to match the current display rotation.
# 
#     Args:
#         x (int): Raw X coordinate (0 to WIDTH-1)
#         y (int): Raw Y coordinate (0 to HEIGHT-1)
#         rotation (int): 0=Portrait, 1=Landscape, 2=Inv_Portrait, 3=Inv_Landscape
# 
#     Returns:
#         tuple: (new_x, new_y) transformed coordinates
#     """
#     if rotation == 0:        # PORTRAIT (0 degrees)
#         # No change needed
#         return (x, HEIGHT - 1 - y)
# 
#     elif rotation == 1:      # LANDSCAPE (90 degrees Clockwise)
#         # New width becomes old height, new height becomes old width
#         return (x,y)
# 
#     elif rotation == 2:      # INV_PORTRAIT (180 degrees)
#         # Rotate 180
#         return (x, HEIGHT - 1 - y)
# 
#     elif rotation == 3:      # INV_LANDSCAPE (270 degrees Clockwise)
#         # New width becomes old height, new height becomes old width
#         return (x,y)
# 
# @micropython.native
# def mirror_y(x,y,enable):
#     if enable == False:
#         return x,y
#     else:
#         if disp.rot == 0 or disp.rot == 2:
#             y = HEIGHT - y - 1
#         else:
#             y = WIDTH - y - 1
#     return x,y
# 
# #@micropython.native
# def mirror_x(x,y,enable):
#     if enable == False:
#         return x,y
#     else:
#         if disp.rot == 0 or disp.rot == 2:
#             x = WIDTH - x - 1
#         else:
#             x = HEIGHT - x - 1
#     return x,y
# 
# #@micropython.native
# def swap_xy(x,y,enable):
#     if enable == False:
#         return x,y
#     else:
#         return y,x

# =============================================================================
# TOUCH EVENT CALLBACK 
# =============================================================================
    
@micropython.native
def tsread(indev_drv, data) -> int:
    global coords
    data.state = 0
    hold = ""
    #######################################################
    if TOUCH_CNTR == "xpt2046":
        #### Resistive touch
        if touch == None:
            print("No touch ")
            return
        coords = touch.pos()
        if coords:
            hold = "non"
            x, y = coords 
            if disp.display_type == "st7796":
                hold = "st7796"
                coords = transform7796((x,y),disp.rot)
            elif disp.display_type in ["ili9488","ili9488b"]:
                hold = "ili9488x"
                coords = transform9488(coords, disp.rot)
            elif disp.display_type == "ili9341":
                hold = "ili9341"
                if disp.model == "big":
                    print("big ")
                    coords = transform9341big(coords,disp.rot)
                else:
                    print("2.4inch ")
                    coords = transform9341((x,y),disp.rot)
            # continue
            x,y = coords
            print(f"disp:{hold} model:{disp.model} rot:{disp.rot} x:{x} y:{y}")
            data.point.x = x
            data.point.y = y
            data.state = lv.INDEV_STATE.PRESSED
            return True
        else:
            data.state = lv.INDEV_STATE.RELEASED
            return False

    ###########################################################
    if TOUCH_CNTR != "xpt2046":
        #### Capacitive touch
        if touch.state == True:
            touch.state = False  #reset touch state
            touch.get_point()
            coords =  (touch.X_point,touch.Y_point)
            if coords != None:
                x,y = coords
                if disp.rot == LANDSCAPE:
                    y,x = coords
                    y = disp.height - y - 1
                if disp.rot == INV_PORTRAIT:
                    x = disp.width - x - 1
                    y = disp.height - y - 1
                if disp.rot == INV_LANDSCAPE:
                    y,x = coords
                    x = disp.width - x - 1
                coords = (x,y)
            # continue
            x,y = coords
            print(f"disp:{hold} model:{disp.model} rot:{disp.rot} x:{x} y:{y}")
            data.point.x = x
            data.point.y = y
            data.state = lv.INDEV_STATE.PRESSED
            return True
        else:
            data.state = lv.INDEV_STATE.RELEASED
            return False
############################################################
            # x,y = transform(x,y, 0)
            # mirror_y(x,y,True)
            # x,y = mirror_x(x,y,False)
            # x,y = swap_xy(x,y,False)
            # if disp.rot == 1 or disp.rot == 3:
            #     x = scale(x, 0, ht, 0, wd)
            #     y = scale(y, 0, wd, 0, ht)
#################################################################

            
#     except Exception as e:
#         print(f"Touch read error: {e}")
#         data.state = lv.INDEV_STATE.RELEASED
#         return False



indev_drv = lv.indev_create()
indev_drv.set_type(lv.INDEV_TYPE.POINTER)
indev_drv.set_read_cb(tsread)


# =============================================================================
# END OF MODULE
# =============================================================================
#if __name__ == "__main__":
print("end")