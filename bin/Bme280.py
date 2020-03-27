import board
import busio
import Adafruit_bme280
import logging


class Bme280:

    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.bme280 = Adafruit_bme280.Adafruit_BME280_I2C(i2c)
        
        
    def get_pressure(self):
        try:
            pressure = self.bme280.pressure
            if pressure is None:
                error = "(SENSOR FAILURE!)"
                raise Exception(error)

            return pressure
        except Exception:
            raise
