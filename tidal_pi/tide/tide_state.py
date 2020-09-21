class TideState():

    def __init__(self, previous_tide, next_tide, current_tide_level):
        self.previous_tide = previous_tide
        self.next_tide = next_tide

        self.current_tide_level = current_tide_level

    def get_previous_tide(self):
        return self.previous_tide

    def get_next_tide(self):
        return self.next_tide

    def get_current_tide_level(self):
        return self.current_tide_level

    

    def _get_current_percent_of_high_tide(self):
        minutesBetween = getMinutesBetweenTides(nextTide, prevTide)
        minutesBefore = getMinutesBeforeTide(nextTide)

        percentOfHigh = ((minutesBetween - minutesBefore) / minutesBetween) * 100
        if (nextTide["type"] == "L"):
            percentOfHigh = 100 - percentOfHigh

        return round(percentOfHigh, 2)



