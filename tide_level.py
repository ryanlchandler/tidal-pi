



class TideLevel:
    def __init__(self, name, tideType, percentOfHighTide, turnOnLights, flashLights=None):
        self.name = name
        self.tideType = tideType
        self.percentOfHighTide = percentOfHighTide
        self.turnOnLights = turnOnLights
        self.flashLights = flashLights

    def hasMetLevel(self, tideType, currentPercentOfHighTide):
        if self.tideType == tideType:
            if tideType == "H":
                return currentPercentOfHighTide > self.percentOfHighTide
            else:
                return currentPercentOfHighTide < self.percentOfHighTide
        else:
            return False

    def getTurnOnLights(self):
        return self.turnOnLights

    def getFlashLights(self):
        return self.flashLights

