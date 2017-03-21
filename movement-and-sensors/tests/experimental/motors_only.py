#!/usr/bin/env python

# This is a very basic test to make the DC motors plugged into the L293D chip move forwards and backwards at variable speeds
# the pi currently cannot interface with the encoders due to a lack of GPIO ports (extender needed, or we can use reserved pins)

import sys
import time
import RPi.GPIO as io
from time import clock

io.setmode(io.BCM)

motors = [0 for a in range(8)]
motorPWM = [0 for a in range(4)]

motors[0] = 22 # motor 1
motors[1] = 27
motors[2] = 19 # motor 2
motors[3] = 26

#motors[4] = 25 # motor 3
#motors[5] = 21
#motors[6] = 20 # motor 4
#motors[7] = 16

motorPWM[0] = 17
motorPWM[1] = 18
#motorPWM[2] = 0
#motorPWM[3] = 0

def motor(number):
	return 2*number-2;

for mtr in motors:
	io.setup(mtr, io.OUT)

for mtrPWM in motorPWM:
    io.setup(mtrPWM, io.OUT)

i=0
for mtrPWM in motorPWM:
	motorPWM[i] = io.PWM(mtrPWM, 1024)
	motorPWM[i].start(0)
	i+=1

def set_speed(motor_number, speed):
	motorPWM[motor_number/2].ChangeDutyCycle(speed);

def clockwise(motor_number, speed):
	set_speed(motor_number, speed)
	io.output(motors[motor_number], io.LOW)
	io.output(motors[motor_number+1], io.HIGH)

def counter_clockwise(motor_number, speed):
	set_speed(motor_number, speed)
	io.output(motors[motor_number], io.HIGH)
	io.output(motors[motor_number+1], io.LOW)

def stop(motor_number):
	set_speed(motor_number, 0)
	io.output(motors[motor_number], io.LOW)
 	io.output(motors[motor_number+1], io.LOW)

print "CW"
clockwise(motor(1), 45)
counter_clockwise(motor(2), 45)
clockwise(motor(3), 45)
counter_clockwise(motor(4),45)
time.sleep(5)
print "CCW"
counter_clockwise(motor(1), 45)
clockwise(motor(2), 45)
counter_clockwise(motor(3), 45)
clockwise(motor(4), 45)
time.sleep(5)
print "STOP"
stop(motor(1))
stop(motor(2))
stop(motor(3))
stop(motor(4))
time.sleep(1)
print "CLEANUP"
io.cleanup()
print "DONE"
