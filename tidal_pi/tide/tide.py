import datetime

class Tide():

    def __init__(self, date, time, type, height):
        self.data = date
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
        return "{} {}".format(self.date, self.time),

    def get_date_time(self):
        return datetime.datetime.strptime(self.get_date_time_str(), '%Y-%m-%d %H:%M')
