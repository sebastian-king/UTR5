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
encoder1 = encoder(pins.motorEncoderA[1], pins.motorEncoderB[1])



    
def encoderHandlerRF(void):
    encoder1.monitor();




#sets up GPIO, encoders, interrupts
def initMotor():
    io.setmode(io.BCM)
    
    #TODO make sure pwm is set up right
    wiringpi.pinMode(pins.rightFrontMotorPWM, 2)
    wiringpi.pwmWrite(pins.rightFrontMotorPWM, 0)     #set all speeds to 0
    
    #TODO make sure gpio is set up right
    #set up GPIO
    io.setup(pins.rightFrontMotorEnableA, io.OUT)
    io.setup(pins.rightFrontMotorEnableB, io.OUT)
    
    stop(1)
    
    #set up interrupts
    io.add_event_detect(pins.motorEncoderA[1], io.BOTH, callback = encoderHandlerRF)
    io.add_event_detect(pins.motorEncoderB[1], io.BOTH, callback = encoderHandlerRF)    



#TODO test this make sure it works
#motor numbers: LF=0 RF=1 LB=2 RB=3
def runMotor(pulses):    
    speed = 1000
    
    #set pulses to 0
    encoder1.resetPulses()
    
    rotate(1, speed, 1)

    
    numMotorsRotating = 1
            
    while numMotorsRotating != 0:
        if abs(encoder1.getPulses()) >= pulses:
            stop(1)
            numMotorsRotating = numMotorsRotating - 1
            

    
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
    io.output(pins.motorEnableA[motor_number], True)

def stop(motor_number):
    #TODO im not sure why the speed is set to 254 in motors_with_encoders
    setSpeed(motor_number, 254)
    io.output(pins.motorEnableA[motor_number], True)
    io.output(pins.motorEnableB[motor_number], True)

#TODO make sure this is right
def setSpeed(motor_number, speed):
    if 0 < speed <= 1024:
        io.output(pins.motorPwm[motor_number], True)
        #wiringpi.pwmWrite(pins.motorPwm[motor_number], speed)
    else:
        io.output(pins.motorPwm[motor_number], False)
        #wiringpi.pwmWrite(pins.motorPwm[motor_number], 0)
