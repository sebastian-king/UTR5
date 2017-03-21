#!/usr/bin/env python

# This is a very basic test to make the DC motors plugged into the L293D chip move forwards and backwards at variable speeds
# the pi currently cannot interface with the encoders due to a lack of GPIO ports (extender needed, or we can use reserved pins)

import sys
import time
import RPi.GPIO as io
import wiringpi #apt-get install wiringpi

#io.cleanup()

io.setmode(io.BCM)
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18,2)
wiringpi.pwmWrite(18, 0)

motors = [0 for a in range(8)]

motors[0] = 15 # motor 1
motors[1] = 16
motors[2] = 13 # motor 2
motors[3] = 19
motors[4] = 26 # motor 3
motors[5] = 21
motors[6] = 20 # motor 4
motors[7] = 16

def motor(number):
	return 2*number-2;

for motor in motors:
	io.setup(motor, io.OUT)

#io.cleanup();

def speed(speed):
	if 0 <= speed <= 1024:
		wiringpi.pwmWrite(18, speed)
	else:
		wiringpi.pwmWrite(18, 0)

def clockwise(motor_number, speed):
	speed(speed)
	io.output(motors[motor_number], True)
	io.output(motors[motor_number+1], False)

def counter_clockwise(motor_number, speed):
	speed(speed)
	io.output(motors[motor_number], False)
	io.output(motors[motor_number+1], True)

start = time.clock()

while (time.clock()-start < 3000):
	clockwise(motor(1), 512) # etc...
	clockwise(motor(2), 512)
	clockwise(motor(3), 512)
	clockwise(motor(4), 512)

io.cleanup()
