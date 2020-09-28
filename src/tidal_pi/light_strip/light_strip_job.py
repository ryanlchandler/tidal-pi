import time

class LightStripJob():

    def __init__(self, tide_state_provider, tide_level_light_strip):
        self.tide_level_light_strip = tide_level_light_strip
        self.tide_state_provider = tide_state_provider

    def run(self):
        while (True):
            tide_state = self.tide_state_provider.get_tide_state()
            self.tide_level_light_strip.render(tide_state)
            time.sleep(1)



