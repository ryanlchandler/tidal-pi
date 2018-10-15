from tide import *
from tide_forecast import *
from Adafruit_LED_Backpack import SevenSegment
from threading import Thread

highTideClock = SevenSegment.SevenSegment(address=0x70)
highTideClock.begin()

lowTideClock = SevenSegment.SevenSegment(address=0x71)
lowTideClock.begin()

def runClockUpdateJob():
    t = Thread(target=clockUpdateJob)
    t.start()
    return t

def clockUpdateJob():
    while(True):
        forecast = getForecast()
        setLowTideClock(getNextTide(forecast, None, "L"))
        setHighTideClock(getNextTide(forecast, None, "H"))
        time.sleep(1)

def setLowTideClock(tide):
    _setClock(tide, lowTideClock)

def setHighTideClock(tide):
    _setClock(tide, highTideClock)

def _setClock(tide, clock):
    tideTime = getTideDateTime(tide)
    hour = tideTime.hour
    minute = tideTime.minute

    clock.clear()
    # Set hours
    clock.set_digit(0, int(hour / 10))  # Tens
    clock.set_digit(1, hour % 10)  # Ones

    # Set minutes
    clock.set_digit(2, int(minute / 10))  # Tens
    clock.set_digit(3, minute % 10)  # Ones

    clock.set_colon(1)  # colon

    clock.write_display()