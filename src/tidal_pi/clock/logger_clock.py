import logging

logger = logging.getLogger(__name__)

class LoggerClock:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        logger.info("new clock named {} for address {}".format(name, address))

    def set_clock(self, tide):
        logger.info("set clock {} to {}".format(self.name, tide.get_date_time()))
