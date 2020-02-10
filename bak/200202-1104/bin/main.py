import time
import socket
import logging
import random
#import os
import subprocess




#Logger config:
def set_logger():
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(filename='/home/pi/system.log', format= '%(asctime)s %(levelname)s %(message)s', level= logging.INFO)


def get_pressure():
    ;

def get_load():
    ;

def create_csv():
    ;






#### MAIN ####


while True:

    set_logger()
    sleep_duration = 60
    try:

        t="{0:.2f}".format(t)
        h="{0:.2f}".format(h)
        results = "t="+str(t),"h="+str(h)
        subprocess.check_output('/usr/lib/inst-mon-pi/srv/send_value.sh '+str(t)+' '+str(h), shell=True)
        logging.info(results)

    except Exception as e:
        print(e)
        sleep_duration = 5
        logging.error(e)


    time.sleep(sleep_duration)
time.sleep(5)
