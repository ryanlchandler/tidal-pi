import logging
from Adafruit_LED_Backpack import SevenSegment

class LedClock:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.clock = SevenSegment.SevenSegment(self.address)
        self.clock.begin()
        logging.debug("new clock named {} for address {}".format(name, address))

    def setClock(self, tide):
        logging.debug("set clock {} to {}".format(self.name, tide.getDateTime()))
        tideTime = tide.getDateTime()
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