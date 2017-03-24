#!/usr/bin/env python

#a module for storing all wiring information and pin numbers
#NEVER USE PIN 13 for OUTPUT

#Left Front Motor Pins
leftFrontMotorPWM = 24
leftFrontMotorEnableA = 0
leftFrontMotorEnableB = 0
leftFrontEncoderChA = 7
leftFrontEncoderChB = 8

#Right Front Motor Pins
rightFrontMotorPWM = 23
rightFrontMotorEnableA = 5 
rightFrontMotorEnableB = 6
rightFrontEncoderChA = 20
rightFrontEncoderChB = 21

#Left Rear Motor Pins
leftRearMotorPWM = 18
leftRearMotorEnableA = 0
leftRearMotorEnableB = 0
leftRearEncoderChA = 14
leftRearEncoderChB = 15

#Right Rear Motor Pins
rightRearMotorPWM = 12
rightRearMotorEnableA = 0
rightRearMotorEnableB = 0
rightRearEncoderChA = 4
rightRearEncoderChB = 17




#array versions
motorEncoderA = [0 for a in range(4)]
motorEncoderB = [0 for a in range(4)]
motorEnableA = [0 for a in range(4)]
motorEnableB = [0 for a in range(4)]
motorPwm = [0 for a in range(4)]


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

motorPwm[0] = leftFrontMotorPWM
motorPwm[1] = rightFrontMotorPWM
motorPwm[2] = leftRearMotorPWM
motorPwm[3] = rightRearMotorPWM

# displays
matrix = range(1, 32)	#each led has 1 pin for on and 3 pins for rgb
segment = [11,12,13,15,16,18,22]
