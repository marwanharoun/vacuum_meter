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
        # Calibration with bme280 showed that pressure should be adjusted as follows:
        value = 1.259149674 * value + -256.0778551 + 48.74493367
        # 48.74493367 comes from doing a regression on data received from the first regression,
        # which showed that coeficient got to one but there was still an offset of 48.7
        return value
