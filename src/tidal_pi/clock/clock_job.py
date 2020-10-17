from tidal_pi import config
from tidal_pi.clock import clock_factory
import time


class ClockJob:

    def __init__(self, tide_state_provider):
        self.highTideClock = clock_factory.create_clock("HighTideClock", config.HIGH_TIDE_CLOCK_ADDRESS)
        self.lowTideClock = clock_factory.create_clock("LowTideClock", config.LOW_TIDE_CLOCK_ADDRESS)
        self.tide_state_provider = tide_state_provider

    def run(self):
        while (True):
            tide_state = self.tide_state_provider.get_tide_state()

            if tide_state != None:
                self.highTideClock.set_clock(tide_state.get_next_high_tide())
                self.lowTideClock.set_clock(tide_state.get_next_low_tide())