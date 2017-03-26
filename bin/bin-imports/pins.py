#!/usr/bin/env python

#a module for storing all wiring information and pin numbers
#NEVER USE PIN 13 for OUTPUT
#GPIO23 and GPIO6 arent working!

#Left Front Motor Pins
leftFrontListNum = 0

leftFrontMotorPWM = 35 #GPIO19 ALL PWM IS BOARD MODE (bc of wiringpi)
leftFrontMotorEnableA = 9
leftFrontMotorEnableB = 8
leftFrontEncoderChA = 16
leftFrontEncoderChB = 12

#Right Front Motor Pins
rightFrontListNum = 1

rightFrontMotorPWM = 37 #GPIO26 ALL PWM IS BOARD MODE
rightFrontMotorEnableA = 1 
rightFrontMotorEnableB = 0
rightFrontEncoderChA = 21
rightFrontEncoderChB = 20

#Left Rear Motor Pins
leftRearListNum = 2

leftRearMotorPWM = 22 #GPIO 25 ALL PWM IS BOARD MODE
leftRearMotorEnableA = 11
leftRearMotorEnableB = 10
leftRearEncoderChA = 14
leftRearEncoderChB = 15

#Right Rear Motor Pins
rightRearListNum = 3

rightRearMotorPWM = 29 #GPIO5 ALL PWM IS BOARD MODE
rightRearMotorEnableA = 3
rightRearMotorEnableB = 2
rightRearEncoderChA = 4
rightRearEncoderChB = 17

INPUT = HIGH = 1
OUTPUT = LOW = 0



#array versions
motorEncoderA = [0 for a in range(4)]
motorEncoderB = [0 for a in range(4)]
motorEnableA = [0 for a in range(4)]
motorEnableB = [0 for a in range(4)]
motorPWM = [0 for a in range(4)]


motorEnableA[0] = leftFrontMotorEnableA
motorEnableA[1] = rightFrontMotorEnableA
motorEnableA[2] = leftRearMotorEnableA
motorEnableA[3] = rightRearMotorEnableA

motorEnableB[0] = leftFrontMotorEnableB
motorEnableB[1] = rightFrontMotorEnableB
motorEnableB[2] = leftRearMotorEnableB
motorEnableB[3] = rightRearMotorEnableB

motorEncoderA[0] = leftFrontEncoderChA
motorEncoderA[1] = rightFrontEncoderChA
motorEncoderA[2] = leftRearEncoderChA
motorEncoderA[3] = rightRearEncoderChA

motorEncoderB[0] = leftFrontEncoderChB
motorEncoderB[1] = rightFrontEncoderChB
motorEncoderB[2] = leftRearEncoderChB
motorEncoderB[3] = rightRearEncoderChB

motorPWM[0] = leftFrontMotorPWM
motorPWM[1] = rightFrontMotorPWM
motorPWM[2] = leftRearMotorPWM
motorPWM[3] = rightRearMotorPWM

# displays
matrix = range(1, 32)	#each led has 1 pin for on and 3 pins for rgb
segment = [11,12,13,15,16,18,22]
