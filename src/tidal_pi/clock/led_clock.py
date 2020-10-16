import sys
import logging
from Adafruit_LED_Backpack import SevenSegment
from tidal_pi.util.i2c import i2cdetect

logger = logging.getLogger(__name__)

class LedClock:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        try:
            logger.info("creating {} at address {}".format(name, address))
            logger.info("running i2cdetect -y 1")
            logger.info("i2cdetect -y 1\n{}".format(i2cdetect()))
            logger.info("finished i2cdetect -y 1")
            self.clock = SevenSegment.SevenSegment(self.address)
            self.clock.begin()
            logger.debug("new clock named {} for address {}".format(name, address))
        except:
            logger.error("could not start clock", sys.exc_info()[0])
            self.clock = None

    def set_clock(self, tide):
        if self.clock != None:
            try:
                logger.debug("set clock {} to {}".format(self.name, tide.get_date_time()))
                tideTime = tide.get_date_time()
                hour = tideTime.hour
                minute = tideTime.minute

                self.clock.clear()
                # Set hours
                self.clock.set_digit(0, int(hour / 10))  # Tens
                self.clock.set_digit(1, hour % 10)  # Ones

                # Set minutes
                self.clock.set_digit(2, int(minute / 10))  # Tens
                self.clock.set_digit(3, minute % 10)  # Ones

                self.clock.set_colon(1)  # colon

                self.clock.write_display()
            except:
                logger.error("could not set clock", sys.exc_info()[0])
        else:
            logger.info("clock did not start cannot set {}".format(self.name))