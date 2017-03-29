#!/usr/bin/env python

import RPi.GPIO as GPIO
import os, sys, time
from Adafruit_MCP230xx import *

myfolder = os.path.dirname(os.path.realpath(__file__))

sys.path.append(myfolder + "/bin-imports/")
import pins
import map_data as md

mcpBLUE = Adafruit_MCP230XX(busnum = 0, address = 0x20, num_gpios = 16)

for i in range(8):
	(pins.mcp22).config(display8x8red[i], pins.OUTPUT)
	(pins.mcp21).config(display8x8green[i], pins.OUTPUT)
	(pins.mcp22).config(display8x8blue[i], pins.OUTPUT)

#TODO fix row enable pins/ setup
rowpins = [17, 18, 19, 20, 29, 30, 31, 32]	# these are the pins to turn on rows
for pin in pins.matrixrow:
	GPIO.setup(pin, GPIO.OUT)

#TODO fix setup
for pin in pins.segment:
	GPIO.setup(pin, GPIO.OUT)

#define 7 segment digits
d = [ None for y in range( 11 ) ]
d[10] = [1,1,1,1,1,1,1]
d[0] = [0,0,0,0,0,0,1]
d[1] = [1,0,0,1,1,1,1]
d[2] = [0,0,1,0,0,1,0]
d[3] = [0,0,0,0,1,1,0]
d[4] = [1,0,0,1,1,0,0]
d[5] = [0,1,0,0,1,0,0]
d[6] = [0,1,0,0,0,0,0]
d[7] = [0,0,0,1,1,1,1]
d[8] = [0,0,0,0,0,0,0]
d[9] = [0,0,0,1,1,0,0]

#TODO check pin setup
# we should always have the bottom left lit yellow
(pins.mcp22).output(pins.display8x8red[0], pins.HIGH) #GPIO.output(pins.matrix[8], GPIO.HIGH)
(pins.mcp21).output(pins.display8x8green[0], pins.HIGH) #GPIO.output(pins.matrix[29], GPIO.HIGH)
mcp.output(rowpins[7], pins.HIGH) #GPIO.output(pins.matrix[rowpins[6]], GPIO.HIGH)

def show():
	with open(+"/finaldata") as f:
		lines = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	lines = [x.strip() for x in content]
	os.remove(myfolder + "/finaldata")


	digit = d[int(lines.pop(0))]
	for x in range(0, 7):
		GPIO.output(pins.segment[x], digit[x])
	
	while True: # need to quit this at some point, maybe on button press or after time TODO
		for y in range(0, len(lines)):
			for i in range(8):
				(pins.mcp22).output(display8x8red[i], pins.LOW)
				(pins.mcp21).output(display8x8green[i], pins.LOW)
				(pins.mcp22).output(display8x8blue[i], pins.LOW)
			GPIO.output(pins.matrix[rowpins[y]], GPIO.HIGH)		#TODO rowpins
			for x in range(0, md.gridsize):
				r = pins.display8x8red[x+8]		#find the correct pin that corresponds to the color for the led in that column
				g = pins.display8x8green[x]
				b = pins.display8x8blue[x]
				if (x == 0 and y == 6):
					(pins.mcp22).output(r, pins.HIGH)
					(pins.mcp21).output(g, pins.HIGH)
				elif lines[y][x] == "L":
					(pins.mcp22).output(b, pins.HIGH)
				elif lines[y][x] == "T":
					(pins.mcp22).output(r, pins.HIGH)
			time.sleep(0.001) # need to mess around to find good time TODO
