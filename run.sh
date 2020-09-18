#!/bin/bash

STRIP_TYPE="${STRIP_TYPE:-LoggerStrip}"
echo "STRIP_TYPE=$STRIP_TYPE"

docker rm --force tidalpi
docker run -v /var/log/pi:/app/log -v /var/data:/app/data --privileged --env STRIP_TYPE=$STRIP_TYPE --detach --name tidalpi tidalpi:1.0