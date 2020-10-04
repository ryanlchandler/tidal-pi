import datetime
from tidal_pi.tide.tide_level import TideLevel

class TideState():

    def __init__(self, previous_tide, next_tide, next_high_tide, next_low_tide, from_date_time=None):
        if (from_date_time == None):
            from_date_time = datetime.datetime.now()
        else:
            from_date_time = datetime.datetime.strptime(from_date_time, '%Y-%m-%d %H:%M')

        self.previous_tide = previous_tide
        self.next_tide = next_tide
        self.next_high_tide = next_high_tide
        self.next_low_tide = next_low_tide
        self.current_tide_level = TideLevel(
            "current tide",
            next_tide.get_type(),
            TideState._get_current_percent_of_high_tide(next_tide, previous_tide, from_date_time)
        )

    def get_previous_tide(self):
        return self.previous_tide

    def get_next_tide(self):
        return self.next_tide

    def get_next_high_tide(self):
        return self.next_high_tide

    def get_next_low_tide(self):
        return self.next_low_tide

    def get_current_tide_level(self):
        return self.current_tide_level

    def _get_current_percent_of_high_tide(next_tide, prev_tide, predicate_date_time=None):
        minutes_between = TideState._get_minutes_between_tides(next_tide, prev_tide)
        minutes_before = TideState._get_minutes_before_tide(next_tide, predicate_date_time)

        percent_of_high = ((minutes_between - minutes_before) / minutes_between) * 100
        if (next_tide.get_type() == "L"):
            percent_of_high = 100 - percent_of_high
        return round(percent_of_high, 2)

    def _get_minutes_between_tides(tide1, tide2):
        return round((tide1.get_date_time() - tide2.get_date_time()).total_seconds() / 60, 2)

    def _get_minutes_before_tide(tide, predicate_date_time=None):
        if (predicate_date_time == None):
            predicate_date_time = datetime.datetime.now()
        return round((tide.get_date_time() - predicate_date_time).total_seconds() / 60, 2)



