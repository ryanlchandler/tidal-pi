import sys
import logging
from Adafruit_LED_Backpack import SevenSegment

class LedClock:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        try:
            self.clock = SevenSegment.SevenSegment(self.address)
            self.clock.begin()
            logging.debug("new clock named {} for address {}".format(name, address))
        except:
            logging.error("could not start clock", sys.exc_info()[0])

    def set_clock(self, tide):
        try:
            logging.debug("set clock {} to {}".format(self.name, tide.get_date_time()))
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
            logging.error("could not set clock", sys.exc_info()[0])