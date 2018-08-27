import json
import requests
import datetime
from config import *
from tide import *

def updateTideForecasts(begin_date, end_date):
    predictions = _getTidePredictions(begin_date, end_date)
    tides = {}
    for prediction in predictions:
        date = datetime.datetime.strptime(prediction["t"], "%Y-%m-%d %H:%M")
        date_str = date.strftime("%Y-%m-%d")
        time_str = date.strftime("%H:%M")
        height = prediction["v"]
        type = prediction["type"]
        tide = newTide(date_str, time_str, type, height)

        if (date.weekday() not in tides):
            tides[date.weekday()] = []
        tides[date.weekday()].append(tide)

    _writeForecast(tides)

def _getTidePredictions(begin_date, end_date):
    product = "predictions"
    format = "json"
    units = "english"
    time_zone = "lst_ldt"
    datum = "MLLW"
    interval = "hilo"
    url = ("%s?station=%s&begin_date=%s&end_date=%s&product=%s&format=%s&units=%s&time_zone=%s&datum=%s&interval=%s" % (TIDE_URL, STATION_ID, begin_date, end_date, product, format, units, time_zone, datum, interval))
    r = requests.get(url)
    return json.loads(r.text)["predictions"]

def _writeForecast(forecast):
    with open(FORECAST_FILE, 'w+') as forecastFile:
        forecastFile.write(json.dumps(forecast))

def _readForecast():
    with open(FORECAST_FILE) as forecastFile:
        return json.load(forecastFile)

def getForecast(dayOfWeek):
    tides = _readForecast()
    return tides[str(dayOfWeek)]

def getTodaysForecast():
    return getForecast(str(datetime.date.today().weekday()))

def getMonForecast():
    return getForecast("0")

def getTueForecast():
    return getForecast("1")

def getWedForecast():
    return getForecast("2")

def getThurForecast():
    return getForecast("3")

def getFriForecast():
    return getForecast("4")

def getSatForecast():
    return getForecast("5")

def getSunForecast():
    return getForecast("6")

def _printForecast(tides):
    print("--- {}---".format(tides[0]["date"]))
    for tide in tides:
        _printTide(tide)

def _printTide(tide):
    print("{}: {}".format(tide["type"], tide["time"]))

# begin_date = datetime.date.today().strftime("%m/%d/%Y")
# end_date = (datetime.date.today() + datetime.timedelta(days=6)).strftime("%m/%d/%Y")
# updateTideForecasts(begin_date, end_date)

# _printForecast(getMonForecast())
# _printForecast(getTueForecast())
# _printForecast(getWedForecast())


_printTide(getNextTide(getTodaysForecast()))


