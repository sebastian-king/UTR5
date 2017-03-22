#!/usr/bin/env python

#a module for storing all wiring information and pin numbers

#Left Front Motor Pins
leftFrontMotorPWM = 0
leftFrontMotorEnableA = 0
leftFrontMotorEnableB = 0
leftFrontEncoderChA = 0
leftFrontEncoderChB =0

#Right Front Motor Pins
rightFrontMotorPWM = 26
rightFrontMotorEnableA = 5
rightFrontMotorEnableB = 6
rightFrontEncoderChA = 13
rightFrontEncoderChB = 19

#Left Rear Motor Pins
leftRearMotorPWM = 0
leftRearMotorEnableA = 0
leftRearMotorEnableB = 0
leftRearEncoderChA = 0
leftRearEncoderChB = 0

#Right Rear Motor Pins
rightRearMotorPWM = 0
rightRearMotorEnableA = 0
rightRearMotorEnableB = 0
rightRearEncoderChA = 0
rightRearEncoderChB = 0




#array versions
motorEncoderA = [0 for a in range(0, 3)]
motorEncoderB = [0 for a in range(0, 3)]
motorEnableA = [0 for a in range(0, 3)]
motorEnableB = [0 for a in range(0, 3)]
motorPwm = [0 for a in range(0, 3)]


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
motorEncoderB[1] = rightFrontEncoderChA
motorEncoderB[2] = leftRearEncoderChB
motorEncoderB[3] = rightRearEncoderChB

motorPwm[0] = leftFrontMotorPWM
motorPwm[1] = rightFrontMotorPWM
motorPwm[2] = leftRearMotorPWM
motorPwm[3] = rightRearMotorPWM

# displays
matrix = range(1, 32)	#each led has 1 pin for on and 3 pins for rgb
segment = [11,12,13,15,16,18,22]
