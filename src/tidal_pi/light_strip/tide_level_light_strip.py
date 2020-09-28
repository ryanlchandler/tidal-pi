from tidal_pi.tide.tide_level import TideLevel
from tidal_pi.light_strip.light_strip_factory import create_light_strip
from tidal_pi.light_strip.tide_level_light_config import *
import logging
import sys
import time

class TideLevelLightStrip():

    def __init__(self):
        self.light_strip = create_light_strip()
        self.high_tide_levels = [
            # low IN
            TideLevel("low tide", "H", 0),
            TideLevel("level 13", "H", 13),
            TideLevel("level 25", "H", 25),
            TideLevel("level 38", "H", 38),
            TideLevel("level 50", "H", 50),
            TideLevel("level 63", "H", 63),
            TideLevel("level 75", "H", 75),
            TideLevel("level 83", "H", 83),
            TideLevel("level 90", "H", 90),
            TideLevel("level 95", "H", 95),
            # high IN
        ]
        self.low_tide_levels = [
            # high OUT
            TideLevel("high tide", "L", 100),
            TideLevel("level 95",  "L",  95),
            TideLevel("level 90",  "L",  90),
            TideLevel("level 83",  "L",  83),
            TideLevel("level 75",  "L",  75),
            TideLevel("level 63",  "L",  63),
            TideLevel("level 50",  "L",  50),
            TideLevel("level 38",  "L",  38),
            TideLevel("level 25",  "L",  25),
            TideLevel("level 13",  "L",  13)
            # low OUT
        ]        

    def render(self, tide_state):
        if (tide_state.get_current_tide_level().get_tide_type() == "H"):
            self._render_tide_coming_in(tide_state)
        else:
            self._render_tide_going_out(tide_state)

    def _render_tide_coming_in(self, tide_state):
        current_level = tide_state.get_current_tide_level().find_level(self.high_tide_levels)
        logging.info("current tide level: {} - {}".format(current_level.get_tide_type(), current_level.get_name()))
        self._render_light_strip(
            HIGH_TIDE_LEVEL_LIGHTS_ON.get(current_level.get_percent_of_high_tide()),
            HIGH_TIDE_LEVEL_LIGHTS_FLASHING.get(current_level.get_percent_of_high_tide()),
            IN_TIDE_COLOR
        )

    def _render_tide_going_out(self, tide_state):
        current_level = tide_state.get_current_tide_level().find_level(self.low_tide_levels)
        logging.info("current tide level: {} - {}".format(current_level.get_tide_type(), current_level.get_name()))
        self._render_light_strip(
            LOW_TIDE_LEVEL_LIGHTS_ON.get(current_level.get_percent_of_high_tide()),
            LOW_TIDE_LEVEL_LIGHTS_FLASHING.get(current_level.get_percent_of_high_tide()),
            OUT_TIDE_COLOR
        )

    def _render_light_strip(self, on_lights, flashing_lights, light_color):
        self._turn_off_lights(on_lights)

        for lightIdx in on_lights:
            self._turn_on_light(lightIdx, light_color)

        self._update_strip()

        if flashing_lights != None:
            self._flash_lights(flashing_lights, light_color)

    def _turn_off_lights(self, leave_on):
        for i in range(48):
            if(i not in leave_on):
                self._turn_off_light(i)

    def _turn_on_light(self, light_idx, color, brightness=255):
        r = color.get_r(brightness)
        g = color.get_g(brightness)
        b = color.get_b(brightness)
        try:
            logging.debug("turning on light {} - ({},{},{})".format(light_idx, r, g, b))
            self.light_strip.set_pixel_color(light_idx, r, g, b)
        except:
            logging.error("could not turn on light {}".format(light_idx), sys.exc_info()[0])

    def _turn_off_light(self, light_idx):
        r = OFF_COLOR.get_r()
        g = OFF_COLOR.get_g()
        b = OFF_COLOR.get_b()
        try:
            logging.debug("turning off light {} - ({},{},{})".format(light_idx, r, g, b))
            self.light_strip.set_pixel_color(light_idx, r, g, b)
        except:
            logging.error("could not turn off light {}".format(light_idx), sys.exc_info()[0])

    def _update_strip(self):
        try:
            self.light_strip.show()
        except:
            logging.error("could not show lights", sys.exc_info()[0])

    def _turn_on_lights(self, light_idxs, color, birghtness):
        for light_idx in light_idxs:
            self._turn_on_light(light_idx, color, birghtness)

    def _flash_lights(self, flash_lights, color):
        self._turn_up_brightness(flash_lights, color, 255, 1, 0)
        time.sleep(.3)
        self._turn_down_brightness(flash_lights, color, 255, 1, 0)
        time.sleep(.3)

    def _turn_up_brightness(self, lights, color, steps, step_factor, sleep):
        for step in range(steps):
            self._turn_on_lights(lights, color, (step * step_factor))
            self._update_strip()
            time.sleep(sleep)

    def _turn_down_brightness(self, lights, color, steps, step_factor, sleep):
        for step in range(steps):
            self._turn_on_lights(lights, color, 255 - (step * step_factor))
            self._update_strip()
            time.sleep(sleep)