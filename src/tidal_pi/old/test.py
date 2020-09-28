from tidal_pi.old.tide_gpio import *


threads = []
threads.append(runForecastUpdateJob())
threads.append(runClockUpdateJob())
threads.append(runTideLightUpdateJob())

for thread in threads:
    thread.join()
