import sys
import datetime
import json
import tidal_pi.config as config
from tidal_pi.tide.tide import Tide


class TideChart():
    
    def __init__(self, predictions=None):
        if (predictions == None):
            self.tides = self._read_tide_chart()
        else:
            self.tides = self._build_tide_chart(predictions)
            self._write_tide_chart(self.tides)

    def get_tide_state(self):
        #  TODO



    def _build_tide_chart(self, predictions):
        tides = {}
        for prediction in predictions:
            date = datetime.datetime.strptime(prediction["t"], "%Y-%m-%d %H:%M")
            date_str = date.strftime("%Y-%m-%d")
            time_str = date.strftime("%H:%M")
            height = prediction["v"]
            type = prediction["type"]
            tide = Tide(date_str, time_str, type, height)

            if (date.weekday() not in tides):
                tides[date.weekday()] = []
            tides[date.weekday()].append(tide)
        return tides

    def _write_tide_chart(self, tide_chart):
        with open(config.TIDE_CHART_FILE, 'w+') as tide_chart_file:
            tide_chart_file.write(json.dumps(tide_chart))
    
    def _read_tide_chart(self):
        try:
            with open(config.TIDE_CHART_FILE) as tide_chart_file:
                return json.load(tide_chart_file)
        except:
            print("could not read tide forecast {}".format(tide_chart_file), sys.exc_info()[0])
            return {}

    def _sort_tides(self, tides):
        return sorted(tides, key=lambda tide: tide.get_date_time_str())

    def _get_all_tides(self):
        all_tides = []
        for index in self.tides:
            for tide in self.tides[index]:
                all_tides.append(tide)
        return all_tides

    def _get_next_tide(self, tide_type):
        predicate_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        all_tides = self.sort_tides(self._get_all_tides())
        for tide in all_tides:
            if tide.get_date_time_str() > predicate_date_time:
                return tide
        return None

    def _get_previous_tide(self):
        predicate_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        all_tides = self.sort_tides(self._get_all_tides())
        previous_tide = None
        for tide in all_tides:
            if tide.get_date_time_str() > predicate_date_time:
                return previous_tide
            previous_tide = tide
        return None