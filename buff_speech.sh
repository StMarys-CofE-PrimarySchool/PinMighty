#!/bin/bash

/bin/rm /home/pi/robot/out.wav 2>/dev/null
/usr/bin/espeak "$*" -w /home/pi/robot/out.wav
/usr/bin/aplay /home/pi/robot/out.wav
/bin/rm /home/pi/robot/out.wav 2>/dev/null
