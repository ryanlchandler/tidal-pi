#!/bin/bash
docker build --tag tidalpi:1.0 .
docker rm --force tidalpi
docker run  --privileged --detach --name tidalpi tidalpi:1.0