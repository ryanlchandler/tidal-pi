import tidal_pi.config as config
import logging

def create_clock(name, address):
    if config.CLOCK_TYPE == "LoggerClock":
        logging.info("using LoggerClock")
        from tidal_pi.clock.logger_clock import LoggerClock
        return LoggerClock(name, address)
    else:
        logging.info("using LedClock")
        from tidal_pi.clock.led_clock import LedClock
        return LedClock(name, address)