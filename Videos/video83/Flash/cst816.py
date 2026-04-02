# Modified: 23 March 2026
# Modified By: KW Services 2026
# Verified on:
# Waveshare 1.28inch Round Touch LCD
# MicroPython v1.27.0 on 2026-03-01;
# Raspberry Pi Pico W with RP2040
# Raspberry Pi Pico 2 W with RP2350

from machine import Pin,I2C,SPI,PWM,Timer
from machine import reset, SoftI2C
#import framebuf
import time


#Pin definition  引脚定义
# I2C_SDA = 6
# I2C_SCL = 7
# I2C_INT = 17
# I2C_RST = 16
 
 

#Touch drive  触摸驱动
class Touch_CST816S(object):
    #Initialize the touch chip  初始化触摸芯片
    def __init__(self,address=0x15,mode=1,i2c=None,int_pin=None,rst_pin=None):
        #print("I2C pins SDA:%d SCL:%d " % (I2C_SDA,I2C_SCL))
        print("I2C pins Interrupt:%d Reset:%d " % (int_pin,rst_pin))
        #self._bus = I2C(id=i2c_num,scl=Pin(i2c_scl),sda=Pin(i2c_sda),freq=400_000) #Initialize I2C 初始化I2C
        self._bus = i2c   #SoftI2C(scl=Pin(i2c_scl),sda=Pin(i2c_sda),freq=100_000) #Initialize I2C 初始化I2C
        print(self._bus)
        self._address = address #Set slave address  设置从机地址
        self.int=Pin(int_pin,Pin.IN, Pin.PULL_UP)     
        #self.tim = Timer()     
        self.rst=Pin(rst_pin,Pin.OUT)
        self.Reset()
        self.Reset()
        self.state = False
        devices = self._bus.scan()
        print("I2C devices found:", devices)
        bRet=self.WhoAmI()
        if bRet :
            print("Success:Detected CST816S.")
            Rev= self.Read_Revision()
            print("CST816S Revision = {}".format(Rev))
            self.Stop_Sleep()
        else    :
            print("Error: Not Detected CST816S.")
            return None
        self.Mode = mode
        self.Gestures="None"
        self.Flag = self.Flgh =self.l = 0
        self.X_point = self.Y_point = 0
        self.int.irq(handler=self.Int_Callback,trigger=Pin.IRQ_FALLING)
      
    def _read_byte(self,cmd):
        rec=self._bus.readfrom_mem(int(self._address),int(cmd),1)
        return rec[0]
    
    def _read_block(self, reg, length=1):
        rec=self._bus.readfrom_mem(int(self._address),int(reg),length)
        return rec
    
    def _write_byte(self,cmd,val):
        self._bus.writeto_mem(int(self._address),int(cmd),bytes([int(val)]))

    def WhoAmI(self):
        if (0xB5) != self._read_byte(0xA7):
            return False
        return True
    
    def Read_Revision(self):
        return self._read_byte(0xA9)
      
    #Stop sleeping  停止睡眠
    def Stop_Sleep(self):
        self._write_byte(0xFE,0x01)
    
    #Reset  复位    
    def Reset(self):
        self.rst(0)
        time.sleep_ms(1)
        self.rst(1)
        time.sleep_ms(50)
    
    #Set mode  设置模式   
    def Set_Mode(self,mode,callback_time=10,rest_time=5): 
        # mode = 0 gestures mode 
        # mode = 1 point mode 
        # mode = 2 mixed mode 
        if (mode == 1):      
            self._write_byte(0xFA,0X41)
            
        elif (mode == 2) :
            self._write_byte(0xFA,0X71)
            
        else:
            self._write_byte(0xFA,0X11)
            self._write_byte(0xEC,0X01)
     
    #Get the coordinates of the touch  获取触摸的坐标
    def get_point(self):
        if self.Flag == 1:
            self.mode = 2
            self.Flag = 0
            time.sleep_ms(150)
            try:
                xy_point = self._read_block(0x03,4)
                x_point= ((xy_point[0]&0x0f)<<8)+xy_point[1]
                y_point= ((xy_point[2]&0x0f)<<8)+xy_point[3]
                self.X_point=x_point
                self.Y_point=y_point
                #print("loc: x,y",x_point,y_point)
            except:
                pass
        self.mode = 1

    
    def show_point(self):
        self.get_point()
        coords = (self.X_point, self.Y_point)
        print(coords)

            
    def Int_Callback(self,pin):
        #print("touched")
        if self.Mode == 0 :
            self.Gestures = self._read_byte(0x01)

        elif self.Mode == 1:           
            self.Flag = 1
            self.state = True
            #self.get_point()

    def Timer_callback(self,t):
        self.l += 1
        if self.l > 100:
            self.l = 50
######    
#####  Touch=Touch_CST816S(mode=1)