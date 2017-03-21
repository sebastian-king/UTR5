#!/usr/bin/env python

#a module for storing all wiring information and pin numbers

#Left Front Motor Pins
leftFrontMotorPWM = 0
leftFrontMotorEnableA = 0
leftFrontMotorEnableB = 0
leftFrontEncoderChA = 0
leftFrontEncoderChB =0

#Right Front Motor Pins
rightFrontMotorPWM = 0
rightFrontMotorEnableA = 0
rightFrontMotorEnableB = 0
rightFrontEncoderChA = 0
rightFrontEncoderChB = 0

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


motorEnableA[0] = pins.leftFrontMotorEnableA
motorEnableA[1] = pins.rightFrontMotorEnableA
motorEnableA[2] = pins.leftRearMotorEnableA
motorEnableA[3] = pins.rightRearMotorEnableA

motorEnableB[0] = pins.leftFrontMotorEnableB
motorEnableB[1] = pins.rightFrontMotorEnableB
motorEnableB[2] = pins.leftRearMotorEnableB
motorEnableB[3] = pins.rightRearMotorEnableB

motorEncoderA[0] = pins.leftFrontEncoderChA
motorEncoderA[1] = pins.rightFrontEncoderChA
motorEncoderA[2] = pins.leftRearEncoderChA
motorEncoderA[3] = pins.rightRearEncoderChA

motorEncoderB[0] = pins.leftFrontEncoderChB
motorEncoderB[1] = pins.rightFrontEncoderChA
motorEncoderB[2] = pins.leftRearEncoderChB
motorEncoderB[3] = pins.rightRearEncoderChB

motorPwm[0] = pins.leftFrontMotorPWM
motorPwm[1] = pins.rightFrontMotorPWM
motorPwm[2] = pins.leftRearMotorPWM
motorPwm[3] = pins.rightRearMotorPWM