#!/usr/bin/env python

# This is a very basic test to make the DC motors plugged into the L293D chip move forwards and backwards at variable speeds
# the pi currently cannot interface with the encoders due to a lack of GPIO ports (extender needed, or we can use reserved pins)

import sys
import time
import RPi.GPIO as io

io.setmode(io.BCM)

pin = 16

io.setup(pin, io.IN)

for a in range(10):
	print io.input(pin)
	time.sleep(0.2)
