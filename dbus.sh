#!/bin/bash

Online=$(dbus-send --print-reply --system \
	--dest=org.freedesktop.UPower \
	/org/freedesktop/UPower/devices/line_power_AC \
	org.freedesktop.DBus.Properties.Get \
	string:org.freedesktop.UPower.Device \
	string:Online)

if echo $Online | grep "true" &> /dev/null; then
	echo "This machine is currently plugged in"
else
	echo "This machine is currently using the battery"
fi

exit 0
