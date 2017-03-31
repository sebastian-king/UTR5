#!/usr/bin/env python

#myfolder = os.path.dirname(os.path.realpath(__file__))
#sys.path.append(myfolder + "/bin-imports/")

import os, sys, time
import pins
import map_data as md
from Adafruit_MCP230xx import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

for i in range(8):
	(pins.mcp22).config(pins.display8x8RedCol[i], pins.OUTPUT)
	(pins.mcp21).config(pins.display8x8GreenCol[i], pins.OUTPUT)
	(pins.mcp22).config(pins.display8x8BlueCol[i], pins.OUTPUT)
	(pins.mcp21).config(pins.display8x8Row[i], pins.OUTPUT)

(pins.mcp21).output(pins.display8x8Row[7], pins.HIGH)
(pins.mcp21).output(pins.display8x8GreenCol[7], pins.LOW)

for i in range(8):
	(pins.mcp22).output(display8x8RedCol[i], pins.LOW)
	(pins.mcp21).output(display8x8GreenCol[i], pins.LOW)
	(pins.mcp22).output(display8x8BlueCol[i], pins.LOW)
