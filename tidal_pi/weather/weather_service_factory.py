import tidal_pi.config as config
import logging

def create_weather_service():
    if config.WEATHER_SERVICE == "LoggerWeatherService":
        logging.info("using LoggerWeatherService")
        from tidal_pi.weather.logger_weather_service import LoggerWeatherService
        return LoggerWeatherService()
    else:
        logging.info("using NoaaWeatherService")
        from tidal_pi.weather.noaa_weather_service import NoaaWeatherService
        return NoaaWeatherService()