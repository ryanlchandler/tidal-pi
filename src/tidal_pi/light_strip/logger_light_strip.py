import logging

class LoggerStrip():

    def set_pixel_color(self, lightIdx, r, g, b):
        logging.info("strip.set_pixel_color({}, r({}), g({}), b({}))".format(lightIdx, r, g, b))

    def show(self):
        logging.info("strip.show()")