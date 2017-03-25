#!/usr/bin/env python

#WHAT WE NEED TO DO: MOVEMENT TESTING
#this is a simple test for the encoder and motor, the right front
#import motortest in python on the pi
#call initMotor()
#call clockwise(1, 1), counter_clockwise(1, 1), and stop(1)
#if all of the above works:
#call runMotor(num_pulses), make sure it rotates and stops 
#make sure encoders are working
#>>>WE ARE HERE<<<
#once that works, we need to figurue out pwm stuff for speed
#once this whole test works, we can update/test motors.py in the same way, which is this but with all 4 motors
#when motors.py works, we can test movement_wrapper.strafe_one_block(direction), this is what handles 600 pulses/rot, wheel size constants, etc



#encoder.py has encoder class that takes 2 pins for quadrature encoders
import sys
from encoder import encoder
#from encoder import encoder
import pins
import time
from Adafruit_MCP230xx import *
import RPi.GPIO as io
#import wiringpi
#wiringpi.wiringPiSetupGpio()


#motor numbers: LF=0 RF=1 LB=2 RB=3
rightFrontEncoder = encoder(pins.rightFrontEncoderChA, pins.rightFrontEncoderChB)
leftFrontEncoder = encoder(pins.leftFrontEncoderChA, pins.leftFrontEncoderChB)
rightRearEncoder = encoder(pins.rightRearEncoderChA, pins.rightRearEncoderChB)
leftRearEncoder = encoder(pins.leftRearEncoderChA, pins.leftRearEncoderChB)

encoders = [rightFrontEncoder,leftFrontEncoder, rightRearEncoder, leftRearEncoder]

mcp = Adafruit_MCP230XX(busnum = 0, address = 0x20, num_gpios = 16)

#CALL THIS BEFORE RUNMOTOR
#sets up GPIO, encoders, interrupts
def initMotor():
    io.setmode(io.BCM)
    
    #TODO make sure pwm is set up right
    #wiringpi.pinMode(pins.rightFrontMotorPWM, 2)
    
    #TODO make sure gpio is set up right
    #io.setup(pins.rightFrontMotorEnableA, io.OUT)
    #io.setup(pins.rightFrontMotorEnableB, io.OUT)
    #io.setup(pins.rightFrontMotorPWM, io.OUT)
    
    for i in range(4):
        mcp.config(pins.motorEnableA[i], pins.OUTPUT)
        mcp.config(pins.motorEnableB[i], pins.OUTPUT)
        io.setup(pins.motorPWM[i], io.OUT)
        stop(i)
        
    print 'initMotor() completed'


#TODO test this make sure it works
#running clockwise function on motor 1 (right front) to test
#motor numbers: LF=0 RF=1 LB=2 RB=3
def runMotor(pulses, dir):    
    speed = 1000
    
    #set pulses to 0
    resetEncoders()
    
    for i in range(4):
        rotate(i, speed, dir)

    print 'runMotor() motor started'
    
    moving = True
            
    while moving == True:
        print 'encoder pulses: %s' % (rightFrontEncoder.getPulses())
        if abs(rightFrontEncoder.getPulses()) >= pulses:
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
    if 0 < speed <= 1024:
        io.output(pins.motorPWM[motor_number], True)
        #wiringpi.pwmWrite(pins.motorPwm[motor_number], speed)
    else:
        io.output(pins.motorPWM[motor_number], False)
        #wiringpi.pwmWrite(pins.motorPwm[motor_number], 0)
        
def resetEncoders():
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
    
