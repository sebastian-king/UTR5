#!/usr/bin/env python

#a module for storing all wiring information and pin numbers
#NEVER USE PIN 13 for OUTPUT
#GPIO23 and GPIO6 arent working!

#Left Front Motor Pins
leftFrontListNum = 0

leftFrontMotorPWM = 19 #board 35
leftFrontMotorEnableA = 6 #old 9
leftFrontMotorEnableB = 7 #old 8
leftFrontEncoderChA = 16
leftFrontEncoderChB = 12

#Right Front Motor Pins
rightFrontListNum = 1

rightFrontMotorPWM = 26 #board 37
rightFrontMotorEnableA = 9 
rightFrontMotorEnableB = 8
rightFrontEncoderChA = 21
rightFrontEncoderChB = 20

#Left Rear Motor Pins
leftRearListNum = 2

leftRearMotorPWM = 25 #board 22
leftRearMotorEnableA = 5 #old 11
leftRearMotorEnableB = 4 #old 10
leftRearEncoderChA = 14
leftRearEncoderChB = 15

#Right Rear Motor Pins
rightRearListNum = 3

rightRearMotorPWM = 5 #board 29
rightRearMotorEnableA = 10
rightRearMotorEnableB = 11
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
