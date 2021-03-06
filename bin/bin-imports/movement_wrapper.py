#!/usr/bin/env python

#holonomic drive wrapper

#TESTING PLAN
#call initMotors() first
#test move()
#test strafe_one_block()
#test strafe_to_block()

import motors
import map_data
import time

#this is just so we don't have to include motors.py in main
def initMotors():
	motors.initMotors()

#move the entire bot a certain distance in mm in a direction relative to the bot
#direction: 0=right, 1=fwd, 2=left, 3=back	relative to current direction
def move(distance, direction):
	if distance > 0:
		#constant for ratio of the distance per rotation, in <unit of measurement>, that a wheel travels when wheel is straight
		wheel_diameter = 60.0    #60mm
		#number of rotations needed to travel distance when wheels are at a 45 degree angle
		num_rotations_diagonal = distance / (1.414214 * wheel_diameter * 3.1415)     # 1.414214=sqrt(2)
		#angle = num_rotations_diagonal * 360
		num_pulses = num_rotations_diagonal*90.0  #multiply by 90, the number of phase counts per revolution of the motor
	
		#figure out which wheels are clockwise(1) vs counter_clockwise(0)
		if direction == map_data.RIGHT:    #right
			FL = 0
			FR = 0
			BL = 1
			BR = 1
		elif direction == map_data.UP:    #fwd
			FL = 0
			FR = 1
			BL = 0
			BR = 1
		elif direction == map_data.LEFT:    #left
			FL = 1
			FR = 1
			BL = 0
			BR = 0
		elif direction == map_data.DOWN:    #back
			FL = 1
			FR = 0
			BL = 1
			BR = 0
	
		speed = 100	#rpm
		motors.runMotors(num_pulses, speed, FL, FR, BL, BR)


#330.2 mm circumference of bot
def turn(degrees):
	if degrees != 0:
		map_data.setDir(map_data.getDir() + degrees)
		angle = 0
		d = 0
		if degrees > 0:
			d = 0
			angle = degrees
		elif degrees < 0:
			d = 1
			angle = degrees * -1
		
		dist = 330.2 * 3.1415 * (angle / 360.0)
		num_pulses_turn = (dist * 90.0)/(60.0 * 3.1415)
		print "pulses: %s, dist: %s, direction: %s, angle: %s" % (num_pulses_turn, dist, d, angle)
		speed = 800     #not sure what speed to use	
		motors.runMotors(num_pulses_turn, speed, d, d, d, d)
	



blocklength = 304.8     #1 foot = 305mm

#strafe one block no turning. direction: 0=right, 1=fwd, 2=left, 3=back
def strafe_one_block(direction):
	x = map_data.getX()
	y = map_data.getY()
	if direction == map_data.RIGHT:
		x = x + 1
	elif direction == map_data.UP:
		y = y - 1
	elif direction == map_data.LEFT:
		x = x - 1
	elif direction == map_data.DOWN:
		y = y + 1

	if map_data.is_valid_loc(x, y):
		map_data.setX(x)
		map_data.setY(y)
		move(blocklength, direction)
		print "moved to (%s, %s)" % (map_data.loc[0], map_data.loc[1])
	else: 
		#error in movement algorithm
		print "invalid location (%s, %s)" % (x, y)

def strafe_to_block(x, y):
	if map_data.is_valid_loc(x, y):
		x_diff = x - map_data.getX()
		y_diff = y - map_data.getY()
		
		#x movement
		distance = 0;
		dir = map_data.RIGHT
		if x_diff > 0:
			distance = blocklength * x_diff
			dir = map_data.RIGHT
		elif x_diff < 0:
			distance = blocklength * x_diff * -1
			dir = map_data.LEFT
		move(distance, dir)
		map_data.setX(x)

		time.sleep(.4)

		#y movement
		distance = 0;
		if y_diff < 0:
			dir = map_data.UP
			distance = blocklength * y_diff * -1
		elif y_diff > 0:
			dir = map_data.DOWN
			distance = blocklength * y_diff
		move(distance, dir)
		map_data.setY(y)


#we probably don't need this
#move to a block with turning, no diagonals
def move_to_block(x, y):
	if map_data.is_valid_loc(x, y):
		x_diff = x - map_data.getX()
		y_diff = y - map_data.getY()
		
		#x movement
		turn_angle = 0
		distance = 0;
		if x_diff > 0:
			turn_angle = -1 * current_direction
			distance = blocklength * x_diff
		elif x_diff < 0:
			turn_angle = -1 * (current_direction - 180)
			distance = blocklength * x_diff * -1
		if (turn_angle == 270) or (turn_angle == -270):
			turn_angle = turn_angle * (-1/3)
		turn(turn_angle)
		move(distance, 1)
		map_data.setX(x)

		#y movement
		turn_angle = 0
		distance = 0;
		if y_diff > 0:
			turn_angle = -1 * (current_direction - 90)
			distance = blocklength * y_diff
		elif y_diff < 0:
			turn_angle = -1 * (current_direction - 270)
			distance = blocklength * y_diff * -1
		if (turn_angle == 270) or (turn_angle == -270):
			turn_angle = turn_angle * (-1/3)
		turn(turn_angle)
		move(distance, 1)
		map_data.setY(y)


#im not sure if this should go in movement_wrapper, the arm should maybe have its own file
def removeCacheLid():
	abc = 0
	# lower and raise arm
