#!/bin/bash

# sudo vi /lib/systemd/system/tidal-pi.service
until ping -c1 github.com &>/dev/null; do :; done
rm -rf /home/pi/git/tidal-pi
git clone https://github.com/ryanlchandler/tidal-pi.git /home/pi/git/tidal-pi
git -C /home/pi/git/tidal-pi submodule init 
git -C /home/pi/git/tidal-pi submodule update
cp /home/pi/git/tidal-pi/scripts/wifi-config.sh /home/pi/scripts/wifi-config.sh
cp /home/pi/git/tidal-pi/scripts/tidal-pi.sh /home/pi/scripts/tidal-pi.sh
cd /home/pi/git/tidal-pi
./run.sh