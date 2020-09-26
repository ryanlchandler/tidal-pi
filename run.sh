#!/bin/bash

echo "-----------------------------------------"
echo "               Running"
echo "-----------------------------------------"

LIGHT_STRIP_TYPE="${LIGHT_STRIP_TYPE:-LoggerStrip}"
WEATHER_SERVICE="${WEATHER_SERVICE:-LoggerWeatherService}"
CLOCK_TYPE="${CLOCK_TYPE:-LoggerClock}"
LOG_LEVEL="${LOG_LEVEL:-INFO}"

docker rm --force tidalpi

docker run \
-v /var/log/pi:/app/log \
-v /var/data:/app/data \
--privileged \
--env LIGHT_STRIP_TYPE=$LIGHT_STRIP_TYPE \
--env WEATHER_SERVICE=$WEATHER_SERVICE \
--env CLOCK_TYPE=$CLOCK_TYPE \
--env LOG_LEVEL=$LOG_LEVEL \
--detach \
--name tidalpi tidalpi:1.0