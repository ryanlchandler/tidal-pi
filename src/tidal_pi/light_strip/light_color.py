class LightColor():

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def get_r(self, brightness=255):
        return (brightness * self.r / 255)

    def get_g(self, brightness=255):
        return (brightness * self.g / 255)

    def get_b(self, brightness=255):
        return (brightness * self.b / 255)