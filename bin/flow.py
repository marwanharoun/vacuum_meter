import RPi.GPIO as GPIO
import time, sys







class FlowRate:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        inpt = 13
        GPIO.setup(inpt, GPIO.IN)
        minutes = 0
        constant = 0.006
        time_new = 0.0
        rpt_int = 10
        global rate_cnt, tot_cnt
        rate_cnt = 0
        tot_cnt = 0
        rpt_int = float(input('Input desired report intervals in sec: '))
        GPIO.add_event_detect(inpt,GPIO.FALLING,callback=Pulse_cnt,bouncetime=10)
        
        
    def Pulse_cnt(inpt_pin):
        global rate_cnt, tot_cnt
        rate_cnt += 1
        tot_cnt += 1


    def get_value(self):
        time_new = time.time()+rpt_int
        rate_cnt = 0
        while time.time() <= time_new:
            try:
                None
            except KeyboardInterrupt:
                GPIO.cleanup()
                sys.exit()
        minutes += 1
        rate = round(((rate_cnt*constant)/(rpt_int/60)),2)
        tot = round(tot_cnt*constant,1)
        GPIO.cleanup()
        return rate

