from rpi_ws281x import *

LED_COUNT   = 48       # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)

class NeoPixelStrip():

    def __init__(self, led_count=LED_COUNT, led_pin=LED_PIN, led_freq_hz=LED_FREQ_HZ, led_dma=LED_DMA, led_invert=LED_INVERT):
        self.led_count = led_count
        self.led_pin = led_pin
        self.led_freq_hz = led_freq_hz
        self.led_dma = led_dma
        self.led_invert = led_invert
        self.strip = Adafruit_NeoPixel(self.led_count, self.led_pin, self.led_freq_hz, self.led_dma, self.led_invert)
        self.strip.begin()

    def setPixelColor(self, lightIdx, r, g, b):
        self.strip.setPixelColor(lightIdx, Color(r, g, b))

    def show(self):
        self.strip.show()
