import os

# weather
TIDE_URL = "https://tidesandcurrents.noaa.gov/api/datagetter"
STATION_ID = "8679083"
TIDE_CHART_FILE = "/app/data/tide_chart.json"

# light strip
LOW_TIDE_PIN = 16
HIGH_TIDE_PIN = 12
LIGHT_STRIP_TYPE = os.getenv('STRIP_TYPE', "LoggerStrip")

# clock
CLOCK_TYPE = os.getenv('CLOCK_TYPE', "LoggerClock")
HIGH_TIDE_CLOCK_ADDRESS=0x70
LOW_TIDE_CLOCK_ADDRESS=0x71