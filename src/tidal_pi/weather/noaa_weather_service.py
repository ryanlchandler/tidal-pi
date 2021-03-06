import json
import requests
from tidal_pi import config
import logging
import sys

logger = logging.getLogger(__name__)

_product = "predictions"
_format = "json"
_units = "english"
_time_zone = "lst_ldt"
_datum = "MLLW"
_interval = "hilo"

class NoaaWeatherService():

    def fetch_tide_forecast(self, begin_date, end_date):
        logger.info("fetching noaa tide forecast for {} to {}".format(begin_date, end_date))
        try:
            url = ("%s?station=%s&begin_date=%s&end_date=%s&product=%s&format=%s&units=%s&time_zone=%s&datum=%s&interval=%s" %
                   (
                       config.TIDE_URL,
                       config.STATION_ID,
                       begin_date,
                       end_date,
                       _product,
                       _format,
                       _units,
                       _time_zone,
                       _datum,
                       _interval
                   ))
            r = requests.get(url)
            logger.debug("\n---response - start---\n{}\n---response - end---".format(r.text))
            return json.loads(r.text)["predictions"]
        except:
            logger.error("could not fetch weather", exc_info=True)



