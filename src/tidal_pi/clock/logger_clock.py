import logging

class LoggerClock:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        logging.info("new clock named {} for address {}".format(name, address))

    def set_clock(self, tide):
        logging.info("set clock {} to {}".format(self.name, tide.get_date_time()))
