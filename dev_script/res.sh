#!/bin/sh
echo Enter DIR:
read DIR
echo Enter IP:
read IP


ssh pi@${IP} -p 22 'sudo rm -rf /home/pi/vacuum_meter/; sudo mkdir /home/pi/vacuum_meter; mkdir ~/temp'

scp -r -P 22 ${DIR}/* pi@${IP}:temp
ssh pi@${IP} -p 22 'sudo rm -rf /home/pi/vacuum_meter/; sudo mkdir /home/pi/vacuum_meter; sudo mv ~/temp/* /home/pi/vacuum_meter/; rm -r ~/temp/;'
