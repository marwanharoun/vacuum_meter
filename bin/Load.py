#!/usr/bin/python3
from Hx711 import HX711
import RPi.GPIO as GPIO



class LoadCell:

    def __init__(self):
        DT = 5
        SCK = 6
        CHANNEL = 'B'
        GAIN = 64
        GPIO.setmode(GPIO.BCM) #keep that in Main.py only
        GPIO.setwarnings(False)
        self.hx711 = HX711(DT,SCK,GAIN,CHANNEL)
        self.hx711.reset()   # Before we start, reset the HX711 (not obligate)


    def return_calib(self,input):
        #A = 0.00488594648262289
        #B = -106.44773936296 + 155.787500483901 + 1012
        A = 0.009595
        B = 2134
        load = A*(input) + B
        return load

    def get_value(self):
        value = self.return_calib(self.hx711.get_weight_mean(1))
        return value
