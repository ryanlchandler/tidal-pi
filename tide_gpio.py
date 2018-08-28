# import RPi.GPIO as GPIO
from tide_forecast import *
from config import *

def signalTide(tide):
    if(tide["type"] == "H"):
        _flashLight(HIGH_TIDE_PIN, "High Tide")
    else:
        _flashLight(LOW_TIDE_PIN, "Low Tide")

def _flashLight(ledPin, label):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(ledPin, GPIO.OUT)
    for i in range(5):
        print("{} LED on".format(label))
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(3)
        print("{} LED off".format(label))
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(3)