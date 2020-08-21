# from tidal_pi.tide_clock import *
from tidal_pi.tide_gpio import *
from tidal_pi.strip_factory import build_strip


def start():
    TidalPi().run()

class TidalPi():
    def run(self):
        threads = []
        threads.append(runForecastUpdateJob())
        # threads.append(runClockUpdateJob())
        threads.append(runTideLightUpdateJob(build_strip()))

        for thread in threads:
            thread.join()