#!/usr/bin/env python

import sys
import time
import RPi.GPIO as io
import wiringpi

io.setmode(io.BCM)
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18,2)
#wiringpi.pwmWrite(18, 0)

wiringpi.pwmWrite(18, 512)

time.sleep(2);

wiringpi.pwmWrite(18, 0)
