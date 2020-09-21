import tidal_pi.config as config


def create_light_strip():
    if config.LIGHT_STRIP_TYPE == "LoggerStrip":
        print("using LoggerStrip")
        from tidal_pi.light_strip.logger_light_strip import LoggerStrip
        return LoggerStrip()
    else:
        print("using NeoPixelStrip")
        from tidal_pi.light_strip.neo_pixel_light_strip import NeoPixelStrip
        return NeoPixelStrip()