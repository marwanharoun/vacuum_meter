
echo Enter File Name:
read CSV


scp pi@192.168.0.103:~/vacuum_meter/data/${CSV} ~/OneDrive/stom/systems/vacuum_meter/data
