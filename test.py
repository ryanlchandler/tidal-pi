import datetime
from tide_forecast import *
from tide_gpio import *

begin_date = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%m/%d/%Y")
end_date   = (datetime.date.today() + datetime.timedelta(days=6)).strftime("%m/%d/%Y")
updateTideForecasts(begin_date, end_date)

while(True):
    forecast = getForecast()
    nextTide = getNextTide(forecast)
    prevTide = getPreviousTide(forecast)
    print("{}  {}: {}".format(prevTide["date"], prevTide["type"], prevTide["time"]))
    print("{}  {}: {}".format(nextTide["date"], nextTide["type"], nextTide["time"]))
    print("time remaining:  {} mins".format(getMinutesBeforeTide(nextTide)))
    print("percent high tide:  {}%".format(getCurrentPercentOfHighTide(prevTide, nextTide)))
    signalTide(nextTide)
    print("----------------------------")
    time.sleep(3)