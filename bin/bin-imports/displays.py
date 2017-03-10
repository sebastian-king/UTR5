#!/usr/bin/env python

import RPi.GPIO as GPIO
import os, sys, time

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/bin-imports/")
import map_data as md

pinmap = range(1, 32)
rowpins = [17, 18, 19, 20, 29, 30, 31, 32]

for pin in pinmap:
	GPIO.setup(pin, GPIO.OUT)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#setup output pins
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

#define 7 segment digits
d = [ None for y in range( 11 ) ]
d[10]=[1,1,1,1,1,1,1]
d[0]=[0,0,0,0,0,0,1]
d[1]=[1,0,0,1,1,1,1]
d[2]=[0,0,1,0,0,1,0]
d[3]=[0,0,0,0,1,1,0]
d[4]=[1,0,0,1,1,0,0]
d[5]=[0,1,0,0,1,0,0]
d[6]=[0,1,0,0,0,0,0]
d[7]=[0,0,0,1,1,1,1]
d[8]=[0,0,0,0,0,0,0]
d[9]=[0,0,0,1,1,0,0]
gpin=[11,12,13,15,16,18,22]

#routine to clear and then write to display
def showNumber(number):
	digit = d[number]
	for x in range (0,7):
		GPIO.output(gpin[x], d[10][x])
			for x in range (0,7):
				GPIO.output(gpin[x], digit[x])

# needs matrix display function
def drawField():
	while True: # need to quit this at some point, maybe on button press or after time
		for y in range(0, md.gridsize):
			for pin in pinmap:
				GPIO.output(pin, GPIO.LOW) # turn off everything
			GPIO.output(pinmap[rowpins[y]], GPIO.HIGH)
			for x in range(0, md.gridsize):
				r = pinmap[x+8]
				g = pinmap[29-x]
				b = pinmap[x]
				if (x == 0 and y == 6):
					GPIO.output(r, GPIO.HIGH)
					GPIO.output(g, GPIO.HIGH)
				elif md.has_live_wire_for_loc(x, y):
					GPIO.output(b, GPIO.HIGH)
				elif md.has_tunnel_for_loc(x, y):
					GPIO.output(r, GPIO.HIGH)
			time.sleep(0.001) # need to mess around to find good time
