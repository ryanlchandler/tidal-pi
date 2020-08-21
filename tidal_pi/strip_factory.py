from tidal_pi.config import *

def build_strip():
    if STRIP_TYPE == "LoggerStrip":
        print("using LoggerStrip")
        from tidal_pi.logger_strip import LoggerStrip
        return LoggerStrip()
    else:
        print("using NeoPixelStrip")
        from tidal_pi.neo_pixel_strip import NeoPixelStrip
        return NeoPixelStrip()