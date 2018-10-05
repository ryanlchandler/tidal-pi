from tide_forecast import *
from config import *
from neopixel import *

LED_COUNT   = 48       # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)

# high lit
LEVEL_4 = 90
# flash 75
LEVEL_3 = 75
# flash 50
LEVEL_2 = 50
# flash 25
LEVEL_1 = 25
# flash low
LEVEL_0 = 10
# low lit

TIDE_OUT = "OUT"
TIDE_IN = "IN"

LIGHT_0_IDX = 0 # low
LIGHT_1_IDX = 1 # 25
LIGHT_2_IDX = 2 # 50
LIGHT_3_IDX = 3 # 75
LIGHT_4_IDX = 4 # 90
LIGHT_5_IDX = 5 # high
LIGHT_6_IDX = 6 # 90
LIGHT_7_IDX = 7 # 75
LIGHT_8_IDX = 8 # 50
LIGHT_9_IDX = 9 # 25

# 90 4        5        6
# 75   3             7
# 50     2         8
# 25       1    9
# 10         0

def Kolor(r, g, b):
    return {
        "r": r,
        "g": g,
        "b": b
    }

OFF_COLOR = Kolor(0, 0, 0)
IN_TIDE_COLOR = Kolor(3, 77, 203) # r g b
OUT_TIDE_COLOR = Kolor(255, 0, 60)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
# Intialize the library (must be called once before other functions).
strip.begin()


def signalTide(tide, currentPercentOfHighTide):
    lightColor = OUT_TIDE_COLOR
    if (tide["type"] == "H"):
        lightColor = IN_TIDE_COLOR

    if (lessThan(currentPercentOfHighTide, LEVEL_0)):
        _signalLow(lightColor)
    elif(between(currentPercentOfHighTide, LEVEL_0,LEVEL_1)):
        _signalLevel1(lightColor)
    elif(between(currentPercentOfHighTide,LEVEL_1, LEVEL_2)):
        _signalLevel2(lightColor)
    elif(between(currentPercentOfHighTide, LEVEL_2, LEVEL_3)):
        _signalLevel3(lightColor)
    elif(between(currentPercentOfHighTide, LEVEL_3, LEVEL_4)):
        _signalLevel4(lightColor)
    elif(greaterThan(currentPercentOfHighTide, LEVEL_4)):
        _signalHigh(lightColor)
    else:
        print("no signals found")

def _signalLow(lightColor):
    print("signal low")
    onLights = [
                    LIGHT_0_IDX
                ]
    _updateLights(onLights, lightColor)
    time.sleep(30)

def _signalLevel1(lightColor):
    print("signal level 1")
    onLights = [
                    LIGHT_0_IDX,
                    LIGHT_1_IDX,
                    LIGHT_9_IDX,
                ]
    _updateLights(onLights, lightColor)

def _signalLevel2(lightColor):
    print("signal level 2")
    onLights = [
                    LIGHT_0_IDX,
                    LIGHT_1_IDX,
                    LIGHT_2_IDX,
                    LIGHT_8_IDX,
                    LIGHT_9_IDX,
                ]
    _updateLights(onLights, lightColor)

def _signalLevel3(lightColor):
    print("signal level 3")
    onLights = [
                    LIGHT_0_IDX,
                    LIGHT_1_IDX,
                    LIGHT_2_IDX,
                    LIGHT_3_IDX,
                    LIGHT_7_IDX,
                    LIGHT_8_IDX,
                    LIGHT_9_IDX,
                ]
    _updateLights(onLights, lightColor)

def _signalLevel4(lightColor):
    print("signal level 4")
    onLights = [
                    LIGHT_0_IDX,
                    LIGHT_1_IDX,
                    LIGHT_2_IDX,
                    LIGHT_3_IDX,
                    LIGHT_4_IDX,
                    LIGHT_6_IDX,
                    LIGHT_7_IDX,
                    LIGHT_8_IDX,
                    LIGHT_9_IDX,
                ]
    _updateLights(onLights, lightColor)

def _signalHigh(lightColor):
    print("signal high")
    onLights = [
                    LIGHT_0_IDX,
                    LIGHT_1_IDX,
                    LIGHT_2_IDX,
                    LIGHT_3_IDX,
                    LIGHT_4_IDX,
                    LIGHT_5_IDX,
                    LIGHT_6_IDX,
                    LIGHT_7_IDX,
                    LIGHT_8_IDX,
                    LIGHT_9_IDX,
                ]
    _updateLights(onLights, lightColor)

def between(currentPercentOfHighTide, min, max):
    return currentPercentOfHighTide > min and currentPercentOfHighTide <= max

def lessThan(currentPercentOfHighTide, min):
    return currentPercentOfHighTide <= min

def greaterThan(currentPercentOfHighTide, max):
    return currentPercentOfHighTide > max

def _updateLights(onLights, lightColor):
    _turnOffLight(onLights)
    for lightIdx in onLights:
        _turnOnLight(lightIdx, lightColor)
    _updateStrip()

def _turnOffLights(leaveOn):
    for i in range(48):
        if(i not in leaveOn):
            _turnOffLight(i)

def _turnOnLight(lightIdx, color, brightness=255):
    try:
        strip.setPixelColor(lightIdx, Color((brightness * color["r"] / 255), (brightness * color["g"] / 255), (brightness * color["b"] / 255)))
    except:
        print("could not turn on light", sys.exc_info()[0])

def _turnOffLight(lightIdx):
    try:
        strip.setPixelColor(lightIdx, Color(OFF_COLOR["r"], OFF_COLOR["g"], OFF_COLOR["b"]))
    except:
        print("could not turn off light", sys.exc_info()[0])

def _updateStrip():
    try:
        strip.show()
    except:
        print("could not show lights", sys.exc_info()[0])
