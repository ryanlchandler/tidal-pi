import logging

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
        if self.get_tide_type() == "H":
            found_tide = self._find_highest(tide_levels)
        else:
            found_tide = self._find_lowest(tide_levels)

        logging.debug("=== looking through tides ===")
        for level in tide_levels:
            logging.debug("{}\n----------------------------".format(level))
        logging.debug("=============================")

        logging.debug("=== found tide ===\n{}\n=============================".format(found_tide.to_string()))
        return found_tide

    def to_string(self):
        return "name: {}\ntype: {}\npercent of high tide: {}".format(self.get_name(), self.get_tide_type(), self.get_percent_of_high_tide())

    def _find_highest(self, tide_levels):
        logging.debug("find highest")
        found_level = None
        for level in tide_levels:
            if self.has_met(level):
                if found_level == None or level.get_percent_of_high_tide() > found_level.get_percent_of_high_tide():
                    found_level = level
        return found_level

    def _find_lowest(self, tide_levels):
        logging.debug("find lowest")
        found_level = None
        for level in tide_levels:
            if self.has_met(level):
                if found_level == None or level.get_percent_of_high_tide() < found_level.get_percent_of_high_tide():
                    found_level = level
        return found_level