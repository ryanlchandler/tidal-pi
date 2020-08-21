class LoggerStrip():

    def setPixelColor(self, lightIdx, r, g, b):
        print("strip.setPixelColor({}, r({}), g({}), b({}))".format(lightIdx, r, g, b))

    def show(self):
        print("strip.show()")