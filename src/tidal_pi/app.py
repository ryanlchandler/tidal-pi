from tidal_pi.tide.tide_state_provider import TideStateProvider
from tidal_pi.clock.clock_job import ClockJob
from tidal_pi.weather.weather_update_job import WeatherUpdateJob
from tidal_pi.light_strip.light_strip_job import LightStripJob
from tidal_pi.tide.tide_chart import TideChart
from tidal_pi.light_strip.tide_level_light_strip import TideLevelLightStrip
from tidal_pi.job_runner import JobRunner
from tidal_pi.config import LOG_LEVEL
from tidal_pi.config import RUN_TESTS
import logging
import sys
import pytest

logger = logging.getLogger(__name__)


def start():
    if(RUN_TESTS.lower() == "true"):
        TidalPi().run_tests()
    else:
        TidalPi().run()


class TidalPi():

    def run_tests(self):
        logger.info("running tests...")
        pytest.main(["-x", "tests"])
        logger.info("tests finished")

    def run(self):
        self._configure_logging()
        logger.info("TidalPi starting")

        # weather
        tide_chart = TideChart()
        tide_state_provider = TideStateProvider(tide_chart)
        weather_update_job = WeatherUpdateJob(tide_chart)

        # light strip
        light_strip_job = LightStripJob(tide_state_provider, TideLevelLightStrip())

        # clocks
        clock_job = ClockJob(tide_state_provider)

        threads = []
        threads.append(JobRunner("weather update job", weather_update_job, 60 * 60).start())
        threads.append(JobRunner("light strip job", light_strip_job, 1).start())
        threads.append(JobRunner("tide clock", clock_job, 1).start())

        logger.info("TidalPi running")
        for thread in threads:
            thread.join()


    def _configure_logging(self):
        root = logging.getLogger()
        root.setLevel(self._get_log_level())

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(self._get_log_level())
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        root.addHandler(handler)
        logging.getLogger("tidal_pi.light_strip.tide_level_light_strip").setLevel(logging.INFO)

    def _get_log_level(self):
        if(LOG_LEVEL.upper() == "INFO"):
            return logging.INFO
        elif(LOG_LEVEL.upper() == "DEBUG"):
            return logging.DEBUG
        elif(LOG_LEVEL.upper() == "WARN"):
            return logging.WARN
        elif(LOG_LEVEL.upper() == "ERROR"):
            return logging.ERROR
        else:
            return logging.INFO