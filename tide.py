import datetime
from operator import itemgetter, attrgetter

def newTide(date, time, type, height):
    return {
        "date": date,
        "time": time,
        "type": type,
        "height": height
    }

def sortTides(tides):
    return sorted(tides, key=lambda k: k['time'])

def getNextTide(tides):
    tides = sortTides(tides)
    currentDate = datetime.datetime.now().strftime("%Y-%m-%d")
    currentTime = datetime.datetime.now().strftime("%H:%M")
    for tide in tides:
        if tide["date"] >= currentDate and tide["time"] >= currentTime:
            return tide
    return None







