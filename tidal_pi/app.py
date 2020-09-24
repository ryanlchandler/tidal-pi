from tidal_pi.tide.tide_state_provider import TideStateProvider
from tidal_pi.clock.high_tide_clock_job import HighTideClockJob
from tidal_pi.clock.low_tide_clock_job import LowTideClockJob
from tidal_pi.weather.weather_update_job import WeatherUpdateJob
from tidal_pi.light_strip.light_strip_job import LightStripJob
from tidal_pi.tide.tide_chart import TideChart
from tidal_pi.light_strip.tide_level_light_strip import TideLevelLightStrip
from tidal_pi.job_runner import JobRunner


def start():
    TidalPi().run()

class TidalPi():
    def run(self):
        # weather
        tide_chart = TideChart()
        tide_state_provider = TideStateProvider(tide_chart)
        weather_update_job = WeatherUpdateJob(tide_chart)

        # light strip
        light_strip_job = LightStripJob(tide_state_provider, TideLevelLightStrip())

        # clocks
        high_tide_clock_job = HighTideClockJob(tide_state_provider)
        low_tide_clock_job = LowTideClockJob(tide_state_provider)

        threads = []
        threads.append(JobRunner(weather_update_job, 60 * 60))
        threads.append(JobRunner(light_strip_job, 1))
        threads.append(JobRunner(high_tide_clock_job, 1))
        threads.append(JobRunner(low_tide_clock_job, 1))

        for thread in threads:
            thread.join()