#!/usr/bin/env python

#encoder.py has encoder class that takes 2 pins for quadrature encoders
import sys
from encoder import encoder
import pins

import RPi.GPIO as io
import wiringpi
wiringpi.wiringPiSetupGpio()


#list of encoder objects
#motor numbers: LF=0 RF=1 LB=2 RB=3
#motorEncoders = [0 for a in range(0, 3)]


#sets up GPIO, encoders, interrupts
def initMotors():
    io.setmode(io.BCM)
    #TODO make sure pwm is set up right
    for m in pins.motorPwm:
        wiringpi.pinMode(m,2)
        wiringpi.pwmWrite(m, 0)     #set all speeds to 0
    
    #TODO make sure gpio is set up right
    #set up GPIO
    for m in pins.motorEnableA:
        io.setup(m, io.OUT)
    for m in pins.motorEnableB:
        io.setup(m, io.OUT)
    
    #make sure bot is at rest
    for i in range(0, 3):
        stop(i)
    
    #create encoder list
    for i in range(0, 3):
        motorEncoders[i] = encoder(pins.motorEncoderA[i], pins.motorEncoderB[i])
    

#TODO test this make sure it works
#motor numbers: LF=0 RF=1 LB=2 RB=3
def run_all_motors(speed, pulses, dir0, dir1, dir2, dir3):    
    #set pulses to 0
    for e in motorEncoders:
        e.reset()
    
    rotate(0, speed, dir0)
    rotate(1, speed, dir1)
    rotate(2, speed, dir2)
    rotate(3, speed, dir3)
    
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
    speed(motor_number, speed)
    io.output(pins.motorEnableA[motor_number], True)
    io.output(pins.motorEnableB[motor_number], False)

def counter_clockwise(motor_number, speed):
    speed(motor_number, speed)
    io.output(pins.motorEnableA[motor_number], False)
    io.output(pins.motorEnableB[motor_number], True)

def stop(motor_number):
    speed(motor_number, 0)
    io.output(pins.motorEnableA[motor_number], False)
    io.output(pins.motorEnableB[motor_number], False)

#TODO make sure this is right
def speed(motor_number, speed):
    if 0 <= speed <= 1024:
        wiringpi.pwmWrite(pins.motorPwm[motor_number], speed)
    else:
        wiringpi.pwmWrite(pins.motorPwm[motor_number], 0)
