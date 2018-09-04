from tide_forecast import *
from config import *
from neopixel import *

LED_COUNT   = 48       # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)

LEVEL_0 = 10
LEVEL_1 = 25
LEVEL_2 = 50
LEVEL_3 = 75
LEVEL_4 = 90
LEVEL_5 = 75
LEVEL_6 = 50
LEVEL_7 = 25
LEVEL_8 = 10

LIGHT_0_IDX = 0
LIGHT_1_IDX = 1
LIGHT_2_IDX = 2
LIGHT_3_IDX = 3
LIGHT_4_IDX = 4
LIGHT_5_IDX = 5
LIGHT_6_IDX = 6
LIGHT_7_IDX = 7
LIGHT_8_IDX = 8
LIGHT_9_IDX = 9

OFF_COLOR = Color(0, 0, 0)
IN_TIDE_COLOR = Color(0, 255, 0)
OUT_TIDE_COLOR = Color(255, 0, 0)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
# Intialize the library (must be called once before other functions).
strip.begin()

def signalHighTide(tide, currentPercentOfHighTide):
    if(currentPercentOfHighTide <= LEVEL_0):
        _signalLevel0(tide, currentPercentOfHighTide)
    elif(currentPercentOfHighTide > LEVEL_0 and currentPercentOfHighTide <= LEVEL_1):
        _signalLevel1(tide, currentPercentOfHighTide)
    elif(currentPercentOfHighTide > LEVEL_1 and currentPercentOfHighTide <= LEVEL_2):
        _signalLevel2(tide, currentPercentOfHighTide)
    elif(currentPercentOfHighTide > LEVEL_2 and currentPercentOfHighTide <= LEVEL_3):
        _signalLevel3(tide, currentPercentOfHighTide)
    elif(currentPercentOfHighTide > LEVEL_3 and currentPercentOfHighTide <= LEVEL_4):
        _signalLevel4(tide, currentPercentOfHighTide)

def signalLowTide(tide, currentPercentOfHighTide):
    if(currentPercentOfHighTide >= LEVEL_4):
        _signalLevel4(tide, currentPercentOfHighTide)
    elif(currentPercentOfHighTide < LEVEL_4 and currentPercentOfHighTide >= LEVEL_5):
        _signalLevel5(tide, currentPercentOfHighTide)
    elif(currentPercentOfHighTide < LEVEL_5 and currentPercentOfHighTide >= LEVEL_6):
        _signalLevel6(tide, currentPercentOfHighTide)
    elif(currentPercentOfHighTide < LEVEL_6 and currentPercentOfHighTide >= LEVEL_7):
        _signalLevel7(tide, currentPercentOfHighTide)
    elif(currentPercentOfHighTide < LEVEL_7 and currentPercentOfHighTide >= LEVEL_8):
        _signalLevel8(tide, currentPercentOfHighTide)
    elif(currentPercentOfHighTide < LEVEL_8):
        _signalLevel9(tide, currentPercentOfHighTide)

def signalTide(tide, currentPercentOfHighTide):
    if(tide["type"] == "H"):
        signalHighTide(tide, currentPercentOfHighTide)
    else:
        signalLowTide(tide, currentPercentOfHighTide)

def _signalLevel0(tide, currentPercentOfHighTide):
    print("signal level 0")
    _turnOffAllLights(LIGHT_0_IDX, LIGHT_0_IDX)
    _turnOnLight(LIGHT_0_IDX, IN_TIDE_COLOR)
    time.sleep(30)

def _signalLevel1(tide, currentPercentOfHighTide):
    print("signal level 1")
    _turnOffAllLights(LIGHT_0_IDX, LIGHT_1_IDX)
    _turnOnLight(LIGHT_0_IDX, IN_TIDE_COLOR)
    _flashLight(LIGHT_1_IDX, IN_TIDE_COLOR)

def _signalLevel2(tide, currentPercentOfHighTide):
    print("signal level 2")
    _turnOffAllLights(LIGHT_0_IDX, LIGHT_2_IDX)
    _turnOnLight(LIGHT_0_IDX, IN_TIDE_COLOR)
    _turnOnLight(LIGHT_1_IDX, IN_TIDE_COLOR)
    _flashLight(LIGHT_2_IDX, IN_TIDE_COLOR)

def _signalLevel3(tide, currentPercentOfHighTide):
    print("signal level 3")
    _turnOffAllLights(LIGHT_0_IDX, LIGHT_3_IDX)
    _turnOnLight(LIGHT_0_IDX, IN_TIDE_COLOR)
    _turnOnLight(LIGHT_1_IDX, IN_TIDE_COLOR)
    _turnOnLight(LIGHT_2_IDX, IN_TIDE_COLOR)
    _flashLight(LIGHT_3_IDX, IN_TIDE_COLOR)

def _signalLevel4(tide, currentPercentOfHighTide):
    print("signal level 4")
    _turnOffAllLights([LIGHT_4_IDX, LIGHT_6_IDX])
    _turnOnLight(LIGHT_4_IDX, IN_TIDE_COLOR)
    _turnOnLight(LIGHT_5_IDX, IN_TIDE_COLOR)
    _turnOnLight(LIGHT_6_IDX, IN_TIDE_COLOR)
    time.sleep(30)

def _signalLevel5(tide, currentPercentOfHighTide):
    print("signal level 5")
    _turnOffAllLights(LIGHT_6_IDX, LIGHT_7_IDX)
    _turnOnLight(LIGHT_6_IDX, OUT_TIDE_COLOR)
    _flashLight(LIGHT_7_IDX, OUT_TIDE_COLOR)

def _signalLevel6(tide, currentPercentOfHighTide):
    print("signal level 6")
    _turnOffAllLights(LIGHT_6_IDX, LIGHT_8_IDX)
    _turnOnLight(LIGHT_6_IDX, OUT_TIDE_COLOR)
    _turnOnLight(LIGHT_7_IDX, OUT_TIDE_COLOR)
    _flashLight(LIGHT_8_IDX, OUT_TIDE_COLOR)

def _signalLevel7(tide, currentPercentOfHighTide):
    print("signal level 7")
    _turnOffAllLights(LIGHT_6_IDX, LIGHT_9_IDX)
    _turnOnLight(LIGHT_6_IDX, OUT_TIDE_COLOR)
    _turnOnLight(LIGHT_7_IDX, OUT_TIDE_COLOR)
    _turnOnLight(LIGHT_8_IDX, OUT_TIDE_COLOR)
    _flashLight(LIGHT_9_IDX, OUT_TIDE_COLOR)

def _signalLevel8(tide, currentPercentOfHighTide):
    print("signal level 8")
    _turnOffAllLights(LIGHT_6_IDX, LIGHT_9_IDX)
    _turnOnLight(LIGHT_6_IDX, OUT_TIDE_COLOR)
    _turnOnLight(LIGHT_7_IDX, OUT_TIDE_COLOR)
    _turnOnLight(LIGHT_8_IDX, OUT_TIDE_COLOR)
    _turnOnLight(LIGHT_9_IDX, OUT_TIDE_COLOR)
    _flashLight(LIGHT_0_IDX, OUT_TIDE_COLOR)

def _signalLevel9(tide, currentPercentOfHighTide):
    print("signal level 9")
    _turnOffAllLights(LIGHT_0_IDX, LIGHT_0_IDX)
    _turnOnLight(LIGHT_0_IDX, OUT_TIDE_COLOR)
    time.sleep(30)

def _turnOnLight(lightIdx, color):
    strip.setPixelColor(lightIdx, color)
    strip.show()

def _turnOffAllLights(leaveOnStart, leaveOnEnd):
    for i in range(48):
        if(i < leaveOnStart or i > leaveOnEnd):
            _turnOffLight(i)
    # _turnOffLight(LIGHT_0_IDX)
    # _turnOffLight(LIGHT_1_IDX)
    # _turnOffLight(LIGHT_2_IDX)
    # _turnOffLight(LIGHT_3_IDX)
    # _turnOffLight(LIGHT_4_IDX)
    # _turnOffLight(LIGHT_5_IDX)
    # _turnOffLight(LIGHT_6_IDX)
    # _turnOffLight(LIGHT_7_IDX)
    # _turnOffLight(LIGHT_8_IDX)
    # _turnOffLight(LIGHT_9_IDX)

def _turnOffLight(lightIdx):
    strip.setPixelColor(lightIdx, OFF_COLOR)
    strip.show()

def _flashLight(lightIdx, color):
    for i in range(20):
        _turnOnLight(lightIdx, color)
        time.sleep(1)
        _turnOffLight(lightIdx)
        time.sleep(.5)