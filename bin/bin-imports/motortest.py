#!/usr/bin/env python

#WHAT WE NEED TO DO: MOVEMENT TESTING
#this is a simple test for the encoder and motor, the right front
#import motortest in python on the pi
#call initMotor()
#call clockwise(1, 1), counter_clockwise(1, 1), and stop(1)
#if all of the above works:
#call runMotor(num_pulses), make sure it rotates and stops 
#make sure encoders are working
#once that works, we need to figurue out pwm stuff for speed
#once this whole test works, we can update/test motors.py in the same way, which is this but with all 4 motors
#when motors.py works, we can test movement_wrapper.strafe_one_block(direction), this is what handles 600 pulses/rot, wheel size constants, etc



#need to test/debug encodertest on the pi


#encoder.py has encoder class that takes 2 pins for quadrature encoders
import sys
from encoder import encoder
#from encoder import encoder
import pins

import RPi.GPIO as io
#import wiringpi
#wiringpi.wiringPiSetupGpio()


#motor numbers: LF=0 RF=1 LB=2 RB=3
encoder1 = encoder(pins.motorEncoderA[1], pins.motorEncoderB[1])



#CALL THIS BEFORE RUNMOTOR
#sets up GPIO, encoders, interrupts
def initMotor():
    io.setmode(io.BCM)
    
    #TODO make sure pwm is set up right
    #wiringpi.pinMode(pins.rightFrontMotorPWM, 2)
    
    #TODO make sure gpio is set up right
    io.setup(pins.rightFrontMotorEnableA, io.OUT)
    io.setup(pins.rightFrontMotorEnableB, io.OUT)
    io.setup(pins.rightFrontMotorPWM, io.OUT)
    
    stop(1)
    print 'initMotor() completed'


#TODO test this make sure it works
#running clockwise function on motor 1 (right front) to test
#motor numbers: LF=0 RF=1 LB=2 RB=3
def runMotor(pulses, dir):    
    speed = 1000
    
    #set pulses to 0
    encoder1.reset()
    
    rotate(1, speed, dir)

    print 'runMotor() motor started'
    
    moving = True
            
    while moving == True:
        print 'encoder pulses: %s' % (encoder1.getPulses())
        if abs(encoder1.getPulses()) >= pulses:
            moving = False

    stop(1)
    print 'runMotor() completed'

    
#motor numbers: LF=0 RF=1 LB=2 RB=3
def rotate(motor_number, speed, dir):
    if dir == 1:
        clockwise(motor_number, speed)
    else:
        counter_clockwise(motor_number, speed)

def clockwise(motor_number, speed):
    setSpeed(motor_number, speed)
    io.output(pins.motorEnableA[motor_number], True)
    io.output(pins.motorEnableB[motor_number], False)

def counter_clockwise(motor_number, speed):
    setSpeed(motor_number, speed)
    io.output(pins.motorEnableA[motor_number], False)
    io.output(pins.motorEnableB[motor_number], True)

def stop(motor_number):
    setSpeed(motor_number, 0)
    io.output(pins.motorEnableA[motor_number], False)
    io.output(pins.motorEnableB[motor_number], False)

#TODO make sure this is right
def setSpeed(motor_number, speed):
    if 0 < speed <= 1024:
        io.output(pins.motorPwm[motor_number], True)
        #wiringpi.pwmWrite(pins.motorPwm[motor_number], speed)
    else:
        io.output(pins.motorPwm[motor_number], False)
        #wiringpi.pwmWrite(pins.motorPwm[motor_number], 0)
