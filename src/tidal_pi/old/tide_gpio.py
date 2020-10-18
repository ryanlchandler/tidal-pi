from tidal_pi import TideLevel

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

forecast = None
nextTide = None
prevTide = None
currentPercentOfHighTide = None

def runTideLightUpdateJob(strip):
    t1 = Thread(target=tideLightUpdateJob, args=[strip])
    t2 = Thread(target=tideDataUpdateJob)
    t1.start()
    t2.start()
    return [t1, t2]

def tideDataUpdateJob():
    global forecast
    global nextTide
    global prevTide
    global currentPercentOfHighTide
    while (True):
        forecast = getForecast()
        if forecast != None:
            nextTide = getNextTide(forecast)
            prevTide = getPreviousTide(forecast)
            currentPercentOfHighTide = getCurrentPercentOfHighTide(prevTide, nextTide)
            print("{}  {}: {}".format(prevTide["date"], prevTide["type"], prevTide["time"]))
            print("{}  {}: {}".format(nextTide["date"], nextTide["type"], nextTide["time"]))
            print("time remaining:  {} mins".format(getMinutesBeforeTide(nextTide)))
            print("percent high tide:  {}%".format(currentPercentOfHighTide))
            print("----------------------------")
            sys.stdout.flush()
        else:
            print("no forecast")
        time.sleep(1)

def tideLightUpdateJob(strip):
    global nextTide
    global currentPercentOfHighTide
    while(True):
        if nextTide != None and currentPercentOfHighTide != None:
            signalTide(strip, nextTide, currentPercentOfHighTide)
        time.sleep(1)

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
IN_TIDE_COLOR = Kolor(0, 0, 255) # r g b
OUT_TIDE_COLOR = Kolor(255, 0, 0)

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

def signalTide(strip, tide, currentPercentOfHighTide):
    if (tide["type"] == "H"):
        _signalInTide(strip, currentPercentOfHighTide)
    else:
        _signalOutTide(strip, currentPercentOfHighTide)

def _signalInTide(strip, currentPercentOfHighTide):
    lightColor = IN_TIDE_COLOR
    currentLevel = None
    for level in highTideLevels:
        if level.hasMetLevel("H", currentPercentOfHighTide):
            if currentLevel == None or level.getPercentOfHighTide() > currentLevel.getPercentOfHighTide():
                currentLevel = level
    print("signal H {}".format(currentLevel.getName()))
    _updateLights(strip, currentLevel.getTurnOnLights(), currentLevel.getFlashLights(), lightColor)

def _signalOutTide(strip, currentPercentOfHighTide):
    lightColor = OUT_TIDE_COLOR
    currentLevel = None
    for level in lowTideLevels:
        if level.hasMetLevel("L", currentPercentOfHighTide):
            if currentLevel == None or level.getPercentOfHighTide() < currentLevel.getPercentOfHighTide():
                currentLevel = level
    print("signal L {}".format(currentLevel.getName()))
    _updateLights(strip, currentLevel.getTurnOnLights(), currentLevel.getFlashLights(), lightColor)

def _updateLights(strip, onLights, flashLights, lightColor):
    _turnOffLights(strip, onLights)

    for lightIdx in onLights:
        _turnOnLight(strip, lightIdx, lightColor)
    _updateStrip(strip)

    if flashLights != None:
        _flashLights(strip, flashLights, lightColor)

def _turnOffLights(strip, leaveOn):
    for i in range(48):
        if(i not in leaveOn):
            _turnOffLight(strip, i)

def _turnOnLight(strip, lightIdx, color, brightness=255):
    try:
        print("turning on light {} - ({},{},{})".format(lightIdx, (brightness * color["r"] / 255), (brightness * color["g"] / 255), (brightness * color["b"] / 255)))
        strip.setPixelColor(lightIdx, (brightness * color["r"] / 255), (brightness * color["g"] / 255), (brightness * color["b"] / 255))
    except:
        print("could not turn on light {}".format(lightIdx), exc_info=True)

def _turnOffLight(strip, lightIdx):
    try:
        print("turning off light {} - ({},{},{})".format(lightIdx, OFF_COLOR["r"], OFF_COLOR["g"], OFF_COLOR["b"]))
        strip.setPixelColor(lightIdx, OFF_COLOR["r"], OFF_COLOR["g"], OFF_COLOR["b"])
    except:
        print("could not turn off light {}".format(lightIdx), exc_info=True)

def _updateStrip(strip):
    try:
        strip.show()
    except:
        print("could not show lights", exc_info=True)

def _turnOnLights(strip, lightIdxs, color, birghtness):
    for lightIdx in lightIdxs:
        _turnOnLight(strip, lightIdx, color, birghtness)

def _flashLights(strip, flashLights, color):
    _turnUpBrightness(strip, flashLights, color, 255, 1, 0)
    time.sleep(.3)
    _turnDownBrightness(strip, flashLights, color, 255, 1, 0)
    time.sleep(.3)

def _turnUpBrightness(strip, lights, color, steps, stepFactor, sleep):
    for step in range(steps):
        _turnOnLights(strip, lights, color, (step * stepFactor))
        _updateStrip(strip)
        time.sleep(sleep)

def _turnDownBrightness(strip, lights, color, steps, stepFactor, sleep):
    for step in range(steps):
        _turnOnLights(strip, lights, color, 255 - (step * stepFactor))
        _updateStrip(strip)
        time.sleep(sleep)



