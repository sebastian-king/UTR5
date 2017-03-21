#!/usr/bin/env python

#encoder.py has encoder class that takes 2 pins for quadrature encoders
import encoder

import RPi.GPIO as io
import wiringpi
io.setmode(io.BCM)
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18,2)
wiringpi.pwmWrite(18, 0)

#list of encoder objects
motorEncoders = [0 for a in range(0, 3)]



#interrupt that updates encoders
def encoderHandlerLF(void):
    motorEncoders[0].monitor();
    
def encoderHandlerRF(void):
    motorEncoders[1].monitor();
    
def encoderHandlerLB(void):
    motorEncoders[2].monitor();
    
def encoderHandlerRB(void):
    motorEncoders[3].monitor();




def initMotors(void):
    #set up GPIO
    for m in pins.motorEnableA:
        io.setup(m, io.OUT)
    for m in pins.motorEnableB:
        io.setup(m, io.OUT)
    
    #create encoder list
    for i in range(0, 3):
        motorEncoders[i] = encoder(pins.motorEncoderA[i], pins.motorEncoderB[i])
    
    #set up interrups
    GPIO.add_event_detect(pins.motorEncoderA[0], GPIO.BOTH, callback = encoderHandlerLF)
    GPIO.add_event_detect(pins.motorEncoderB[0], GPIO.BOTH, callback = encoderHandlerLF)
    GPIO.add_event_detect(pins.motorEncoderA[1], GPIO.BOTH, callback = encoderHandlerRF)
    GPIO.add_event_detect(pins.motorEncoderB[1], GPIO.BOTH, callback = encoderHandlerRF)    
    GPIO.add_event_detect(pins.motorEncoderA[2], GPIO.BOTH, callback = encoderHandlerLB)
    GPIO.add_event_detect(pins.motorEncoderB[2], GPIO.BOTH, callback = encoderHandlerLB)
    GPIO.add_event_detect(pins.motorEncoderA[3], GPIO.BOTH, callback = encoderHandlerRB)
    GPIO.add_event_detect(pins.motorEncoderB[3], GPIO.BOTH, callback = encoderHandlerRB)



def run_all_motors(speed, pulses, dir1, dir2, dir3, dir4):    
    #set distances to 0
    for e in motorEncoders:
        e.resetPulses()
    
    rotate(0, speed, dir1)
    rotate(1, speed, dir2)
    rotate(2, speed, dir3)
    rotate(3, speed, dir4)
    
    numMotorsRotating = 4
            
    while numMotorsRotating != 0:
        for i in range(0, 3):
            if motorEncoders[i].getPulses() == pulses:
                stop(i)
                numMotorsRotating = numMotorsRotating - 1
            

    
#motor numbers: LF=0 RF=1 LB=2 RB=3
def rotate(motor_number, speed, dir):
    if dir == 1:
        clockwise(motor_number, speed)
    else:
        counter_clockwise(motor_number, speed)

def clockwise(motor_number, speed):
    speed(speed)
    io.output(pins.motorEnableA[motor_number], True)
    io.output(pins.motorEnableB[motor_number], False)

def counter_clockwise(motor_number, speed):
    speed(speed)
    io.output(pins.motorEnableA[motor_number], False)
    io.output(pins.motorEnableA[motor_number], True)

def stop(motor_number):
    speed(254)
    io.output(pins.motorEnableA[motor_number], True)
    io.output(pins.motorEnableB[motor_number], True)

def speed(speed):
    if 0 <= speed <= 1024:
        wiringpi.pwmWrite(18, speed)
    else:
        wiringpi.pwmWrite(18, 0)
