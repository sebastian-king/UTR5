#!/usr/bin/env python

#myfolder = os.path.dirname(os.path.realpath(__file__))
#sys.path.append(myfolder + "/bin-imports/")

import os, sys, time
import pins
import map_data as md
from Adafruit_MCP230xx import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#map_data color info
RED = 0
GREEN = 1
BLUE = 2

#mcpBLUE = Adafruit_MCP230XX(busnum = 0, address = 0x20, num_gpios = 16)
#Expander 0x20 is the motor controller?

for i in range(8):
	(pins.mcp22).config(pins.display8x8RedCol[i], pins.OUTPUT)
	(pins.mcp21).config(pins.display8x8GreenCol[i], pins.OUTPUT)
	(pins.mcp22).config(pins.display8x8BlueCol[i], pins.OUTPUT)
	(pins.mcp21).config(pins.display8x8Row[i], pins.OUTPUT)

for x in range(0, 7):
	(pins.mcp23).config(pins.segments[x], pins.OUTPUT)

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
(pins.mcp22).output(pins.display8x8RedCol[0], pins.HIGH) #GPIO.output(pins.matrix[8], GPIO.HIGH)
(pins.mcp21).output(pins.display8x8GreenCol[0], pins.HIGH) #GPIO.output(pins.matrix[29], GPIO.HIGH)
(pins.mcp21).output(pins.display8x8Row[7], pins.LOW) #GPIO.output(pins.matrix[rowpins[6]], GPIO.HIGH)

def show():
	with open(+"/finaldata") as f:
		lines = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	lines = [x.strip() for x in content]
	os.remove(myfolder + "/finaldata")
	showNumber(lines.pop(0))
	#TODO make sure high and low is correct
	while True: # need to quit this at some point, maybe on button press or after time TODO
		for y in range(0, len(lines)):
			for i in range(8):
				(pins.mcp22).output(pins.display8x8RedCol[i], pins.LOW)
				(pins.mcp21).output(pins.display8x8GreenCol[i], pins.LOW)
				(pins.mcp22).output(pins.display8x8BlueCol[i], pins.LOW)
			(pins.mcp21).output(pins.display8x8Row[y], pins.HIGH)
			for x in range(0, md.gridsize):
				r = pins.display8x8RedCol[x]		#find the correct pin that corresponds to the color for the led in that column
				g = pins.display8x8GreenCol[x]
				b = pins.display8x8BlueCol[x]
				if (x == 0 and y == 6):
					(pins.mcp22).output(r, pins.HIGH)
					(pins.mcp21).output(g, pins.HIGH)
				elif lines[y][x] == "L":
					(pins.mcp22).output(b, pins.HIGH)
				elif lines[y][x] == "T":
					(pins.mcp22).output(r, pins.HIGH)
			time.sleep(0.001) # need to mess around to find good time TODO

def lightSingle(x, y, color):
	for i in range(8):
		(pins.mcp22).output(pins.display8x8RedCol[i], pins.LOW)
		(pins.mcp21).output(pins.display8x8GreenCol[i], pins.LOW)
		(pins.mcp22).output(pins.display8x8BlueCol[i], pins.LOW)
	(pins.mcp21).output(pins.display8x8Row[y], pins.HIGH)
	if color is "r":
		(pins.mcp22).output(pins.display8x8RedCol[x], pins.HIGH)
	elif color is "g":
		(pins.mcp21).output(pins.display8x8GreenCol[x], pins.HIGH)
	elif color is "b":
		(pins.mcp22).output(pins.display8x8BlueCol[x], pins.HIGH)

def showNumber(n):
	digit = d[int(n)]
	for x in range(0, 7):
		(pins.mcp23).output(pins.segments[x], digit[x])


def mapDisplay():
	while True:
		for row in range(8): #range(n) isn't inclusive so go from row 0 to row 7
			(pins.mcp21).output(pins.display8x8Row[row], pins.HIGH)
			for col in range(8):
				color = 2 #This should come from map_data.py, right now I just set it to Blue (2) for testing
				if color == 0: #It's red
					(pins.mcp22).output(pins.display8x8RedCol[col], pins.LOW)
				elif color == 1: #It's green
					(pins.mcp21).output(pins.display8x8GreenCol[col], pins.LOW)
				elif color == 2: #It's blue
					(pins.mcp22).output(pins.display8x8BlueCol[col], pins.LOW)
			time.sleep(0.01) #Do we even need this? Should it be less time?
			(pins.mcp21).output(pins.display8x8Row[row], pins.LOW)
			#We REALLY need to check this section to make sure we're not burning out the LEDs
			for i in range(8):
					(pins.mcp22).output(display8x8RedCol[i], pins.HIGH)
					(pins.mcp21).output(display8x8GreenCol[i], pins.HIGH)
					(pins.mcp22).output(display8x8BlueCol[i], pins.HIGH)
