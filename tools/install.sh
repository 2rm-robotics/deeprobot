#!/bin/sh
[ "`id -u`" -ne "0" ] && echo "This command must be run as root" && exit 127

install -o root runrobot.sh /usr/local/bin/runrobot.sh
install -o root -m 755 runrobot.service /lib/systemd/system/runrobot.service
systemctl enable runrobot.service
