# INSTALL PYTHON3 LIBRARIES:
sudo apt-get install python3-setuptools python-dev python3-pip vim tree
sudo pip3 install adafruit-circuitpython-mcp3xxx Adafruit_MCP3008 HX711

# CREATING LINKS:

sudo ln -s /home/pi/code/vacuum_meter/bin/start /bin/measure
sudo ln -s /home/pi/code/vacuum_meter/dev_script/pull.sh /bin/pull
