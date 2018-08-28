import datetime

def newTide(date, time, type, height):
    return {
        "date": date,
        "time": time,
        "dateTimeStr": "{} {}".format(date, time),
        "type": type,
        "height": height
    }

def sortTides(tides):
    return sorted(tides, key=lambda k: k["dateTimeStr"])

def _getAllTides(forecast):
    allTides = []
    for index in forecast:
        tides = forecast[index]
        for tide in tides:
            allTides.append(tide)
    return allTides

def getNextTide(forecast, predicateDateTime = None):
    if(predicateDateTime == None):
        predicateDateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    allTides = sortTides(_getAllTides(forecast))
    for tide in allTides:
        if tide["dateTimeStr"] > predicateDateTime:
            return tide
    return None

def getPreviousTide(forecast, predicateDateTime = None):
    if(predicateDateTime == None):
        predicateDateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    allTides = sortTides(_getAllTides(forecast))
    previousTide = None
    for tide in allTides:
        if tide["dateTimeStr"] > predicateDateTime:
            return previousTide
        previousTide = tide
    return None

def getTideDateTime(tide):
    return datetime.datetime.strptime(tide["dateTimeStr"], '%Y-%m-%d %H:%M')

def getMinutesBetweenTides(tide1, tide2):
    return round((getTideDateTime(tide1) - getTideDateTime(tide2)).total_seconds() / 60, 2)

def getMinutesBeforeTide(tide, predicateDateTime = None):
    if(predicateDateTime == None):
        predicateDateTime = datetime.datetime.now()

    return round((getTideDateTime(tide) - predicateDateTime).total_seconds() / 60, 2)

def getCurrentPercentOfHighTide(prevTide, nextTide):
    minutesBetween = getMinutesBetweenTides(nextTide, prevTide)
    minutesBefore = getMinutesBeforeTide(nextTide)

    percentOfHigh = ((minutesBetween - minutesBefore) / minutesBetween) * 100
    if(nextTide["type"] == "L"):
        percentOfHigh = 100 - percentOfHigh

    return round(percentOfHigh, 2)

def walkTides(forecast):
    allTides = sortTides(_getAllTides(forecast))

    for tide in allTides:
        predicateDateTime = tide["dateTimeStr"]
        nextTide = getNextTide(forecast, predicateDateTime)
        prevTide = getPreviousTide(forecast, predicateDateTime)

        if(prevTide != None):
            print("{} -> {}  {}: {}".format(predicateDateTime, prevTide["date"], prevTide['type'], prevTide['time']))
        else:
            print("{} -> None".format(predicateDateTime))

        if(nextTide != None):
            print("{} -> {}  {}: {}".format(predicateDateTime, nextTide["date"], nextTide['type'], nextTide['time']))
        else:
            print("{} -> None".format(predicateDateTime))

        print("-------------------------------------------------")





