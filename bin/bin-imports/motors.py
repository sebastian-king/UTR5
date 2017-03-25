#!/usr/bin/env python

#encoder.py has encoder class that takes 2 pins for quadrature encoders
import sys
from encoder import encoder
import pins
import RPi.GPIO as io
#import wiringpi

from Adafruit_MCP230xx import *

mcp = Adafruit_MCP230XX(busnum = 0, address = 0x20, num_gpios = 16)



#list of encoder objects
#motor numbers: LF=0 RF=1 LB=2 RB=3
motorEncoders = [0 for a in range(4)]


#sets up GPIO, encoders, interrupts
def initMotors():
    io.setmode(io.BCM)
    
    #wiringpi.wiringPiSetupGpio()
    #TODO make sure pwm is set up right
    #for m in pins.motorPwm:
    #    wiringpi.pinMode(m,2)
    #    wiringpi.pwmWrite(m, 0)     #set all speeds to 0
    
    #TODO make sure gpio is set up right
    #set up GPIO, pwm, encoder list
    for i in range(4):
        mcp.config(pins.motorEnableA[i], pins.OUTPUT)
        mcp.config(pins.motorEnableB[i], pins.OUTPUT)
        io.setup(pins.motorPWM[i], io.OUT)
        motorEncoders[i] = encoder(pins.motorEncoderA[i], pins.motorEncoderB[i])
        stop(i)
    

#TODO test this make sure it works
#motor numbers: LF=0 RF=1 LB=2 RB=3
#directions: 1 = clockwise, 0 = counterclockwise
def run_all_motors(speed, pulses, dirLF, dirRF, dirLB, dirRB):    
    #set pulses to 0
    for e in motorEncoders:
        e.reset()
    
    rotate(0, speed, dirLF)
    rotate(1, speed, dirRF)
    rotate(2, speed, dirLB)
    rotate(3, speed, dirRB)
    
    numMotorsRotating = 4
            
    while numMotorsRotating != 0:
        for i in range(0, 3):
            if abs(motorEncoders[i].getPulses()) >= pulses:
                stop(i)
                numMotorsRotating = numMotorsRotating - 1
            

    
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
def speed(motor_number, speed):
    if 0 <= speed <= 1024:
        wiringpi.pwmWrite(pins.motorPwm[motor_number], speed)
    else:
        wiringpi.pwmWrite(pins.motorPwm[motor_number], 0)
