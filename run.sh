#!/bin/bash

echo "-----------------------------------------"
echo "               Running"
echo "-----------------------------------------"

LIGHT_STRIP_TYPE="${LIGHT_STRIP_TYPE:-LoggerStrip}"
WEATHER_SERVICE="${WEATHER_SERVICE:-LoggerWeatherService}"
CLOCK_TYPE="${CLOCK_TYPE:-LoggerClock}"
LOG_LEVEL="${LOG_LEVEL:-INFO}"
RUN_TESTS="${RUN_TESTS:-false}"
TZ="${TZ:-America/New_York}"

docker rm --force tidalpi

docker run \
-v /var/log/pi:/app/log \
-v /var/data:/app/data \
-v /usr/sbin:/usr/sbin \
--privileged \
--env LIGHT_STRIP_TYPE=$LIGHT_STRIP_TYPE \
--env WEATHER_SERVICE=$WEATHER_SERVICE \
--env CLOCK_TYPE=$CLOCK_TYPE \
--env LOG_LEVEL=$LOG_LEVEL \
--env RUN_TESTS=$RUN_TESTS \
--env TZ=$TZ \
--detach \
--name tidalpi tidalpi:1.0