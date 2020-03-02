import RPi.GPIO as GPIO
import time



class Flow:

    def __init__(self):
        CHANNEL = 27
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(CHANNEL, GPIO.IN)
        global rev_count
        rev_count = 0
        GPIO.add_event_detect(CHANNEL, GPIO.RISING, callback=self.increase_rev)

    def increase_rev(self,channel):
        global rev_count
        rev_count +=1

    
    def get_value(self):
        global rev_count
        value = rev_count
        rev_count = 0
        return value
