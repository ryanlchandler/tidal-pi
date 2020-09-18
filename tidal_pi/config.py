import os

TIDE_URL = "https://tidesandcurrents.noaa.gov/api/datagetter"
STATION_ID = "8679083"
FORECAST_FILE = "/app/data/forecast.json"
LOW_TIDE_PIN = 16
HIGH_TIDE_PIN = 12
STRIP_TYPE = os.getenv('STRIP_TYPE', "LoggerStrip")