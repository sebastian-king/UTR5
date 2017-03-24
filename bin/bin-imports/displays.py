#!/usr/bin/env python

import RPi.GPIO as GPIO
import os, sys, time

myfolder = os.path.dirname(os.path.realpath(__file__))

sys.path.append(myfolder + "/bin-imports/")
import pins
import map_data as md

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

for pin in pins.matrix:
	GPIO.setup(pin, GPIO.OUT)

for pin in pins.matrixrow:
	GPIO.setup(pin, GPIO.OUT)

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

rowpins = [17, 18, 19, 20, 29, 30, 31, 32]	# these are the pins to turn on rows

# we should always have the bottom left lit yellow
GPIO.output(pins.matrix[8], GPIO.HIGH)
GPIO.output(pins.matrix[29], GPIO.HIGH)
GPIO.output(pins.matrix[rowpins[6]], GPIO.HIGH)

def show():
	with open(+"/finaldata") as f:
		lines = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	lines = [x.strip() for x in content]
	os.remove(myfolder + "/finaldata")

	#mcp = Adafruit_MCP230XX(busnum = 1, address = 0x20, num_gpios = 16)
	#mcp.config(0, OUTPUT)
	#mcp.config(1, OUTPUT)
	#mcp.config(2, OUTPUT)
	#mcp.output(0, 1)  # High
	#mcp.output(0, 0)  # Low

	digit = d[int(lines.pop(0))]
	for x in range(0, 7):
		GPIO.output(pins.segment[x], digit[x])
	
	while True: # need to quit this at some point, maybe on button press or after time
		for y in range(0, len(lines)):
			for pin in pins.matrix:
				GPIO.output(pin, GPIO.LOW) # turn off everything
			GPIO.output(pins.matrix[rowpins[y]], GPIO.HIGH)
			for x in range(0, md.gridsize):
				r = pins.matrix[x+8]		#find the correct pin that corresponds to the color for the led in that column
				g = pins.matrix[29-x]
				b = pins.matrix[x]
				if (x == 0 and y == 6):
					GPIO.output(r, GPIO.HIGH)
					GPIO.output(g, GPIO.HIGH)
				elif lines[y][x] == "L":
					GPIO.output(b, GPIO.HIGH)
				elif lines[y][x] == "T":
					GPIO.output(r, GPIO.HIGH)
			time.sleep(0.001) # need to mess around to find good time
