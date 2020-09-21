# from tidal_pi.tide_clock import *
from tidal_pi.old.tide_gpio import *
from tidal_pi.light_strip.light_strip_factory import build_strip


def start():
    TidalPi().run()

class TidalPi():
    def run(self):
        # tide job
        # weather job
        # light strip job
        # high tide clock job
        # low tide clock job



        threads = []
        threads.append(runForecastUpdateJob())
        # threads.append(runClockUpdateJob())
        threads.append(runTideLightUpdateJob(build_strip()))

        for thread in threads:
            thread.join()