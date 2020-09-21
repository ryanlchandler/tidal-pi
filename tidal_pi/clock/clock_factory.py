import tidal_pi.config as config

def create_clock(name, address):
    if config.LIGHT_STRIP_TYPE == "LoggerClock":
        print("using LoggerClock")
        from tidal_pi.clock.logger_clock import LoggerClock
        return LoggerClock(name, address)
    else:
        print("using LedClock")
        from tidal_pi.clock.led_clock import LedClock
        return LedClock(name, address)