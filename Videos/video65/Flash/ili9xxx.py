# ili9xxx.py
# Update 1.1: 08 May 2025 to support the four Orientation modes
# Update 1.2: 17 October to include GC9A01 driver
# Update 1.3: 21 November to merge driver updates
# Updated by: KWServices
#
"""Generic ILI9xxx drivers.

This code is licensed under MIT license.

Adapted from:
    https://github.com/rdagger/micropython-ili9341

The following code snippet will instantiate the driver and
automatically register it to lvgl. Adjust the SPI bus and
pin configurations to match your hardware setup::

    import ili9xxx
    from machine import SPI, Pin
    spi = SPI(0, baudrate=24_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
    drv = ili9xxx.Ili9341(spi=spi, dc=0, cs=17, rst=1)
"""
from micropython import const

import st77xx
import lvgl as lv
import time

# Command constants from ILI9341 datasheet
_NOP = const(0x00)  # No-op
_SWRESET = const(0x01)  # Software reset
_RDDID = const(0x04)  # Read display ID info
_RDDST = const(0x09)  # Read display status
_SLPIN = const(0x10)  # Enter sleep mode
_SLPOUT = const(0x11)  # Exit sleep mode
_PTLON = const(0x12)  # Partial mode on
_NORON = const(0x13)  # Normal display mode on
_RDMODE = const(0x0A)  # Read display power mode
_RDMADCTL = const(0x0B)  # Read display MADCTL
_RDPIXFMT = const(0x0C)  # Read display pixel format
_RDIMGFMT = const(0x0D)  # Read display image format
_RDSELFDIAG = const(0x0F)  # Read display self-diagnostic
_INVOFF = const(0x20)  # Display inversion off
_INVON = const(0x21)  # Display inversion on
_GAMMASET = const(0x26)  # Gamma set
_DISPLAY_OFF = const(0x28)  # Display off
_DISPLAY_ON = const(0x29)  # Display on
_SET_COLUMN = const(0x2A)  # Column address set
_SET_PAGE = const(0x2B)  # Page address set
_WRITE_RAM = const(0x2C)  # Memory write
_READ_RAM = const(0x2E)  # Memory read
_PTLAR = const(0x30)  # Partial area
_VSCRDEF = const(0x33)  # Vertical scrolling definition
_MADCTL = const(0x36)  # Memory access control
_VSCRSADD = const(0x37)  # Vertical scrolling start address
_PIXFMT = const(0x3A)  # COLMOD: Pixel format set
_WRITE_DISPLAY_BRIGHTNESS = const(0x51)  # Brightness hardware dependent!
_READ_DISPLAY_BRIGHTNESS = const(0x52)
_WRITE_CTRL_DISPLAY = const(0x53)
_READ_CTRL_DISPLAY = const(0x54)
_WRITE_CABC = const(0x55)  # Write Content Adaptive Brightness Control
_READ_CABC = const(0x56)  # Read Content Adaptive Brightness Control
_WRITE_CABC_MINIMUM = const(0x5E)  # Write CABC Minimum Brightness
_READ_CABC_MINIMUM = const(0x5F)  # Read CABC Minimum Brightness
_FRMCTR1 = const(0xB1)  # Frame rate control (In normal mode/full colors)
_FRMCTR2 = const(0xB2)  # Frame rate control (In idle mode/8 colors)
_FRMCTR3 = const(0xB3)  # Frame rate control (In partial mode/full colors)
_INVCTR = const(0xB4)  # Display inversion control
_DFUNCTR = const(0xB6)  # Display function control
_PWCTR1 = const(0xC0)  # Power control 1
_PWCTR2 = const(0xC1)  # Power control 2
_PWCTRA = const(0xCB)  # Power control A
_PWCTRB = const(0xCF)  # Power control B
_VMCTR1 = const(0xC5)  # VCOM control 1
_VMCTR2 = const(0xC7)  # VCOM control 2
_RDID1 = const(0xDA)  # Read ID 1
_RDID2 = const(0xDB)  # Read ID 2
_RDID3 = const(0xDC)  # Read ID 3
_RDID4 = const(0xDD)  # Read ID 4
_GMCTRP1 = const(0xE0)  # Positive gamma correction
_GMCTRN1 = const(0xE1)  # Negative gamma correction
_DTCA = const(0xE8)  # Driver timing control A
_DTCB = const(0xEA)  # Driver timing control B
_POSC = const(0xED)  # Power on sequence control
_ENABLE3G = const(0xF2)  # Enable 3 gamma control
_PUMPRC = const(0xF7)  # Pump ratio control

_MADCTL_MY = const(0x80)  # page address order (0: top to bottom; 1: bottom to top)
_MADCTL_MX = const(0x40)  # column address order (0: left to right; 1: right to left)
_MADCTL_MV = const(0x20)  # page/column order (0: normal mode 1; reverse mode)
_MADCTL_ML = const(0x10)  # line address order (0: refresh to to bottom; 1: refresh bottom to top)
_MADCTL_BGR = 0x08 # just a label  (0: RGB  1: BGR)  so BGR=false is 0x08
_MADCTL_RTL = const(0x04)  # refresh right to left

_MADCTL_ROTS = (
    const(_MADCTL_MX),  # 0 = portrait
    const(_MADCTL_MV),  # 1 = landscape
    const(_MADCTL_MY),  # 2 = inverted portrait
    const(_MADCTL_MX | _MADCTL_MY | _MADCTL_MV),  # 3 = inverted landscape
)

ILI9XXX_PORTRAIT = st77xx.ST77XX_PORTRAIT
ILI9XXX_LANDSCAPE = st77xx.ST77XX_LANDSCAPE
ILI9XXX_INV_PORTRAIT = st77xx.ST77XX_INV_PORTRAIT
ILI9XXX_INV_LANDSCAPE = st77xx.ST77XX_INV_LANDSCAPE

class Ili9341_hw(st77xx.St77xx_hw):
    def __init__(self, **kw):
        """ILI9341 TFT Display Driver."""
        print("ili9341 hw")
        self.display_type = "ili9341"
        super().__init__(
            res=(240,320),
            suppRes=[
                (240,320),
                (320,240),
            ],
            model=None,
            suppModel=None,
            bgr=False,
            **kw,
        )
        
    # Distinguish a display from another
    # None  = 2.4 inch ILI9341 Display
    # "big" = 2.8 or 3.2 inch ILI9341 Display
    def set_model(self, model):
        self.model = model

    def config_hw(self):
        self._run_seq(
            [
                (_SLPOUT, None, 100),
                (_PWCTRB, b"\x00\xC1\x30"),  # Pwr ctrl B
                (_POSC, b"\x64\x03\x12\x81"),  # Pwr on seq. ctrl
                (_DTCA, b"\x85\x00\x78"),  # Driver timing ctrl A
                (_PWCTRA, b"\x39\x2C\x00\x34\x02"),  # Pwr ctrl A
                (_PUMPRC, b"\x20"),  # Pump ratio control
                (_DTCB, b"\x00\x00"),  # Driver timing ctrl B
                (_PWCTR1, b"\x23"),  # Pwr ctrl 1
                (_PWCTR2, b"\x10"),  # Pwr ctrl 2
                (_VMCTR1, b"\x3E\x28"),  # VCOM ctrl 1
                (_VMCTR2, b"\x86"),  # VCOM ctrl 2
                (_VSCRSADD, b"\x00"),  # Vertical scrolling start address
                (_PIXFMT, b"\x55"),  # COLMOD: Pixel format
                (_FRMCTR1, b"\x00\x18"),  # Frame rate ctrl
                (_DFUNCTR, b"\x08\x82\x27"),
                (_ENABLE3G, b"\x00"),  # Enable 3 gamma ctrl
                (_GAMMASET, b"\x01"),  # Gamma curve selected
                (
                    _GMCTRP1,
                    b"\x0F\x31\x2B\x0C\x0E\x08\x4E\xF1\x37\x07\x10\x03\x0E\x09\x00",
                ),
                (
                    _GMCTRN1,
                    b"\x00\x0E\x14\x03\x11\x07\x31\xC1\x48\x08\x0F\x0C\x31\x36\x0F",
                ),
                (_SLPOUT, None, 100),
                (_DISPLAY_ON, None),
            ]
        )

    def apply_rotation(self, rot):
        self.rot = rot
        if (self.rot % 2) == 0:
            self.width, self.height = self.res
        else:
            self.height, self.width = self.res
        try:
            self.write_register(
                _MADCTL,
                bytes([_MADCTL_BGR | _MADCTL_ROTS[self.rot % 4]]),
            )
        except:
            print("exception in ili9xxx, _madctl:",_MADCTL)

class Ili9341(Ili9341_hw, st77xx.St77xx_lvgl):
    def __init__(self, doublebuffer=True, factor=4, **kw):
        """See :obj:`Ili9341_hw` for the meaning of the parameters."""
        Ili9341_hw.__init__(self, **kw)
        st77xx.St77xx_lvgl.__init__(self, doublebuffer, factor) 

        
class St7796_hw(st77xx.St77xx_hw):
    def __init__(self, **kw):
        """ST7796 TFT Display Driver."""
        self.display_type = "st7796"
        print("ST7796_hw")
        super().__init__(
            res=(320, 480),
            suppRes=[
                (320, 480),
                (480, 320),
            ],
            model=None,
            suppModel=None,
            bgr=False,
            **kw,
        )
        
    # Distinguish a display from another
    # None  = 4.0 inch ST7796 Display
    def set_model(self, model):
        self.model = model
    
    def config_hw(self):
        self._run_seq(
            [
                (_SLPOUT, None, 100),
                (_PWCTRB, b"\x00\xC1\x30"),  # Pwr ctrl B
                (_POSC, b"\x64\x03\x12\x81"),  # Pwr on seq. ctrl
                (_DTCA, b"\x85\x00\x78"),  # Driver timing ctrl A
                (_PWCTRA, b"\x39\x2C\x00\x34\x02"),  # Pwr ctrl A
                (_PUMPRC, b"\x20"),  # Pump ratio control
                (_DTCB, b"\x00\x00"),  # Driver timing ctrl B
                (_PWCTR1, b"\x23"),  # Pwr ctrl 1
                (_PWCTR2, b"\x10"),  # Pwr ctrl 2
                (_VMCTR1, b"\x3E\x28"),  # VCOM ctrl 1
                (_VMCTR2, b"\x86"),  # VCOM ctrl 2
                (_VSCRSADD, b"\x00"),  # Vertical scrolling start address
                (_PIXFMT, b"\x55"),  # COLMOD: Pixel format
                (_FRMCTR1, b"\x00\x18"),  # Frame rate ctrl
                (_DFUNCTR, b"\x08\x82\x27"),
                (_ENABLE3G, b"\x00"),  # Enable 3 gamma ctrl
                (_GAMMASET, b"\x01"),  # Gamma curve selected
                (0xB6, b"\x08\x22\x3B" ),   #Blanking Porch Control
                (
                    _GMCTRP1,
                    b"\xF0\x09\x0B\x06\x04\x15\x2F\x54\x42\x3C\x17\x14\x18\x1B",
                ),
                (
                    _GMCTRN1,
                    b"\xE0\x09\x0B\x06\x04\x03\x2B\x43\x42\x3B\x16\x14\x17\x1B",
                ),
                (_SLPOUT, None, 100),
                (_DISPLAY_ON, None),
            ]
        )
        
    

    def apply_rotation(self, rot):
        _MADCTL_BGR = 0x04
        #self.height, self.width = self.res
        self.rot = rot
        if (self.rot % 2) == 0:
            print("rot=0")
            #self.width, self.height = self.res
            self.height, self.width = self.res
        else:
            #self.height, self.width = self.res
            self.width, self.height = self.res
        #self.height, self.width = self.res
        try:
            self.write_register(
                _MADCTL,
                bytes([_MADCTL_BGR | _MADCTL_ROTS[self.rot % 4]]),
            )
        except:
            print("except in ili9xxx, _madctl:",_MADCTL)

class St7796(St7796_hw, st77xx.St77xx_lvgl):
    def __init__(self, doublebuffer=True, factor=8, **kw):
        """See :obj:`Ili9341_hw` for the meaning of the parameters."""
        ######_MADCTL_BGR must = 0x04  see apply _rotation()
        St7796_hw.__init__(self, **kw)
        st77xx.St77xx_lvgl.__init__(self, doublebuffer, factor)

        
class Gc9a01_hw(st77xx.St77xx_hw):
    def __init__(self, **kw):
        """GC9A01 TFT Display Driver."""
        self.display_type = "gc9a01"
        print("Gc9a01_hw")
        super().__init__(
            res=(240, 240),
            suppRes=[
                (240, 240),
                (240, 240),
            ],
            model=None,
            suppModel=None,
            bgr=False,
            **kw,
        )
        
    # Distinguish a display from another
    # None  = 1.28 GC9A01 Display
    def set_model(self, model):
        self.model = model
    
    def config_hw(self):
        self._run_seq(
            [
                (const(0x11) , None, 100), #SLPOUT
                ( const( 0xEF), b"\x00"),
                ( const( 0xEB), b"\x14"),
                ( const( 0xFE), b"\x00"),
                ( const( 0xEF), b"\x00"),
                ( const( 0xEB), b"\x14"),
                ( const( 0x84), b"\x40"),
                ( const( 0x85), b"\xFF"),
                ( const( 0x86), b"\xFF"),
                ( const( 0x87), b"\xFF"),
                ( const( 0x88), b"\x0A"),
                ( const( 0x89), b"\x21"),
                ( const( 0x8A), b"\x00"),
                ( const( 0x8B), b"\x80"),
                ( const( 0x8C), b"\x01"),
                ( const( 0x8D), b"\x01"),
                ( const( 0x8E), b"\xFF"),
                ( const( 0x8F), b"\xFF"),
                ( const( 0xB6), b"\x00\x00"), 
                ( const( 0x36), b"\x48"),
                ( const( self.rot), b"\x00"),
                ( const( 0x3A), b"\x05"),
                ( const( 0x90), b"\x08\x08\x08\x08"),
                ( const( 0xBD), b"\x06"),
                ( const( 0xBC), b"\x00"),
                ( const( 0xFF), b"\x60\x01\x04"),
                ( const( 0xC3), b"\x13"),
                ( const( 0xC4), b"\x13"),
                ( const( 0xC9), b"\x22"),
                ( const( 0xBE), b"\x11"),
                ( const( 0xE1), b"\x10\x0E"),
                ( const( 0xDF), b"\x21\x0c\x02"),
                ( const( 0xF0), b"\x45\x09\x08\x08\x26\x2A"),
                ( const( 0xF1), b"\x43\x70\x72\x36\x37\x6F"),
                ( const( 0xF2), b"\x45\x09\x08\x08\x26\x2A"),
                ( const( 0xF3), b"\x43\x70\x72\x36\x37\x6F"),
                ( const( 0xED), b"\x1B\x0B"),
                ( const( 0xAE), b"\x77"),
                ( const( 0xCD), b"\x63"),
                ( const( 0x70), b"\x07\x07\x04\x0E\x0F\x09\x07\x08\x03"),
                ( const( 0xE8), b"\x34"),
                ( const( 0x62), b"\x18\x0D\x71\xED\x70\x70\x18\x0F\x71\xEF\x70\x70"),
                ( const( 0x63), b"\x18\x11\x71\xF1\x70\x70\x18\x13\x71\xF3\x70\x70"),
                ( const( 0x64), b"\x28\x29\xF1\x01\xF1\x00\x07"),
                ( const( 0x66), b"\x3C\x00\xCD\x67\x45\x45\x10\x00\x00\x00"),
                ( const( 0x67), b"\x00\x3C\x00\x00\x00\x01\x54\x10\x32\x98"),
                ( const( 0x74), b"\x10\x85\x80\x00\x00\x4E\x00"),
                ( const( 0x98), b"\x3e\x07"),
                ( const( 0x35), b"\x00"),
                ( const( 0x21), b"\x00"),
                (const(0x11), None, 20),  #SLPOUT
                (const(0x29), None, 120),  #DISPLAY_ON
            ]
        )

    def apply_rotation(self, rot):
        self.rot = rot
        if (self.rot % 2) == 0:
            print("rot=0")
            self.height, self.width = self.res
        else:
            self.width, self.height = self.res
        try:
            self.write_register(
                _MADCTL,
                bytes([_MADCTL_BGR | _MADCTL_ROTS[self.rot % 4]]),
            )
        except:
            print("except in ili9xxx, _madctl:",_MADCTL)

class Gc9a01(Gc9a01_hw, st77xx.St77xx_lvgl):
    def __init__(self, doublebuffer=True, factor=8, **kw):
        """See :obj:`Gc9a01_hw` for the meaning of the parameters."""
        Gc9a01_hw.__init__(self, **kw)
        st77xx.St77xx_lvgl.__init__(self, doublebuffer, factor)
