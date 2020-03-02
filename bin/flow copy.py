import RPi.GPIO as GPIO
import time, sys


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

def Pulse_cnt(inpt_pin):
    global rate_cnt, tot_cnt
    rate_cnt += 1
    tot_cnt += 1

rpt_int = float(input('Input desired report intervals in sec: '))
GPIO.add_event_detect(inpt,GPIO.FALLING,callback=Pulse_cnt,bouncetime=10)

print(str(time.asctime(time.localtime(time.time()))))

while True:
    time_new = time.time()+rpt_int
    rate_cnt = 0
    while time.time() <= time_new:
        try:
            None
            #print(GPIO.input(inpt), end='')
        except KeyboardInterrupt:
            GPIO.cleanup()
            sys.exit()
    minutes += 1
    LperM = round(((rate_cnt*constant)/(rpt_int/60)),2)
    TotLit = round(tot_cnt*constant,1)
    print('\nLiters / min ',LperM,'(',rpt_int,'second sample)')
    print('Total Liters ', TotLit)

GPIO.cleanup()

