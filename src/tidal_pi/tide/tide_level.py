class TideLevel:
    def __init__(self, name, tide_type, percent_of_high_tide):
        self.name = name
        self.tide_type = tide_type
        self.percent_of_high_tide = percent_of_high_tide

    def get_tide_type(self):
        return self.tide_type

    def get_name(self):
        return self.name

    def get_percent_of_high_tide(self):
        return self.percent_of_high_tide

    def has_met(self, compare_to_tide_level):
        if self.get_tide_type() == compare_to_tide_level.get_tide_type():
            if self.get_tide_type() == "H":
                return compare_to_tide_level.get_percent_of_high_tide() >= self.get_percent_of_high_tide()
            else:
                return compare_to_tide_level.get_percent_of_high_tide() < self.get_percent_of_high_tide()
        else:
            return False

    def find_level(self, tide_levels):
        current_level = None
        for level in tide_levels:
            if self.has_met(level):
                if self.get_tide_type() == "H":
                    if current_level == None or level.get_percent_of_high_tide() > current_level.get_percent_of_high_tide():
                        current_level = level
                else:
                    if current_level == None or level.get_percent_of_high_tide() < current_level.get_percent_of_high_tide():
                        current_level = level

        return current_level