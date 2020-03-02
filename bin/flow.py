import RPi.GPIO as GPIO
import time



class Flow:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(27, GPIO.IN)
        global rev_count
        rev_count = 0
        GPIO.add_event_detect(27, GPIO.RISING, callback=self.increase_rev)

    def increase_rev(self,channel):
        global rev_count
        rev_count +=1

    
    def get_value(self):
        global rev_count
        time.sleep(0.25)
        print("We are at ", rev_count)
        value = rev_count
        rev_count = 0
        return value


#flow = Flow()
#while True:
#    flow.get_value()
