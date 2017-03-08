#!/usr/bin/env python

# This is a very basic test to make the DC motors plugged into the L293D chip move forwards and backwards at variable speeds
# need to figure out if encoders are going in reserved pins or an expander

import sys
import time
import RPi.GPIO as io
import wiringpi
io.setmode(io.BCM)
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18,2)
wiringpi.pwmWrite(18, 0)

motors[0] = 5 # motor 1
motors[1] = 6
motors[2] = 13 # motor 2
motors[3] = 19
motors[4] = 26 # motor 3
motors[5] = 21
motors[6] = 20 # motor 4
motors[7] = 16

# mappings for direct access to the PI, but I cannot guarantee these pins won't be needed for other things
encodersA[0] = 7
encodersB[0] = 8
encodersA[1] = 25
encodersB[1] = 24
encodersA[2] = 11
encodersB[2] = 9
encodersA[3] = 10
encodersB[3] = 22

countover[0] = 0
countover[1] = 1
countover[2] = 2
countover[3] = 3

def motor(number):
	return number-2+number

for motor in motors:
	io.setup(motor, io.OUT)
for encoder in encodersA:
	io.setup(encoder, io.IN)
for encoder in encodersB:
	io.setup(encoder, io.IN)

def speed(speed):
	if 0 <= speed <= 1024:
		wiringpi.pwmWrite(18, speed)
	else:
		wiringpi.pwmWrite(18, 0)

#i think this should work for running 4 motors at once but correct this if its wrong
def run_all_motors(speed, degree, dir1, dir2, dir3, dir4):
	desire_angle = degree
	# in this case gear ratio is 1:200
	gear_ratio = 200;
	# convert the desired angle to the total angle at the rear shaft (multiply gear ratio)
	smalldegree = desire_angle * gear_ratio
	# 12 count per revolution at the rear shaft
	# meaning each count represent 30 degree
	# to calculate how many counts needed for the desire angle
	# we divide total angle at the rear shaft with 30 degree
	limit = smalldegree / 30

	countAB=0; #reset the counter
	while countAB < limit: # while counter is in the limit
				# motor will overshoot because it can not sudden stop
		#im not sure what to do with the encoders, is checking only one okay or does it need to be checked for each motor?
		initA = encoderA[0]	# get current A value -- overshoot depends on load and speed of the motor
		initB = encoderB[0]	# get current B value
		while True:
			rotate(1, speed, dir1)
			rotate(2, speed, dir2)
			rotate(3, speed, dir3)
			rotate(4, speed, dir4)
			if initA != encoderA[motor_number-1] or initB != encoderB[motor_number-1]:	# continue run until state change
				break
		countAB += 1				# increment counter for each state change
	stop(1)
	stop(2)
	stop(3)
	stop(4)


def motor_run(motor_number, direction, speed, degree):
	desire_angle = degree
	# in this case gear ratio is 1:200
	gear_ratio = 200;
	# convert the desired angle to the total angle at the rear shaft (multiply gear ratio)
	smalldegree = desire_angle * gear_ratio
	# 12 count per revolution at the rear shaft
	# meaning each count represent 30 degree
	# to calculate how many counts needed for the desire angle
	# we divide total angle at the rear shaft with 30 degree
	limit = smalldegree / 30

	countAB=0; #reset the counter
	while countAB < limit: # while counter is in the limit
				# motor will overshoot because it can not sudden stop
		initA = encoderA[motor_number-1]	# get current A value -- overshoot depends on load and speed of the motor
		initB = encoderB[motor_number-1]	# get current B value
		while True:
			
			if direction == 1:
				clockwise(motor_number, speed)		# run motor in clockwise direction with user defined speed
			else:
				counter_clockwise(motor_number, speed)
			if initA != encoderA[motor_number-1] or initB != encoderB[motor_number-1]:	# continue run until state change
				break
		countAB += 1				# increment counter for each state change
	stop(motor_number)

def motor_run_with_overshoot(motor_number, direction, speed, degree):
        desire_angle = degree;
        # in this case gear ratio is 1:200
        gear_ratio = 200;
        # convert the desired angle to the total angle at the rear shaft (multiply gear ratio)
        smalldegree = desire_angle * gear_ratio;
        # 12 count per revolution at the rear shaft
        # meaning each count represent 30 degree
        # to calculate how many counts needed for the desire angle
        # we divide total angle at the rear shaft with 30 degree
        limit = smalldegree / 30;

        countAB=0; #reset the counter
        while countAB < limit-countover[motor_number-1]+3: # while counter is in the limit
                                # motor will overshoot because it can not sudden stop
                initA = encoderA[motor_number-1]       # get current A value -- overshoot depends on load and speed of the motor
                initB = encoderB[motor_number-1]       # get current B value
                while True:
                        if direction == 1:
                                clockwise(motor_number, speed)          # run motor in clockwise direction with user defined speed
                        else:
                                counter_clockwise(motor_number, speed)
                        if initA != encoderA[motor_number-1] or initB != encoderB[motor_number-1]:    # continue run until state change
                                break
                countAB += 1				# increment counter for each state change
		stopA = encoderA[motor_number-1]	# get current A value -- overshoot depends on load and speed of the motor
		stopB = encoderB[motor_number-1]

	# once program exit the previous while loop
	# meaning that the motor has reached the desired angle
	countover=0 	# reset overshoot counter
	end=0		# reset end function flag
	while end == 0:	# while the flag is not set
		while True:
			if countstop > 10000:
				end = 1	# set end flag if stop counter >10000
			else:
				stop(motor_number)		# brake the motor
				countstop += 1			# stop counter increment by 1
			if stopA != A or stopB != B or end != 0:
				break				# loop if states do not change
		# if states change,meaning overshoot occur
		countover += 1	# increment overshoot counter
		countstop = 0	# clear stop counter
		stopA = A		# stopA store the current A value
		stopB = B		# stopB store the current B value

def encoderA(motor_number):
	return GPIO.input(encodersA[motor_number-1])

def encoderB(motor_number):
	return GPIO.input(encodersB[motor_number-1])

def rotate(motor_number, speed, dir):
	if dir == 1:
		clockwise(motor_number, speed)
	else:
		counter_clockwise(motor_number, speed)

def clockwise(motor_number, speed):
	speed(speed)
	io.output(motors[motor_number], True)
	io.output(motors[motor_number+1], False)

def counter_clockwise(motor_number, speed):
	speed(speed)
	io.output(motors[motor_number], False)
	io.output(motors[motor_number+1], True)

def stop(motor_number):
	speed(254)
        io.output(motors[motor_number], True)
        io.output(motors[motor_number+1], True)

#clockwise(motor(4), 512) # etc...
