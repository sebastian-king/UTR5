#!/usr/bin/env python

import sys
from encoder import encoder     #encoder.py has encoder class that takes 2 pins for quadrature encoders
import pins
import time
from Adafruit_MCP230xx import *
import RPi.GPIO as io
import wiringpi

#motor numbers: LF=0 RF=1 LB=2 RB=3
#array of motor encoders
encoders = [0 for a in range(4)]

#gpio expander setup
mcp = Adafruit_MCP230XX(busnum = 0, address = 0x20, num_gpios = 16)




#CALL THIS BEFORE RUNMOTORS
#sets up GPIO, encoders, interrupts
def initMotors():
    wiringpi.wiringPiSetupGpio()    #wiringpi setup
    io.setmode(io.BCM)              #gpio pinmode
    
    for i in range(4):
        encoders[i] = encoder(pins.motorEncoderA[i], pins.motorEncoderB[i])     #set up encoder object
        mcp.config(pins.motorEnableA[i], pins.OUTPUT)       #set up the h-bridge a and b pins
        mcp.config(pins.motorEnableB[i], pins.OUTPUT)
        #io.setup(pins.motorPWM[i], io.OUT)
        wiringpi.pinMode(pins.motorPWM[i], pins.OUTPUT)     #set up wiringpi software pwms
        error = wiringpi.softPwmCreate(pins.motorPWM[i],0,1000)
        if error != 0:
            print "error with wiringpi PWM setup in motortest for motor %s" % i       
        stop(i)                 #make sure the motor is stopped
    

#TODO test this make sure it works
#motor numbers: LF=0 RF=1 LB=2 RB=3
#directions: 1 = clockwise, 0 = counter_clockwise
def runMotors(pulses, speed, dirLF, dirRF, dirLB, dirRB):    
    #set pulses to 0
    for i in range(4):
        encoders[i].reset()
    
    #start all motors in desired directions
    rotate(0, speed, dirLF)
    rotate(1, speed, dirRF)
    rotate(2, speed, dirLB)
    rotate(3, speed, dirRB)
    
    #stop when right front motor hits pulse number
    moving = True         
    while moving == True:
        print 'encoder pulses: %s' % (encoders[1].getPulses())
        if abs(encoders[1].getPulses()) >= abs(pulses):
            moving = False
    
    for i in range(4):
        stop(i)
    
    print "final pulses: FL/0=%s, FR/1=%s, BL/2=%s, BR/3=%s" % (encoders[0].getPulses(), encoders[1].getPulses(), encoders[2].getPulses(), encoders[3].getPulses())    
    #stop when all motors hit pulse number (option 2)
    #==============================================================
    # numMotorsRotating = 4        
    # while numMotorsRotating != 0:
    #     for i in range(4):
    #         if abs(encoders[i].getPulses()) >= abs(pulses):
    #             stop(i)
    #             numMotorsRotating = numMotorsRotating - 1
    #==============================================================
            



#helper methods used by runMotors    
    
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
        wiringpi.softPwmWrite(pins.motorPWM[motor_number], speed)
    else:
        wiringpi.softPwmWrite(pins.motorPWM[motor_number], 0)
