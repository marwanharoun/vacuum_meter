#!/bin/sh
echo Enter IP:
read IP
scp -r pi@${IP}:/home/pi/vacuum_meter/ ~/Desktop/vacuum_meter/$(date +%y%m%d)-$(date +%H%M)/
