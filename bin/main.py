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
    filename = '{:%Y%m%d-%H%M%S}'.format(datetime.datetime.now())
    DIR = '/home/pi/vacuum_meter/data/'
    with open(DIR+filename+'.csv','wt') as f:
        csv_writer = csv.DictWriter(f, fieldnames=header)
        csv_writer.writeheader()
        csv_writer.writerows(rows)


get_values()




#### MAIN ####


# while True:
#
#     set_logger()
#     sleep_duration = 60
#     try:
#
#         t="{0:.2f}".format(t)
#         h="{0:.2f}".format(h)
#         results = "t="+str(t),"h="+str(h)
#         subprocess.check_output('/usr/lib/inst-mon-pi/srv/send_value.sh '+str(t)+' '+str(h), shell=True)
#         logging.info(results)
#
#     except Exception as e:
#         print(e)
#         sleep_duration = 5
#         logging.error(e)
#
#
#     time.sleep(sleep_duration)
# time.sleep(5)
