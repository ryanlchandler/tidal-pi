import datetime
from tidal_pi.weather.weather_service_factory import create_weather_service

class WeatherUpdateJob():

    def __init__(self, tide_chart):
        self.weather_service = create_weather_service()
        self.tide_chart = tide_chart

    def run(self):
        begin_date = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%m/%d/%Y")
        end_date = (datetime.date.today() + datetime.timedelta(days=6)).strftime("%m/%d/%Y")
        tide_forecast = self.weather_service.fetch_tide_forecast(begin_date, end_date)
        self.tide_chart.update(tide_forecast)