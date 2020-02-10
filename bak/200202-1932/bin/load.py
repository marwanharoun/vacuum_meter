#!/usr/bin/python3
from hx711 import HX711
import RPi.GPIO as GPIO



class LoadCell:
    def __init__(self):
        DT = 5
        SCK = 6
        CHANNEL = 'A'
        GAIN = 64
        self.hx711 = HX711(DT,SCK,GAIN,CHANNEL)
        self.hx711.reset()   # Before we start, reset the HX711 (not obligate)




    # def get_value(self):
    #     #CALIBRATION CONSTANTS:
    #     A = 567/115000
    #     B = -2835/23
    #
    #     measures = self.hx711.get_raw_data(3)
    #     X = sum(measures)/len(measures)
    #     load = A*X + B
    #     print(load)
    #     return load



    def get_value(self):
        try:
            GPIO.setmode(GPIO.BCM)
            load = self.hx711.get_weight_mean(1)
            print(load)
            return load

        except (KeyboardInterrupt, SystemExit):
            print('Bye')
