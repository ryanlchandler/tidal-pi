#!/bin/bash

STRIP_TYPE="${STRIP_TYPE:-LoggerStrip}"

docker build --tag tidalpi:1.0 .
docker rm --force tidalpi
docker run -v /var/log/pi:/app/log -v /var/data:/app/data --privileged --env STRIP_TYPE=$STRIP_TYPE --detach --name tidalpi tidalpi:1.0