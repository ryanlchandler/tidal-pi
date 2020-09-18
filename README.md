# SSH

You can ssh in as the user rchandler with a common password that you use when you don't care much about security.


# Boot

SystemD is used to run a script to start wifi and start the tidal-pi app.

#### /lib/systemd/system/wifi-config.service

```
[Unit]
Description=Configure WIFI Servicew
After=multi-user.target

[Service]
Type=idle
ExecStart=/home/pi/scripts/wifi-config.sh

[Install]
WantedBy=multi-user.target
```


#### /lib/systemd/system/tidal-pi.service

```
[Unit]
Description=My Script Service
After=pdns-recursor.service

[Service]
Type=idle
User=pi
ExecStart=/home/pi/scripts/tidal-pi.sh

[Install]
WantedBy=pdns-recursor.service
```