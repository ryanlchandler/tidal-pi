from tidal_pi.tide_clock import *
from tidal_pi.tide_gpio import *


threads = []
threads.append(runForecastUpdateJob())
threads.append(runClockUpdateJob())
threads.append(runTideLightUpdateJob())

for thread in threads:
    thread.join()
