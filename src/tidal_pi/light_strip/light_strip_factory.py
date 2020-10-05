from tidal_pi import config
import logging

logger = logging.getLogger(__name__)


def create_light_strip():
    if config.LIGHT_STRIP_TYPE == "LoggerStrip":
        logger.info("using LoggerStrip")
        from tidal_pi.light_strip.logger_light_strip import LoggerStrip
        return LoggerStrip()
    else:
        logger.info("using NeoPixelStrip")
        from tidal_pi.light_strip.neo_pixel_light_strip import NeoPixelStrip
        return NeoPixelStrip()