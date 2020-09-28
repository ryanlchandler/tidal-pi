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
        if forecast != None:
            setLowTideClock(getNextTide(forecast, None, "L"))
            setHighTideClock(getNextTide(forecast, None, "H"))
        time.sleep(1)

def setLowTideClock(tide):
    _set_clock(tide, lowTideClock)

def setHighTideClock(tide):
    _set_clock(tide, highTideClock)

def _set_clock(tide, clock):
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