import RPi.GPIO as GPIO
import time



class Flow:

    def __init__(self):
        CHANNEL = 27
        GPIO.setmode(GPIO.BCM) #keep that in Main.py only
        GPIO.setup(CHANNEL, GPIO.IN)
        global rev_count
        rev_count = 0
        GPIO.add_event_detect(CHANNEL, GPIO.RISING, callback=self.increase_rev)

    def increase_rev(self,channel):
        global rev_count
        rev_count +=1

    def return_calib(input):
        A = 1
        B = 0
        output = A*input + B
        return output
    
    def get_value(self):
        global rev_count
        value = self.return_calib(rev_count)
        rev_count = 0
        return value
