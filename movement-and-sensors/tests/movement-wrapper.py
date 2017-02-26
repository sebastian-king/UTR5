#!/usr/bin/env python

#holonomic drive wrapper

import motors-with-encoders

#direction: 0=right, 1=fwd, 2=left, 3=back
def move(distance, direction):
	#constant for ratio of the distance per rotation, in <unit of measurement>, that a wheel travels when wheel is straight
	distRotRatio = 5    #this is a guess, need to measure
	#constant for ratio of the distance per rotation, in <unit of measurement>, that a wheel travels when wheel is at a 45 degree angle. 
	distRotRatioDiag = distRotRatio / 1.414214   #sqrt(2) = 1.414214
	numRotations = distance / distRotRatioDiag
	angle = rumRotations * 360
	
	if direction == 0:    #right
		FL = 0
		FR = 0
		BL = 1
		BL = 1
	if direction == 1:    #fwd
		FL = 0
		FR = 1
		BL = 0
		BL = 1
	if direction == 2:    #left
		FL = 1
		FR = 1
		BL = 0
		BL = 0
	if direction == 3:    #back
		FL = 1
		FR = 0
		BL = 1
		BL = 0
	
	speed = 512     #not sure what speed to use
	#need to figure out wheel numbers
	motors-with-encoders.motor_run_with_overshoot(front_left, FL, speed, angle)
	motors-with-encoders.motor_run_with_overshoot(front_right, FR, speed, angle)
	motors-with-encoders.motor_run_with_overshoot(b_left, BL, speed, angle)
	motors-with-encoders.motor_run_with_overshoot(b_right, BR, speed, angle)



#an idea for movement control based on coordinates

#location [x,y] 0-7. [0,0] is bottom left (we can change this)
loc = [1, 0]         #starting x, y
blocklength = 10     #constant that we need to measure

def isValidLoc(x, y):
	return (0 <= x <= 7) and (0 <= y <= 7)

#direction: 0=right, 1=fwd, 2=left, 3=back
def move_one_block(direction):
	x = loc[0]
	y = loc[1]
	if direction == 0:
		x = x + 1
	elif direction == 1:
		y = y + 1
	elif direction == 2:
		x = x - 1
	elif direction == 3:
		y = y - 1

	if isValidLoc(x, y):
		loc[0] = x
		loc[1] = y
		move(blocklength, direction)
	#else: error in movement algorithm




