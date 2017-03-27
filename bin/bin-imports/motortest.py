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
#>>>WE ARE HERE<<<
#when motors.py works, we can test movement_wrapper.strafe_one_block(direction), this is what handles 90 pulses/rot, wheel size constants, etc



#encoder.py has encoder class that takes 2 pins for quadrature encoders
import sys
from encoder import encoder
import pins
import time
from Adafruit_MCP230xx import *
import RPi.GPIO as io
import wiringpi


#motor numbers: LF=0 RF=1 LB=2 RB=3
encoders = [0 for a in range(4)]

for i in range(4):
    encoders[i] = encoder(pins.motorEncoderA[i], pins.motorEncoderB[i])


mcp = Adafruit_MCP230XX(busnum = 0, address = 0x20, num_gpios = 16)

#CALL THIS BEFORE RUNMOTOR
#sets up GPIO, encoders, interrupts
def initMotors():
    wiringpi.wiringPiSetupGpio()
    io.setmode(io.BCM)
    
    for i in range(4):
        mcp.config(pins.motorEnableA[i], pins.OUTPUT)       #set up the h-bridge a and b pins
        mcp.config(pins.motorEnableB[i], pins.OUTPUT)
        #io.setup(pins.motorPWM[i], io.OUT)
        wiringpi.pinMode(pins.motorPWM[i], pins.OUTPUT)     #set up wiringpi software pwms
        error = wiringpi.softPwmCreate(pins.motorPWM[i],0,1000)
        if error != 0:
            print "error with wiringpi PWM setup in motortest for motor %s" % i
        stop(i)                             #make sure the motor is stopped
    
    #SETUP FOR NO EXPANDER
    #io.setup(pins.rightFrontMotorEnableA, io.OUT)
    #io.setup(pins.rightFrontMotorEnableB, io.OUT)
    #io.setup(pins.rightFrontMotorPWM, io.OUT)
    
    print 'initMotors() completed'



#running pulses on motor_number
#positive pulses = clockwise, negative = counterclockwise
#motor numbers: LF=0 RF=1 LB=2 RB=3
def runMotor(motor_number, pulses, speed):    
    #find dir based on sign of pulses
    dir = 0
    if pulses >= 0:
        dir = 1
    
    #set pulses to 0
    encoders[motor_number].reset()
    
    rotate(motor_number, speed, dir)

    print 'runMotor() motor started for %s pulses' % pulses
    
    moving = True
            
    while moving == True:
        print 'encoder pulses: %s' % (encoders[motor_number].getPulses())
        if abs(encoders[motor_number].getPulses()) >= abs(pulses):
            moving = False

    stopAllMotors()
    
    print 'runMotor() completed'

#running same number of pulses on all motors to compare
#positive pulses = clockwise, negative = counterclockwise
def runMotors(pulses, speed):
     #find dir based on sign of pulses
    dir = 0
    if pulses >= 0:
        dir = 1

    resetAllEncoders()
    
    for i in range(4):
        rotate(i, speed, dir)

    print 'runMotors() motors started for %s pulses' % pulses
    
    moving = True         
    while moving == True:
        print 'encoder pulses: %s' % (encoders[1].getPulses())
        if abs(encoders[1].getPulses()) >= abs(pulses):
            moving = False

    stopAllMotors()
    
    print 'runMotor() completed'
    
    
    
    
    
#motor numbers: LF=0 RF=1 LB=2 RB=3
def rotate(motor_number, speed, dir):
    if dir == 1:
        clockwise(motor_number, speed)
    else:
        counter_clockwise(motor_number, speed)

def clockwise(motor_number, speed):
    setSpeed(motor_number, speed)
    mcp.output(pins.motorEnableA[motor_number], pins.HIGH)
    mcp.output(pins.motorEnableB[motor_number], pins.LOW)

def counter_clockwise(motor_number, speed):
    setSpeed(motor_number, speed)
    mcp.output(pins.motorEnableA[motor_number], pins.LOW)
    mcp.output(pins.motorEnableB[motor_number], pins.HIGH)

def stop(motor_number):
    setSpeed(motor_number, 0)
    mcp.output(pins.motorEnableA[motor_number], pins.LOW)
    mcp.output(pins.motorEnableB[motor_number], pins.LOW)

#TODO make sure this is right
def setSpeed(motor_number, speed):
    if 0 < speed <= 1000:
        #io.output(pins.motorPWM[motor_number], True)
        wiringpi.softPwmWrite(pins.motorPWM[motor_number], speed)
    else:
        #io.output(pins.motorPWM[motor_number], False)
        wiringpi.softPwmWrite(pins.motorPWM[motor_number], 0)

        
        
        
def resetAllEncoders():
    for i in range(4):
        encoders[i].reset()
        
def stopAllMotors():
    for i in range(4):
        stop(i)
        
def turnOnLED():
    mcp.config(14, OUTPUT)
    mcp.output(14, 1)
    time.sleep(2)
    mcp.output(14, 0)
    
