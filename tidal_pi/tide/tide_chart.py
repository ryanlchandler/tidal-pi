import sys
import datetime
import json
import tidal_pi.config as config
import logging
from tidal_pi.tide.tide import Tide
from tidal_pi.tide.tide_state import TideState


class TideChart():
    
    def __init__(self):
        self.tides = self._read_tide_chart()

    def update(self, predictions):
        self.tides = self._build_tide_chart(predictions)
        self._write_tide_chart(self.tides)

    def get_tide_state(self):
        return TideState(self._get_previous_tide(), self._get_next_tide(), self._get_next_tide("H"), self._get_next_tide("L"))

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

    def _write_tide_chart(self, tides):
        try:
            logging.info("-writing {} tides to {}".format(len(tides), config.TIDE_CHART_FILE))
            tide_dict = {}
            for index in tides:
                tide_dict[index] = []
                for tide in tides[index]:
                    tide_dict[index].append(tide.__dict__)

            tides_json = json.dumps(tide_dict)
            logging.debug("writing {}".format(tides_json))
            with open(config.TIDE_CHART_FILE, 'w+') as tide_chart_file:
                tide_chart_file.write(tides_json)
                logging.info("wrote {} tides to {}".format(len(tides), config.TIDE_CHART_FILE))
        except:
            logging.error("could not write tide forecast {}".format(config.TIDE_CHART_FILE), sys.exc_info()[0])

    def _read_tide_chart(self):
        try:
            with open(config.TIDE_CHART_FILE) as tide_chart_file:
                tides_dict = json.load(tide_chart_file)
                tides = {}
                for index in tides_dict:
                    tides[index] = []
                    for tide in tides_dict[index]:
                        tides[index].append(Tide(tide["date"], tide["time"], tide["type"], tide["height"]))
                return tides
        except:
            logging.error("could not read tide forecast {}".format(config.TIDE_CHART_FILE), sys.exc_info()[0])
            return {}

    def _sort_tides(self, tides):
        return sorted(tides, key=lambda tide: tide.get_date_time_str())

    def _get_all_tides(self):
        all_tides = []
        for index in self.tides:
            for tide in self.tides[index]:
                all_tides.append(tide)
        return all_tides

    def _get_next_tide(self, tide_type=None):
        predicate_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        all_tides = self._sort_tides(self._get_all_tides())
        for tide in all_tides:
            if tide.get_date_time_str() > predicate_date_time:
                if (tide_type == None or tide_type == tide.get_type()):
                    return tide

        return None

    def _get_previous_tide(self):
        predicate_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        all_tides = self._sort_tides(self._get_all_tides())
        previous_tide = None
        for tide in all_tides:
            if tide.get_date_time_str() > predicate_date_time:
                return previous_tide
            previous_tide = tide
        return None