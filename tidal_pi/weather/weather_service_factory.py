import tidal_pi.config as config

def create_weather_service():
    if config.WEATHER_SERVICE == "LoggerWeatherService":
        print("using LoggerWeatherService")
        from tidal_pi.weather.logger_weather_service import LoggerWeatherService
        return LoggerWeatherService()
    else:
        print("using NoaaWeatherService")
        from tidal_pi.weather.noaa_weather_service import NoaaWeatherService
        return NoaaWeatherService()