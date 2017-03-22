#!/usr/bin/env python


#encoder.py has encoder class that takes 2 pins for quadrature encoders
import encoder
import pins

import RPi.GPIO as io
import wiringpi
io.setmode(io.BCM)
wiringpi.wiringPiSetupGpio()


#list of encoder objects
#motor numbers: LF=0 RF=1 LB=2 RB=3
motorEncoders = [0 for a in range(4)]



    
def encoderHandlerRF():
    motorEncoders[1].monitor();




#sets up GPIO, encoders, interrupts
def initMotors():
    #TODO make sure pwm is set up right
    wiringpi.pinMode(pins.rightFrontMotorPWM, 2)
    wiringpi.pwmWrite(pins.rightFrontMotorPWM, 0)     #set all speeds to 0
    
    #TODO make sure gpio is set up right
    #set up GPIO
    io.setup(pins.rightFrontMotorEnableA, io.OUT)
    io.setup(pins.rightFrontMotorEnableB, io.OUT)
    
    stop(1)
    #create encoder list
    motorEncoders[0] = encoder(pins.motorEncoderA[1], pins.motorEncoderB[1])
    
    #set up interrupts
    GPIO.add_event_detect(pins.motorEncoderA[1], GPIO.BOTH, callback = encoderHandlerRF)
    GPIO.add_event_detect(pins.motorEncoderB[1], GPIO.BOTH, callback = encoderHandlerRF)    



#TODO test this make sure it works
#motor numbers: LF=0 RF=1 LB=2 RB=3
def runMotor(pulses):    
    speed = 512
    
    #set pulses to 0
    motorEncoders[0].resetPulses()
    
    rotate(1, speed, 1)

    
    numMotorsRotating = 1
            
    while numMotorsRotating != 0:
        if abs(motorEncoders[0].getPulses()) >= pulses:
            stop(1)
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
    io.output(pins.motorEnableA[motor_number], True)

def stop(motor_number):
    #TODO im not sure why the speed is set to 254 in motors_with_encoders
    speed(motor_number, 254)
    io.output(pins.motorEnableA[motor_number], True)
    io.output(pins.motorEnableB[motor_number], True)

#TODO make sure this is right
def speed(motor_number, speed):
    if 0 <= speed <= 1024:
        wiringpi.pwmWrite(pins.motorPwm[motor_number], speed)
    else:
        wiringpi.pwmWrite(pins.motorPwm[motor_number], 0)
