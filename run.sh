#!/bin/bash

STRIP_TYPE="${STRIP_TYPE:-LoggerStrip}"
WEATHER_SERVICE="${WEATHER_SERVICE:-LoggerWeatherService}"
CLOCK_TYPE="${CLOCK_TYPE:-LoggerClock}"
LOG_LEVEL="${LOG_LEVEL:-INFO}"

echo "STRIP_TYPE=$STRIP_TYPE"

docker rm --force tidalpi
docker run \
-v /var/log/pi:/app/log \
-v /var/data:/app/data \
--privileged \
--env STRIP_TYPE=$STRIP_TYPE \
--env WEATHER_SERVICE=$WEATHER_SERVICE \
--env CLOCK_TYPE=$CLOCK_TYPE \
--env LOG_LEVEL=$LOG_LEVEL \
--detach \
--name tidalpi tidalpi:1.0