import sys
import logging
from Adafruit_LED_Backpack import SevenSegment
from tidal_pi.util.i2c import i2cdetect

logger = logging.getLogger(__name__)

class LedClock:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.clock = None

    def set_clock(self, tide):
        clock = self._get_clock()
        if clock != None:
            try:
                logger.debug("set clock {} at {} to {}".format(self.name, self.address, tide.get_date_time()))
                tideTime = tide.get_date_time()
                hour = tideTime.hour
                minute = tideTime.minute

                clock.clear()
                # Set hours
                logger.info("{} set_digit(0, {})".format(self.name, int(hour / 10)))
                logger.info("{} set_digit(1, {})".format(self.name, hour % 10))
                logger.info("{} set_digit(2, {})".format(self.name, int(minute / 10)))
                logger.info("{} set_digit(3, {})".format(self.name, minute % 10))
                clock.set_digit(0, int(hour / 10))  # Tens
                clock.set_digit(1, hour % 10)  # Ones

                # Set minutes
                clock.set_digit(2, int(minute / 10))  # Tens
                clock.set_digit(3, minute % 10)  # Ones

                clock.set_colon(1)  # colon

                clock.write_display()
            except:
                logger.error("could not set clock", exc_info=True)
        else:
            logger.info("clock did not start cannot set {}".format(self.name))

    def _get_clock(self):
        if self.clock == None:
            try:
                logger.info("creating {} at address {}".format(self.name, self.address))
                logger.info("running i2cdetect -y 1")
                logger.info("i2cdetect -y 1\n{}".format(i2cdetect()))
                logger.info("finished i2cdetect -y 1")
                self.clock = SevenSegment.SevenSegment(address=self.address)
                self.clock.begin()
                logger.debug("new clock named {} for address {}".format(self.name, self.address))
            except:
                self.clock = None
                logger.error("could not start clock", exc_info=True)

        return self.clock
