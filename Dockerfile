FROM python:3

COPY . /app

WORKDIR /app/Adafruit_Python_LED_Backpack
RUN python setup.py install
WORKDIR /app
RUN pip install rpi_ws281x adafruit-circuitpython-neopixel
USER root
RUN pip install adafruit-blinka
RUN pip install -r requirements.txt .

CMD tidalpi > /app/log/tidalpi.log 2>&1
