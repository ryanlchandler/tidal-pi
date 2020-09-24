class TideStateProvider():

    def __init__(self, tide_chart):
        self.tide_chart = tide_chart

    def get_tide_state(self):
        return self.tide_chart.get_tide_state()