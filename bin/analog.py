import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Hardware SPI configuration:

class AnalogInput:
    def __init__(self):
        SPI_PORT   = 0
        SPI_DEVICE = 0
        self.mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

    def get_value(self):
        # Read all the ADC channel values in a list.
        value = self.mcp.read_adc(0)
        # Print the ADC values.
        # print(value)
        # FOR PRESSURE SENSOR ONLY:
        # Calibration with bme280 showed that pressure should be increased by 43mBar
        value = value + 43
        return value
