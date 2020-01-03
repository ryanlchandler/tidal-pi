from tide_clock import *
from tide_gpio import *


threads = []
threads.append(runForecastUpdateJob())
threads.append(runClockUpdateJob())
# threads.append(runTideLightUpdateJob())

for thread in threads:
    thread.join()
