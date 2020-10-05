import datetime
import logging

logger = logging.getLogger(__name__)

class Tide():

    def __init__(self, date, time, type, height):
        self.date = date
        self.time = time
        self.type = type
        self.height = height

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_type(self):
        return self.type

    def get_height(self):
        return self.height

    def get_date_time_str(self):
        return "{} {}".format(self.get_date(), self.get_time())

    def get_date_time(self):
        return datetime.datetime.strptime(self.get_date_time_str(), '%Y-%m-%d %H:%M')

    def to_string(self):
        return "date time: {}\ntype: {}\nheight: {}".format(self.get_date_time_str(), self.get_type(), self.get_height())
