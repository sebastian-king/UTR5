#!/usr/bin/env python

# This is a very basic test to make the DC motors plugged into the L293D chip move forwards and backwards at variable speeds
# the pi currently cannot interface with the encoders due to a lack of GPIO ports (extender needed, or we can use reserved pins)

import sys
import time
import RPi.GPIO as io

io.setmode(io.BCM)

motors = [0 for a in range(8)]
motorPWM = [0 for a in range(4)]
encodersA = [0 for a in range(4)]
encodersB = [0 for a in range(4)]

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

encodersA[0] = 16
encodersB[0] = 21

def motor(number):
	return 2*number-2;

for mtr in motors:
	io.setup(mtr, io.OUT)

for mtrPWM in motorPWM:
        io.setup(mtrPWM, io.OUT)

i=0;
for mtrPWM in motorPWM:
	motorPWM[i] = io.PWM(mtrPWM, 1024)
	motorPWM[i].start(0)
	i+=1

for encoder in encodersA:
        io.setup(encoder, io.IN)

for encoder in encodersB:
        io.setup(encoder, io.IN)

def encoderA(motor_number):
        return io.input(encodersA[motor_number])

def encoderB(motor_number):
        return io.input(encodersB[motor_number])

def set_speed(motor_number, speed):
	motorPWM[motor_number].ChangeDutyCycle(speed);

def clockwise(motor_number, speed):
	set_speed(motor_number, speed)
	io.output(motors[motor_number], io.LOW)
	io.output(motors[motor_number+1], io.HIGH)

def counter_clockwise(motor_number, speed):
	print "CCW"
	set_speed(motor_number, speed)
	io.output(motors[motor_number], io.HIGH)
	io.output(motors[motor_number+1], io.LOW)

def stop(motor_number):
	set_speed(motor_number, 0)
        io.output(motors[motor_number], io.LOW)
        io.output(motors[motor_number+1], io.LOW)

def motor_run(motor_number, direction, speed, degree):
        desire_angle = degree
        gear_ratio = 200
        smalldegree = desire_angle * gear_ratio
        limit = smalldegree / 30

        countAB=0;
	print limit;
        while countAB < limit:
		print countAB;
                initA = encoderA(motor_number)
                initB = encoderB(motor_number)
                while True:
			print "COUNT:" + str(countAB) + "|A:" + str(encoderA(motor_number)) + "|B:" + str(encoderB(motor_number))
                        if direction == 1:
                                clockwise(motor_number, speed)
                        else:
                                counter_clockwise(motor_number, speed)
                        if initA != encoderA(motor_number) or initB != encoderB(motor_number):
                                break
		countAB += 1
	stop(motor_number)

#motor_run(motor(1), 0, 45, 360)

#clockwise(0, 45) # etc...

#time.sleep(2)

#set_speed(0, 45)
motorPWM[0].ChangeDutyCycle(45);
#motorPWM[1].ChangeDutyCycle(45);
io.output(motors[0], io.HIGH)
io.output(motors[1], io.LOW)

#time.sleep(2)

#counter_clockwise(motor(1), 45)

time.sleep(500)

#stop(motor(1));

#time.sleep(1)

io.cleanup()
