import datetime
import socket
import logging
import random
import subprocess
import load
import analog
import flow
import sys
import csv
import time


# GLOBAL VARIABLES:
load_cell = load.LoadCell()
analog_input = analog.AnalogInput()
flow_input = flow.Flow()


#Logger config:
def set_logger():
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(filename='/home/pi/system.log', format= '%(asctime)s %(levelname)s %(message)s', level= logging.INFO)



def get_values():
    rows = []
    try:
        while True:
            A = 0.00488594648262289
            B = -106.44773936296
            C = -155.787500483901   #Verticality Correction
            raw = load_cell.get_value()
            load = A*raw + B - C
            pressure = analog_input.get_value()
            flow_rate = flow_input.get_value()
            print("{0:.2f}".format(pressure),"  ","{0:.2f}".format(load),"{0:.2f}".format(flow_rate))
            row = {'timestamp': '{:%Y-%m-%d %H:%M:%S:%f}'.format(datetime.datetime.now()), 'load':load, 'pressure':pressure, 'flow':flow_rate}
            rows.append(row)
            time.sleep(0.25)
    except KeyboardInterrupt:
        print(rows)
        create_csv(rows)
        sys.exit()


def create_csv(rows):
    header = ['timestamp', 'load', 'pressure','flow']
    desc = input("Enter description: ").replace(" ","_")
    filename = '{:%Y%m%d-%H%M%S}'.format(datetime.datetime.now())+"-"+desc
    DIR = '/home/pi/data/'
    with open(DIR+filename+'.csv','wt') as f:
        csv_writer = csv.DictWriter(f, fieldnames=header)
        csv_writer.writeheader()
        csv_writer.writerows(rows)


get_values()
