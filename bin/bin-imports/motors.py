#!/usr/bin/env python

#encoder.py has encoder class that takes 2 pins for quadrature encoders
import encoder

import RPi.GPIO as io
import wiringpi
io.setmode(io.BCM)
wiringpi.wiringPiSetupGpio()


#list of encoder objects
#motor numbers: LF=0 RF=1 LB=2 RB=3
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



#sets up GPIO, encoders, interrupts
def initMotors(void):
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
    
    #set up interrupts
    GPIO.add_event_detect(pins.motorEncoderA[0], GPIO.BOTH, callback = encoderHandlerLF)
    GPIO.add_event_detect(pins.motorEncoderB[0], GPIO.BOTH, callback = encoderHandlerLF)
    GPIO.add_event_detect(pins.motorEncoderA[1], GPIO.BOTH, callback = encoderHandlerRF)
    GPIO.add_event_detect(pins.motorEncoderB[1], GPIO.BOTH, callback = encoderHandlerRF)    
    GPIO.add_event_detect(pins.motorEncoderA[2], GPIO.BOTH, callback = encoderHandlerLB)
    GPIO.add_event_detect(pins.motorEncoderB[2], GPIO.BOTH, callback = encoderHandlerLB)
    GPIO.add_event_detect(pins.motorEncoderA[3], GPIO.BOTH, callback = encoderHandlerRB)
    GPIO.add_event_detect(pins.motorEncoderB[3], GPIO.BOTH, callback = encoderHandlerRB)


#TODO test this make sure it works
#motor numbers: LF=0 RF=1 LB=2 RB=3
def run_all_motors(speed, pulses, dir0, dir1, dir2, dir3):    
    #set pulses to 0
    for e in motorEncoders:
        e.resetPulses()
    
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
    speed(speed)
    io.output(pins.motorEnableA[motor_number], True)
    io.output(pins.motorEnableB[motor_number], False)

def counter_clockwise(motor_number, speed):
    speed(speed)
    io.output(pins.motorEnableA[motor_number], False)
    io.output(pins.motorEnableA[motor_number], True)

def stop(motor_number):
    #TODO im not sure why the speed is set to 254 in motors_with_encoders
    speed(254)
    io.output(pins.motorEnableA[motor_number], True)
    io.output(pins.motorEnableB[motor_number], True)

#TODO make sure this is right
def speed(motor_number, speed):
    if 0 <= speed <= 1024:
        wiringpi.pwmWrite(pins.motorPwm[motor_number], speed)
    else:
        wiringpi.pwmWrite(pins.motorPwm[motor_number], 0)
