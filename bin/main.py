import datetime
import socket
import logging
import random
import subprocess
import load
import analog
import sys
import csv
import time


# GLOBAL VARIABLES:
load_cell = load.LoadCell()
analog_input = analog.AnalogInput()


#Logger config:
def set_logger():
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(filename='/home/pi/system.log', format= '%(asctime)s %(levelname)s %(message)s', level= logging.INFO)



def get_values():
    rows = []
    try:
        while True:
            load = load_cell.get_value()
            pressure = analog_input.get_value()
            row = {'timestamp': '{:%Y-%m-%d %H:%M:%S:%f}'.format(datetime.datetime.now()), 'load':load, 'pressure':pressure}
            rows.append(row)
            time.sleep(0.25)
    except KeyboardInterrupt:
        print(rows)
        create_csv(rows)
        sys.exit()


def create_csv(rows):
    header = ['timestamp', 'load', 'pressure']
    desc = input("Enter description: ").replace(" ","_")
    filename = '{:%Y%m%d-%H%M%S}'.format(datetime.datetime.now())+"-"+desc
    DIR = '/home/pi/data/'
    with open(DIR+filename+'.csv','wt') as f:
        csv_writer = csv.DictWriter(f, fieldnames=header)
        csv_writer.writeheader()
        csv_writer.writerows(rows)


get_values()
