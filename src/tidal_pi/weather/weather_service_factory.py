from tidal_pi import config
import logging

logger = logging.getLogger(__name__)

def create_weather_service():
    if config.WEATHER_SERVICE == "LoggerWeatherService":
        logger.info("using LoggerWeatherService")
        from tidal_pi.weather.logger_weather_service import LoggerWeatherService
        return LoggerWeatherService()
    else:
        logger.info("using NoaaWeatherService")
        from tidal_pi.weather.noaa_weather_service import NoaaWeatherService
        return NoaaWeatherService()