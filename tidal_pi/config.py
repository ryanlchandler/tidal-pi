import os

# general
LOG_LEVEL = os.getenv('LOG_LEVEL', "DEBUG")

# weather
TIDE_URL = "https://tidesandcurrents.noaa.gov/api/datagetter"
STATION_ID = "8679083"
TIDE_CHART_FILE = "/app/data/tide_chart.json"
WEATHER_SERVICE = os.getenv('WEATHER_SERVICE', "LoggerWeatherService")

# light strip
LOW_TIDE_PIN = 16
HIGH_TIDE_PIN = 12
LIGHT_STRIP_TYPE = os.getenv('LIGHT_STRIP_TYPE', "LoggerStrip")

# clock
CLOCK_TYPE = os.getenv('CLOCK_TYPE', "LoggerClock")
HIGH_TIDE_CLOCK_ADDRESS=0x70
LOW_TIDE_CLOCK_ADDRESS=0x71