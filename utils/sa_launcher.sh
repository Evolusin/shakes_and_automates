#!/bin/bash
export SAPATH='/home/django/Desktop/programing/shakes_and_automates/'
export DISPLAY=:1002
export SHAKES='LINUX'

cd $SAPATH
touch magic
source venv/bin/activate
google-chrome https://s39.sfgame.pl &
python3 run.py

