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
import board
import busio
import adafruit_bme280


# GLOBAL VARIABLES:
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
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
            bme_pressure = bme280.pressure
            analogue_pressure = analog_input.get_value()
            print("{0:.2f}".format(bme_pressure),"  ",analogue_pressure)
            row = {'timestamp': '{:%Y-%m-%d %H:%M:%S:%f}'.format(datetime.datetime.now()), 'bme_pressure':bme_pressure, 'analogue_pressure':analogue_pressure}
            rows.append(row)
            time.sleep(0.25)
    except KeyboardInterrupt:
        print(rows)
        create_csv(rows)
        sys.exit()


def create_csv(rows):
    header = ['timestamp', 'bme_pressure', 'analogue_pressure']
    desc = input("Enter description: ").replace(" ","_")
    filename = '{:%Y%m%d-%H%M%S}'.format(datetime.datetime.now())+"-"+desc
    DIR = '/home/pi/data/'
    with open(DIR+filename+'.csv','wt') as f:
        csv_writer = csv.DictWriter(f, fieldnames=header)
        csv_writer.writeheader()
        csv_writer.writerows(rows)


get_values()
