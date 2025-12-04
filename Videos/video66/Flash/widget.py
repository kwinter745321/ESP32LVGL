import lvgl as lv
from machine import Pin
from display_driver import disp
import time

#### Convert PNG mage file to binary #######################
class ConvertPNG:
# """
#     Returns binary image by reading a PNG file
# 
#     Parameters:
#         filename (str): Name of PNG file
#         debug (str): Keyword like 'verbose' default: None
# 
#     Returns:
#         image: Binary image (suitable for LVGL widgets)
# """

    def __init__(self, filename, debug=None):
        self.filename = filename
        self.debug = debug
        self.dsc = None
        self.convert()
    
    def get_image_data(self, filename):
        with open(filename, 'rb') as f:
            imgdata = f.read()
        return imgdata
        
    def create_img_dsc(self, imgdata):
        imgdsc = lv.image_dsc_t({'data_size':len(imgdata), 'data':imgdata})
        return imgdsc
    
    def convert(self):
        image_data = self.get_image_data(self.filename)
        image_data_mv = memoryview(image_data)
        self.dsc = self.create_img_dsc(image_data_mv)
        if self.debug != None:
            size = len(image_data)
            print("Converted {}  {} Bytes".format(self.filename, size))
        return self.dsc
    
    def __str__(self):
        return "Binary data for: " + self.filename

#### Convert PNG mage file to binary #######################
class GaugeSlider:
# """
#     Returns custom widget of a slider and scale
# 
#     Parameters:
#         parent (obj): Parent display object [e.g. scr=lv.obj() ]
#         label (obj): LVGL label (for slider value) default None
#         arrow (image): Image for slider's knob
#         x (int): X coordinate on screen default: 0
#         y (int): Y coordinate on screen default: 0 'center'
#         dark (bool): Screen backgound color is dark  default=False
# 
#     Returns:
#         str: Binary image (suitable for LVGL widgets)
# """    

    def __init__(self,parent,image,label=None,x=0,y=0,dark=False):
        self.scr = parent
        self.arrow = image
        self.label = label
        self.text = ""
        self.dark = dark
        self.cont = lv.obj(self.scr)
        self.cont.set_size(lv.pct(90), 70)
        if self.dark:
            self.cont.set_style_bg_color(lv.color_white(), lv.PART.MAIN)
            self.cont.set_style_border_color(lv.color_white(), lv.PART.MAIN)
        else:
            self.cont.set_style_bg_opa(lv.OPA.TRANSP, lv.PART.MAIN)
            self.cont.set_style_border_color(lv.color_black(), lv.PART.MAIN)
        self.cont.set_style_border_width(2, lv.PART.MAIN)
        #self.cont.set_style_bg_opa(lv.OPA.TRANSP, lv.PART.MAIN)
        if y == 0:
            self.cont.center()
        else:
            self.cont.set_pos(x,y)

#### Slider ###############################
        self.slider = lv.slider(self.cont)
        self.slider.set_size(230,10)
        self.slider.align(lv.ALIGN.CENTER, 0, -20)
        self.slider.set_style_bg_opa(lv.OPA.TRANSP, lv.PART.MAIN)

        scale = lv.scale(self.cont)
        scale.align_to(self.slider, lv.ALIGN.OUT_BOTTOM_LEFT, 0, 15)
        scale.set_width(self.slider.get_width())
        scale.set_range(0,100)
        scale.set_total_tick_count(26)
        scale.set_major_tick_every(5)
        scale.set_style_line_width(0, lv.PART.MAIN)
        scale.set_style_line_width(1, lv.PART.ITEMS)
        scale.set_style_line_width(3, lv.PART.INDICATOR)
        scale.set_style_length(5, lv.PART.ITEMS)
        scale.set_style_length(9, lv.PART.INDICATOR)
        scale.set_mode(lv.scale.MODE.HORIZONTAL_BOTTOM)
#         scale.set_style_bg_color(lv.color_white(),0)
#         scale.set_style_text_color(lv.color_white(),0)
#         scale.set_style_line_color(lv.color_white(),lv.PART.INDICATOR)
#         scale.set_style_line_color(lv.color_white(),lv.PART.ITEMS)

        knob_style = lv.style_t()
        knob_style.init()
        knob_style.set_bg_image_src(self.arrow)
        knob_style.set_bg_opa(lv.OPA.TRANSP)

#### Add the style to slider knob part #########
        self.slider.add_style(knob_style, lv.PART.KNOB)
        self.slider.set_style_pad_all(16, lv.PART.KNOB)
        self.slider.set_style_bg_opa(lv.OPA.TRANSP, lv.PART.KNOB)
        self.slider.set_style_border_width(0, lv.PART.KNOB)
        self.slider.set_style_border_width(1, lv.PART.MAIN)
        #self.slider.set_style_border_color(lv.color_white(),lv.PART.MAIN)
        self.slider.add_event_cb(self.slider_cb, lv.EVENT.VALUE_CHANGED, None)
        self.cont.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
        
    def set_text(self, text):
        self.text = text
        
    def _update(self):
        if self.label != None:
            self.label.set_text("{}{}".format( self.text, self.slider.get_value() ) )
        else:
            self.label.set_text("{}".format( self.slider.get_value() ) )       

    def set_value(self, current=50):
        self.slider.set_value(current, lv.PART.MAIN)
        self._update()

    def get_value(self):
        return self.slider.get_value()
        
    def slider_cb(self, event):
        self._update()

class ImageButton():
# """
#     Returns Displays image at x,y location of parent
# 
#     Parameters:
#         parent (obj): Parent display object [e.g. scr=lv.obj() ]
#         image (image): Image for the button
#         width (int): Image width        default: 16 pixels
#         height (int): Image height      default: 16 pixels
#         x (int): X coordinate on screen default: 0
#         y (int): Y coordinate on screen default: 0 'center'
# 
#     Returns:
#         Displays image
# """

    def __init__(self,parent,image,width=16,height=16,x=0,y=0):
        self.image = image
        self.button = lv.button(parent)
        self.button.set_size(width,height)
        self.button.set_pos(x,y)
        if width == height:
            self.button.set_style_radius(width//2,lv.PART.MAIN)
        self.button.set_style_bg_opa(lv.OPA.TRANSP, lv.PART.MAIN)
        self.button.set_style_bg_image_src(self.image,lv.PART.MAIN) 

    def action(self, callback ):
        self.button.add_event_cb( callback, lv.EVENT.CLICKED, None)
    