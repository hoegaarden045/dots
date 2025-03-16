#!/bin/sh

if hyprctl activeworkspace | grep -q "eDP-1"; then
grim -o eDP-1 - | wl-copy && wl-paste > ~/Pictures/Screenshots/Screenshot-$(date +%F_%T).png | notify-send "Screenshot of whole screen taken" -t 1000
fi

if hyprctl activeworkspace | grep -q "HDMI-A-1"; then
grim -c -o HDMI-A-1 - | wl-copy && wl-paste > ~/Pictures/Screenshots/Screenshot-$(date +%F_%T).png | notify-send "Screenshot of whole screen taken" -t 1000

fi
