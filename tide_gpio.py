from tide_forecast import *
from config import *
from neopixel import *

LED_COUNT   = 48       # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)

# low lit
LEVEL_H0 = 10
# flash 25
LEVEL_H1 = 25
# flash 50
LEVEL_H2 = 50
# flash 75
LEVEL_H3 = 75
# flash high
LEVEL_H4 = 90
# high all lit

# high lit
LEVEL_L4 = 90
# flash 75
LEVEL_L3 = 75
# flash 50
LEVEL_L2 = 50
# flash 25
LEVEL_L1 = 25
# flash low
LEVEL_L0 = 10
# low lit

LIGHT_0_IDX = 0 # low
LIGHT_1_IDX = 1 # 25
LIGHT_2_IDX = 2 # 50
LIGHT_3_IDX = 3 # 75
LIGHT_4_IDX = 4 # high
LIGHT_5_IDX = 5 # 75
LIGHT_6_IDX = 6 # 50
LIGHT_7_IDX = 7 # 25
LIGHT_8_IDX = 8 # low
LIGHT_9_IDX = 9





# 90 4        5        6
# 75   3             7
# 50     2         8
# 25       1    9
# 10         0




OFF_COLOR = Color(0, 0, 0)
IN_TIDE_COLOR = Color(3, 77, 203) # r g b
OUT_TIDE_COLOR = Color(255, 0, 60)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
# Intialize the library (must be called once before other functions).
strip.begin()

def signalHighTide(currentPercentOfHighTide):
    if(lessThan(currentPercentOfHighTide, LEVEL_H0)):
        _signalInLow()
    elif(between(currentPercentOfHighTide, LEVEL_H0,LEVEL_H1)):
        _signalTowardH1()
    elif(between(currentPercentOfHighTide,LEVEL_H1, LEVEL_H2)):
        _signalTowardH2()
    elif(between(currentPercentOfHighTide, LEVEL_H2, LEVEL_H3)):
        _signalTowardH3()
    elif(between(currentPercentOfHighTide, LEVEL_H3, LEVEL_H4)):
        _signalTowardH4()
    elif(greaterThan(currentPercentOfHighTide, LEVEL_H4)):
        _signalInHigh()
    else:
        print("no high signals found")

def signalLowTide(tide, currentPercentOfHighTide):
    if(greaterThan(currentPercentOfHighTide, LEVEL_L4)):
        _signalOutHigh()
    elif(between(currentPercentOfHighTide, LEVEL_L3, LEVEL_L4)):
        _signalTowardL3()
    elif(between(currentPercentOfHighTide, LEVEL_L2, LEVEL_L3)):
        _signalTowardL2()
    elif (between(currentPercentOfHighTide, LEVEL_L1, LEVEL_L2)):
        _signalTowardL1()
    elif (between(currentPercentOfHighTide, LEVEL_L0, LEVEL_L1)):
        _signalTowardL0()
    elif (lessThan(currentPercentOfHighTide, LEVEL_L0)):
        _signalOutLow()
    else:
        print("no low signals found")

def between(currentPercentOfHighTide, min, max):
    return currentPercentOfHighTide > min and currentPercentOfHighTide <= max

def lessThan(currentPercentOfHighTide, min):
    return currentPercentOfHighTide <= min

def greaterThan(currentPercentOfHighTide, max):
    return currentPercentOfHighTide > max




def signalTide(tide, currentPercentOfHighTide):
    if(tide["type"] == "H"):
        signalHighTide(tide, currentPercentOfHighTide)
    else:
        signalLowTide(tide, currentPercentOfHighTide)

def _signalInLow():
    print("signal incoming low")
    _turnOffAllLights(LIGHT_0_IDX, LIGHT_0_IDX)
    _turnOnLight(LIGHT_0_IDX, IN_TIDE_COLOR)
    time.sleep(30)

def _signalTowardH1():
    print("signal incoming toward H1")
    _turnOffAllLights(LIGHT_0_IDX, LIGHT_1_IDX)
    _turnOnLight(LIGHT_0_IDX, IN_TIDE_COLOR)
    _flashLight(LIGHT_1_IDX, IN_TIDE_COLOR)

def _signalTowardH2():
    print("signal incoming toward H2")
    _turnOffAllLights(LIGHT_0_IDX, LIGHT_2_IDX)
    _turnOnLight(LIGHT_0_IDX, IN_TIDE_COLOR)
    _turnOnLight(LIGHT_1_IDX, IN_TIDE_COLOR)
    _flashLight(LIGHT_2_IDX, IN_TIDE_COLOR)

def _signalTowardH3():
    print("signal incoming toward H3")
    _turnOffAllLights(LIGHT_0_IDX, LIGHT_3_IDX)
    _turnOnLight(LIGHT_0_IDX, IN_TIDE_COLOR)
    _turnOnLight(LIGHT_1_IDX, IN_TIDE_COLOR)
    _turnOnLight(LIGHT_2_IDX, IN_TIDE_COLOR)
    _flashLight(LIGHT_3_IDX, IN_TIDE_COLOR)

def _signalTowardH4():
    print("signal incoming toward H4")
    _turnOffAllLights(LIGHT_0_IDX, LIGHT_4_IDX)
    _turnOnLight(LIGHT_0_IDX, IN_TIDE_COLOR)
    _turnOnLight(LIGHT_1_IDX, IN_TIDE_COLOR)
    _turnOnLight(LIGHT_2_IDX, IN_TIDE_COLOR)
    _turnOnLight(LIGHT_3_IDX, IN_TIDE_COLOR)
    _flashLight(LIGHT_4_IDX, IN_TIDE_COLOR)

def _signalInHigh():
    print("signal incoming high")
    _turnOffAllLights(LIGHT_4_IDX, LIGHT_6_IDX)
    _turnOnLight(LIGHT_4_IDX, IN_TIDE_COLOR)
    _turnOnLight(LIGHT_5_IDX, IN_TIDE_COLOR)
    _turnOnLight(LIGHT_6_IDX, IN_TIDE_COLOR)


# 90 4        5        6
# 75   3             7
# 50     2         8
# 25       1    9
# 10         0

def _signalOutHigh():
    print("signal out going high")
    _turnOffAllLights(LIGHT_5_IDX, LIGHT_6_IDX)
    _turnOnLight(LIGHT_5_IDX, OUT_TIDE_COLOR)
    _flashLight(LIGHT_6_IDX, OUT_TIDE_COLOR)

def _signalTowardL3():
    print("signal out going L3")
    _turnOffAllLights(LIGHT_6_IDX, LIGHT_7_IDX)
    _turnOnLight(LIGHT_6_IDX, OUT_TIDE_COLOR)
    _flashLight(LIGHT_7_IDX, OUT_TIDE_COLOR)

def _signalTowardL2():
    print("signal out going L2")
    _turnOffAllLights(LIGHT_6_IDX, LIGHT_8_IDX)
    _turnOnLight(LIGHT_6_IDX, OUT_TIDE_COLOR)
    _turnOnLight(LIGHT_7_IDX, OUT_TIDE_COLOR)
    _flashLight(LIGHT_8_IDX, OUT_TIDE_COLOR)

def _signalTowardL1():
    print("signal out going L1")
    _turnOffAllLights(LIGHT_6_IDX, LIGHT_9_IDX)
    _turnOnLight(LIGHT_6_IDX, OUT_TIDE_COLOR)
    _turnOnLight(LIGHT_7_IDX, OUT_TIDE_COLOR)
    _turnOnLight(LIGHT_8_IDX, OUT_TIDE_COLOR)
    _flashLight(LIGHT_9_IDX, OUT_TIDE_COLOR)

def _signalTowardL0():
    print("signal out going L0")
    _turnOffAllLights(LIGHT_6_IDX, LIGHT_9_IDX)
    _turnOnLight(LIGHT_6_IDX, OUT_TIDE_COLOR)
    _turnOnLight(LIGHT_7_IDX, OUT_TIDE_COLOR)
    _turnOnLight(LIGHT_8_IDX, OUT_TIDE_COLOR)
    _turnOnLight(LIGHT_9_IDX, OUT_TIDE_COLOR)
    _flashLight(LIGHT_0_IDX, OUT_TIDE_COLOR)

def _signalOutLow():
    print("signal out low")
    _turnOffAllLights(LIGHT_6_IDX, LIGHT_9_IDX)
    _turnOnLight(LIGHT_6_IDX, OUT_TIDE_COLOR)
    _turnOnLight(LIGHT_7_IDX, OUT_TIDE_COLOR)
    _turnOnLight(LIGHT_8_IDX, OUT_TIDE_COLOR)
    _turnOnLight(LIGHT_9_IDX, OUT_TIDE_COLOR)
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
        print(color)

        _turnOnLight(lightIdx, color)
        time.sleep(1)
        # _turnOffLight(lightIdx)
        time.sleep(.5)