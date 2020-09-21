import tidal_pi.config as config
import tidal_pi.clock.clock_factory as clock_factory
import time


class LowTideClockJob:

    def __init__(self, tide_state_provider):
        self.clock = clock_factory.create_clock("LowTideClock", config.LOW_TIDE_CLOCK_ADDRESS)
        self.tide_state_provider = tide_state_provider

    def run(self):
        while (True):
            tide_state = self.tide_state_provider.get_tide_state()

            if tide_state != None:
                self.clock.setClock(tide_state.get_next_low_tide())
            time.sleep(1)