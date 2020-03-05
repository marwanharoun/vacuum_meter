import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Hardware SPI configuration:

class AnalogInput:

    def __init__(self):
        SPI_PORT   = 0
        SPI_DEVICE = 0
        self.CHANNEL = 0
        self.mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
        #global analog_read
        #analog_read = self.return_calib(self.mcp.read_adc(CHANNEL))
        
    def return_calib(self,input):
        A = 1.259149674
        B = -256.0778551 + 48.74493367
        pressure = A*(input) + B
        return pressure

    def get_value(self):
        #global analog_read
        analog_read = self.mcp.read_adc(self.CHANNEL)
        value = self.return_calib(analog_read)
        return value
