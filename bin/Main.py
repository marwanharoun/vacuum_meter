import datetime
import socket
import logging
import random
import subprocess
import sys
import csv
import time
import threading
import getopt

from Bme280 import Bme280
from Load import LoadCell
from Flow import Flow
from Stopwatch import Timer
from Obj_relay import Relay


# GLOBAL VARIABLES:
load_cell = LoadCell()
flow_input = Flow()
bme280 = Bme280()
timer = Timer()
rel_pump = Relay(2)

rows_load = []
rows_pressure = []
rows_flow = []

running = True



def create_csv(rows):
    header = ['timestamp', 'value', 'type']
    desc = input("Enter description: ").replace(" ","_")
    filename = '{:%Y%m%d-%H%M%S}'.format(datetime.datetime.now())+"-"+desc
    DIR = '/home/pi/public/vacuum_meter_data/'
    with open(DIR+filename+'.csv','wt') as f:
        csv_writer = csv.DictWriter(f, fieldnames=header)
        csv_writer.writeheader()
        csv_writer.writerows(rows)
        
        
        
        

def get_pressure(type="pressure"):
    while running:
        value = bme280.get_pressure()
        timestamp = timer.elapsed()
        row = {'timestamp': timestamp, 'value':value, 'type':type}
        rows_pressure.append(row)
        print(timestamp,"     ","{0:.2f}".format(value))
        if running == False:
            break
        time.sleep(0.25)

def get_flow(type="flow"):
    while running:
        value = flow_input.get_value()
        timestamp = timer.elapsed()
        row = {'timestamp': timestamp, 'value':value, 'type':type}
        rows_flow.append(row)
        print(timestamp,"                    ","{0:.2f}".format(value))
        if running == False:
            break
        time.sleep(0.25)
    
def get_load(type="load"):
    while running:
        value = load_cell.get_value()
        value = -value
        timestamp = timer.elapsed()
        row = {'timestamp': timestamp, 'value':value, 'type':type}
        rows_load.append(row)
        print(timestamp,"                                    ","{0:.2f}".format(value))
        if running == False:
            break
        time.sleep(0.25)
        

def create_threads():
    threads = []
    opts, args = getopt.getopt(sys.argv[1:],'plf')
    argz = []
    
    for opt, arg in opts:
        argz.append(opt)
    print(argz)
    
    if '-p' in argz:
        threads.append(threading.Thread(target=get_pressure))
        
    if '-l' in argz:
        threads.append(threading.Thread(target=get_load))
        
    if '-f' in argz:
        threads.append(threading.Thread(target=get_flow))
    
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
        
        


try:
    timer.start()
    rel_pump.turn_on()
    create_threads()
except KeyboardInterrupt:
    running = False
    rel_pump.turn_off()
    rows = []
    rows.extend(rows_pressure)
    rows.extend(rows_load)
    rows.extend(rows_flow)
    create_csv(rows)
    sys.exit()

