#!/usr/bin/env python

current_direction = 90      #startng direction. 0 to 360 0=+x, 90=+y,, etc


#location [x,y] 0-7. [0,0] is bottom left (we can change this)
loc = [1, 0]         #starting x, y

blocklength = 10     #constant that we need to measure

def is_valid_loc(x, y):
	return (0 <= x <= 7) and (0 <= y <= 7)

def getX():
	return loc[0]

def getY():
	return loc[1]

def setX(newX):
	loc[0] = newX

def setY(newY):
	loc[0] = newY

def getDir():
	return current_direction;

def setDir(dir):
	current_direction = dir;