from tidal_pi import config
import logging

logger = logging.getLogger(__name__)

def create_clock(name, address):
    if config.CLOCK_TYPE == "LoggerClock":
        logger.info("using LoggerClock")
        from tidal_pi.clock.logger_clock import LoggerClock
        return LoggerClock(name, address)
    else:
        logger.info("using LedClock")
        from tidal_pi.clock.led_clock import LedClock
        return LedClock(name, address)