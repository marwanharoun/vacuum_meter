#!/usr/bin/python3
from hx711 import HX711
import RPi.GPIO as GPIO



class LoadCell:
    def __init__(self):
        self.dout_pin=5
        self.pd_sck_pin=6
        self.channel='A'
        self.gain=64
        try:
            #self.hx711 = HX711(self.dout_pin,self.pd_sck_pin,self.channel,self.gain)
            self.hx711 = HX711(5,6,64,'A')
            #self.hx711.reset()   # Before we start, reset the HX711 (not obligate)
        finally:
            GPIO.cleanup()  # always do a GPIO cleanup in your scripts!



    def get_value(self):
        while (True):
            measures = self.hx711.get_raw_data(3)
            print(measures)


test = LoadCell()
test.get_value()
