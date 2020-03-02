import RPi.GPIO as GPIO
import time, sys


class FlowRate:
    global rate_cnt, tot_cnt
    rate_cnt = 0
    tot_cnt = 0

    def pulse_cnt(self, inpt_pin):
        global rate_cnt, tot_cnt
        rate_cnt += 1
        tot_cnt += 1


    def __init__(self):
        #GPIO.setmode(GPIO.BCM)
        inpt = 27
        GPIO.setup(inpt, GPIO.IN)
        GPIO.add_event_detect(inpt,GPIO.FALLING,callback=self.pulse_cnt,bouncetime=10)
        
    
    def get_value(self):
        constant = 0.006
        rpt_int = 0.25
        time_new = time.time()+rpt_int
        while time.time() <= time_new:
            try:
                None
            except KeyboardInterrupt:
                GPIO.cleanup()
                sys.exit()
        rate = round(((rate_cnt*constant)/(rpt_int/60)),2)
        tot = round(tot_cnt*constant,1)
        return rate

