import logging

logger = logging.getLogger(__name__)

class TideStateProvider():

    def __init__(self, tide_chart):
        self.tide_chart = tide_chart

    def get_tide_state(self):
        ts = self.tide_chart.get_tide_state()
        import datetime

        x = datetime.datetime.now()
        print(x)


        logger.debug("providing tide state: \n   now: {}\n   previous_tide: {}\n   next_tide: {}\n   next_high_tide: {}\n   next_low_tide: {}\n   current_tide_level: {} - {}"
                    .format(
                        datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                        ts.get_previous_tide().get_date_time_str(),
                        ts.get_next_tide().get_date_time_str(),
                        ts.get_next_high_tide().get_date_time_str(),
                        ts.get_next_low_tide().get_date_time_str(),
                        ts.get_current_tide_level().get_percent_of_high_tide(),
                        ts.get_current_tide_level().get_tide_type()
                    ))
        return ts