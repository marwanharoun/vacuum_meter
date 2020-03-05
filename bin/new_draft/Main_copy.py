import datetime
import socket
import logging
import random
import subprocess
import sys
import csv
import time
import threading

from Load import LoadCell
from Analog import AnalogInput
from Flow import Flow
from Stopwatch import Timer


# GLOBAL VARIABLES:
load_cell = LoadCell()
analog_input = AnalogInput()
flow_input = Flow()
timer = Timer()

rows_load = []
rows_pressure = []
rows_flow = []

running = True



def create_csv(rows):
    header = ['timestamp', 'value', 'type']
    desc = input("Enter description: ").replace(" ","_")
    filename = '{:%Y%m%d-%H%M%S}'.format(datetime.datetime.now())+"-"+desc
    DIR = '/home/pi/data/'
    with open(DIR+filename+'.csv','wt') as f:
        csv_writer = csv.DictWriter(f, fieldnames=header)
        csv_writer.writeheader()
        csv_writer.writerows(rows)
        
        
        
        

def get_pressure(type="pressure"):
    while running:
        value = analog_input.get_value()
        time = timer.elapsed()
        row = {'timestamp': time, 'value':value, 'type':type}
        rows_pressure.append(row)
        print(time,"     ",value)
        if running == False:
            break
    

def get_flow(type="flow"):
    while running:
        value = flow_input.get_value()
        time = timer.elapsed()
        row = {'timestamp': time, 'value':value, 'type':type}
        rows_flow.append(row)
        print(time,"            ",value)
        if running == False:
            break
    
def get_load(type="load"):
    while running:
        value = load_cell.get_value()
        time = timer.elapsed()
        row = {'timestamp': time, 'value':value, 'type':type}
        rows_load.append(row)
        print(time,"                    ",value)
        if running == False:
            break
        


def create_threads():
    thread_pressure = threading.Thread(target=get_pressure)
    thread_flow = threading.Thread(target=get_flow)
    thread_load = threading.Thread(target=get_load)
    
    thread_pressure.start()
    thread_flow.start()
    thread_load.start()

    thread_pressure.join()
    thread_flow.join()
    thread_load.join()
    
    


try:
    timer.start()
    create_threads()
except KeyboardInterrupt:
    running = False
    rows = []
    rows.extend(rows_pressure)
    rows.extend(rows_load)
    rows.extend(rows_flow)
    create_csv(rows)
    sys.exit()

