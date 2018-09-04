from tide import *
from Adafruit_LED_Backpack import SevenSegment

highTideClock = SevenSegment.SevenSegment(address=0x70)
highTideClock.begin()

lowTideClock = SevenSegment.SevenSegment(address=0x70)
lowTideClock.begin()

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