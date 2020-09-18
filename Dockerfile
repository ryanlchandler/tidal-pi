FROM python:3

COPY . /app

WORKDIR /app/Adafruit_Python_LED_Backpack
RUN python3 setup.py install
WORKDIR /app
RUN pip3 install rpi_ws281x adafruit-circuitpython-neopixel
USER root
RUN pip3 install adafruit-blinka
RUN pip3 install setuptools
RUN pip3 install -r requirements.txt .

CMD tidalpi > /app/log/tidalpi.log 2>&1
