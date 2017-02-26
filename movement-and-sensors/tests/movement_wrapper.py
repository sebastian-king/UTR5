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




