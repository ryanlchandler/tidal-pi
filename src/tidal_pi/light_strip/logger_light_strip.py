import logging
logger = logging.getLogger(__name__)

class LoggerStrip():

    def set_pixel_color(self, lightIdx, r, g, b):
        logger.info("strip.set_pixel_color({}, r({}), g({}), b({}))".format(lightIdx, r, g, b))

    def show(self):
        logger.info("strip.show()")