#!/bin/bash

ETH_DEV="enp3s0" 
WIFI_DEV="wlo1"

C_YELLOW="%{F#F0C674}"
C_WHITE="%{F#cccccc}"
C_GRAY="%{F#707880}"


#if nmcli -t -f active,ssid dev wifi | grep -q yes; then
if [ -n "$(ifconfig $WIFI_DEV | grep inet)" ]; then
    name=$(nmcli -t -f active,ssid dev wifi | grep yes | cut -d: -f2)
    ip=$(ifconfig $WIFI_DEV | awk '/inet /{print $2}' | cut -d':' -f2)
    echo "$C_YELLOW $C_WHITE$name $C_GRAY$ip"
# Check if connected to Ethernet
#else nmcli -t -f active,device dev eth | grep -q yes; then
elif [ -n "$(ifconfig $ETH_DEV | grep inet)" ]; then
    ip=$(ifconfig $ETH_DEV | awk '/inet /{print $2}' | cut -d':' -f2)
    echo "$C_YELLOW $C_GRAY$ip"
else
# No active connection
    echo "$C_YELLOW $C_GRAY"
fi
