#!/bin/bash

export DISPLAY=:0.0

wname=$(xdotool getactivewindow getwindowname|sed -e "s/'/''/g")
echo "INSERT INTO log (window,user) VALUES ('$wname','$(whoami)');"|mysql --defaults-file=~/.gotdone.auth

mkdir -p ~/gotdone/$(date +%Y-%m/%d/)
import -window root ~/gotdone/$(date +%Y-%m/%d/%H.%M.%S.jpg)

