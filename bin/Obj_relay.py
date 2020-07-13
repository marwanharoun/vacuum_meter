import time as t
import smbus
import sys




class Relay:

    def __init__(self, RELAY_NUM):
        self.DEVICE_BUS = 1
        self.DEVICE_ADDR = 0x10
        self.bus = smbus.SMBus(self.DEVICE_BUS)
        self.RELAY_NUM = RELAY_NUM
        
    def turn_on(self):
        self.bus.write_byte_data(self.DEVICE_ADDR, self.RELAY_NUM, 0xFF)
        print("Turning relay " + str(self.RELAY_NUM) + " ON")
    
    
    def turn_off(self):
        self.bus.write_byte_data(self.DEVICE_ADDR, self.RELAY_NUM, 0x00)
        print("Turning relay " + str(self.RELAY_NUM) + " OFF")
        
    def read(self):
        self.RESULT = self.bus.read_byte_data(self.DEVICE_ADDR, self.RELAY_NUM)
#        print("Result: " + str(self.RESULT))
        return self.RESULT

