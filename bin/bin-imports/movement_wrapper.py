#!/usr/bin/env python

#holonomic drive wrapper

import motors
import map_data

#we don't want to have to include motors.py in main
def initMotors(void):
	motors.initMotors()

#direction: 0=right, 1=fwd, 2=left, 3=back	relative to current direction
def move(distance, direction):
	if distance > 0:
		#constant for ratio of the distance per rotation, in <unit of measurement>, that a wheel travels when wheel is straight
		wheel_circumference = 60    #60mm
		#number of rotations needed to travel distance when wheels are at a 45 degree angle
		num_rotations_diagonal = (distance * 1.414214) / wheel_circumference       # 1.414214=sqrt(2)
		#angle = num_rotations_diagonal * 360
		num_pulses = num_rotations_diagonal*600  #multiply by 600, the number of phase counts per revolution of the motor
	
		if direction == map_data.RIGHT:    #right
			FL = 0
			FR = 0
			BL = 1
			BL = 1
		if direction == map_data.UP:    #fwd
			FL = 0
			FR = 1
			BL = 0
			BL = 1
		if direction == map_data.LEFT:    #left
			FL = 1
			FR = 1
			BL = 0
			BL = 0
		if direction == map_data.DOWN:    #back
			FL = 1
			FR = 0
			BL = 1
			BL = 0
	
		speed = 512     #not sure what speed to use (maybe max)
		#need to figure out wheel numbers
		motors.run_all_motors(speed, num_pulses, FL, FR, BL, BR)


def turn(degrees):
	if degrees != 0:
		map_data.setDir(map_data.getDir() + degrees)
		if degrees > 0:
			dir = map_data.RIGHT
			angle = degrees
		elif degrees < 0:
			dir = map_data.UP
			angle = degrees * -1
		speed = 512     #not sure what speed to use
		#need to figure out wheel numbers
		motors.run_all_motors(speed, angle, dir, dir, dir, dir)
	



blocklength = 305     #1 foot = 305mm

#strafe one block no turning. direction: 0=right, 1=fwd, 2=left, 3=back
def strafe_one_block(direction):
	x = map_data.getX()
	y = map_data.getY()
	if direction == map_data.RIGHT:
		x = x + 1
	elif direction == map_data.UP:
		y = y + 1
	elif direction == map_data.LEFT:
		x = x - 1
	elif direction == map_data.DOWN:
		y = y - 1

	if map_data.is_valid_loc(x, y):
		map_data.setX(x)
		map_data.setX(y)
		move(blocklength, direction)
	#else: error in movement algorithm


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

		#y movement
		distance = 0;
		if y_diff > 0:
			dir = map_data.UP
			distance = blocklength * y_diff
		elif y_diff < 0:
			dir = map_data.DOWN
			distance = blocklength * y_diff * -1
		move(distance, dir)
		map_data.setY(y)

def removeCacheLid():
	# lower and raise arm
