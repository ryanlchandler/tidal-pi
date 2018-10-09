from tide_forecast import *
from config import *
from neopixel import *
from tide_level import TideLevel

LED_COUNT   = 48       # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)

LEVEL_100  = 100 # high lit
LEVEL_95 = 95    # h-flash 100 or l-flash 90
LEVEL_90 = 90    # 90 lit
LEVEL_83 = 83    # h-flash 90 or l-flash 75
LEVEL_75 = 75    # 75 lit
LEVEL_63 = 63    # h-flash 75 or l-flash 50
LEVEL_50 = 50    # 50 lit
LEVEL_38 = 38    # h-flash 50 or l-flash 25
LEVEL_25 = 25    # 25 lit
LEVEL_13 = 13    # h-flash 25 or l-flash 0
LEVEL_0 = 0      # low lit


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


def _createHighLevels():
    return [
# low IN
        TideLevel("low tide", "H", 0,  [LIGHT_0_IDX]),
        TideLevel("level 13", "H", 13, [LIGHT_0_IDX], [LIGHT_1_IDX, LIGHT_9_IDX]),
        TideLevel("level 25", "H", 25, [LIGHT_0_IDX, LIGHT_1_IDX, LIGHT_9_IDX]),
        TideLevel("level 38", "H", 38, [LIGHT_0_IDX, LIGHT_1_IDX, LIGHT_9_IDX], [LIGHT_2_IDX, LIGHT_8_IDX]),
        TideLevel("level 50", "H", 50, [LIGHT_0_IDX, LIGHT_1_IDX, LIGHT_2_IDX, LIGHT_8_IDX, LIGHT_9_IDX]),
        TideLevel("level 63", "H", 63, [LIGHT_0_IDX, LIGHT_1_IDX, LIGHT_2_IDX, LIGHT_8_IDX, LIGHT_9_IDX], [LIGHT_3_IDX, LIGHT_7_IDX]),
        TideLevel("level 75", "H", 75, [LIGHT_0_IDX, LIGHT_1_IDX, LIGHT_2_IDX, LIGHT_3_IDX, LIGHT_7_IDX, LIGHT_8_IDX, LIGHT_9_IDX]),
        TideLevel("level 83", "H", 83, [LIGHT_0_IDX, LIGHT_1_IDX, LIGHT_2_IDX, LIGHT_3_IDX, LIGHT_7_IDX, LIGHT_8_IDX, LIGHT_9_IDX], [LIGHT_4_IDX, LIGHT_6_IDX]),
        TideLevel("level 90", "H", 90, [LIGHT_0_IDX, LIGHT_1_IDX, LIGHT_2_IDX, LIGHT_3_IDX, LIGHT_4_IDX, LIGHT_6_IDX, LIGHT_7_IDX, LIGHT_8_IDX, LIGHT_9_IDX], [LIGHT_5_IDX]),
        TideLevel("level 95", "H", 95, [LIGHT_0_IDX, LIGHT_1_IDX, LIGHT_2_IDX, LIGHT_3_IDX, LIGHT_4_IDX, LIGHT_5_IDX, LIGHT_6_IDX, LIGHT_7_IDX, LIGHT_8_IDX, LIGHT_9_IDX]),
# high IN
    ]

def _createLowLevels():
    return [
# high OUT
        TideLevel("high tide","L",100, [LIGHT_0_IDX, LIGHT_1_IDX, LIGHT_2_IDX, LIGHT_3_IDX, LIGHT_4_IDX, LIGHT_5_IDX, LIGHT_6_IDX, LIGHT_7_IDX, LIGHT_8_IDX, LIGHT_9_IDX]),
        TideLevel("level 95", "L", 95, [LIGHT_0_IDX, LIGHT_1_IDX, LIGHT_2_IDX, LIGHT_3_IDX, LIGHT_4_IDX, LIGHT_6_IDX, LIGHT_7_IDX, LIGHT_8_IDX, LIGHT_9_IDX], [LIGHT_4_IDX, LIGHT_6_IDX]),
        TideLevel("level 90", "L", 90, [LIGHT_0_IDX, LIGHT_1_IDX, LIGHT_2_IDX, LIGHT_3_IDX, LIGHT_7_IDX, LIGHT_8_IDX, LIGHT_9_IDX]),
        TideLevel("level 83", "L", 83, [LIGHT_0_IDX, LIGHT_1_IDX, LIGHT_2_IDX, LIGHT_8_IDX, LIGHT_9_IDX], [LIGHT_3_IDX, LIGHT_7_IDX]),
        TideLevel("level 75", "L", 75, [LIGHT_0_IDX, LIGHT_1_IDX, LIGHT_2_IDX, LIGHT_8_IDX, LIGHT_9_IDX]),
        TideLevel("level 63", "L", 63, [LIGHT_0_IDX, LIGHT_1_IDX, LIGHT_9_IDX], [LIGHT_2_IDX, LIGHT_8_IDX]),
        TideLevel("level 50", "L", 50, [LIGHT_0_IDX, LIGHT_1_IDX, LIGHT_9_IDX]),
        TideLevel("level 38", "L", 38, [LIGHT_0_IDX], [LIGHT_1_IDX, LIGHT_9_IDX]),
        TideLevel("level 25", "L", 25, [LIGHT_0_IDX]),
        TideLevel("level 13", "L", 13, [], [LIGHT_0_IDX]),
# low OUT
    ]

highTideLevels = _createHighLevels()
lowTideLevels = _createLowLevels()

def signalTide(tide, currentPercentOfHighTide):
    if (tide["type"] == "H"):
        _signalInTide(currentPercentOfHighTide)
    else:
        _signalOutTide(currentPercentOfHighTide)

def _signalInTide(currentPercentOfHighTide):
    lightColor = IN_TIDE_COLOR
    currentLevel = None
    for level in highTideLevels:
        if level.hasMetLevel("H", currentPercentOfHighTide):
            if currentLevel == None or level.getPercentOfHighTide() > currentLevel.getPercentOfHighTide():
                currentLevel = level
    print("signal H {}".format(currentLevel.getName()))
    _updateLights(currentLevel.getTurnOnLights(), currentLevel.getFlashLights(), lightColor)

def _signalOutTide(currentPercentOfHighTide):
    lightColor = IN_TIDE_COLOR
    currentLevel = None
    for level in lowTideLevels:
        if level.hasMetLevel("L", currentPercentOfHighTide):
            if currentLevel == None or level.getPercentOfHighTide() < currentLevel.getPercentOfHighTide():
                currentLevel = level
    print("signal L {}".format(currentLevel.getName()))
    _updateLights(currentLevel.getTurnOnLights(), currentLevel.getFlashLights(), lightColor)

def _updateLights(onLights, flashLights, lightColor):
    _turnOffLights(onLights)

    for lightIdx in onLights:
        _turnOnLight(lightIdx, lightColor)
    _updateStrip()

    if flashLights != None:
        _flashLights(flashLights, lightColor)

def _turnOffLights(leaveOn):
    for i in range(48):
        if(i not in leaveOn):
            _turnOffLight(i)

def _turnOnLight(lightIdx, color, brightness=255):
    try:
        strip.setPixelColor(lightIdx, Color((brightness * color["r"] / 255), (brightness * color["g"] / 255), (brightness * color["b"] / 255)))
    except:
        print("could not turn on light {}".format(lightIdx), sys.exc_info()[0])

def _turnOffLight(lightIdx):
    try:
        strip.setPixelColor(lightIdx, Color(OFF_COLOR["r"], OFF_COLOR["g"], OFF_COLOR["b"]))
    except:
        print("could not turn off light {}".format(lightIdx), sys.exc_info()[0])

def _updateStrip():
    try:
        strip.show()
    except:
        print("could not show lights", sys.exc_info()[0])

def _turnOnLights(lightIdxs, color, birghtness):
    for lightIdx in lightIdxs:
        _turnOnLight(lightIdx, color, birghtness)

def _flashLights(flashLights, color):
    for i in range(20):
        for x in range(20):
            _turnOnLights(flashLights, color, (x * 20))
            _updateStrip()
            time.sleep(.2)
        
        for x in range(20):
            _turnOnLights(flashLights, color, 255 - (x * 20))
            _updateStrip()
            time.sleep(.2)


