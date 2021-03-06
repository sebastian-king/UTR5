#!/usr/bin/env python

from Adafruit_MCP230xx import *


#a module for storing all wiring information and pin numbers
#NEVER USE PIN 13 for OUTPUT
#GPIO23 and GPIO6 arent working!

#gpio expander setup
mcp20 = Adafruit_MCP230XX(busnum = 1, address = 0x20, num_gpios = 16) #Motor drivers
mcp21 = Adafruit_MCP230XX(busnum = 1, address = 0x21, num_gpios = 16) #Green and row enables 8x8
mcp22 = Adafruit_MCP230XX(busnum = 1, address = 0x22, num_gpios = 16) #Blue and red 8x8
mcp23 = Adafruit_MCP230XX(busnum = 1, address = 0x23, num_gpios = 16) #7 segment


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
segment = range(0,7) # 8 elements, a..g, last one for decimal point, on expander 0x23




#BLUE on gpio expander 0x22
display8x8p1 = 8
display8x8p2 = 9
display8x8p3 = 10
display8x8p4 = 11
display8x8p5 = 12
display8x8p6 = 13
display8x8p7 = 14
display8x8p8 = 15

#RED on gpio expander 0x22
display8x8p9 = 7
display8x8p10 = 6
display8x8p11 = 5
display8x8p12 = 4
display8x8p13 = 3
display8x8p14 = 2
display8x8p15 = 1
display8x8p16 = 0

#GREEN on gpio expander 0x21
display8x8p28 = 11
display8x8p27 = 10
display8x8p26 = 9
display8x8p25 = 8
display8x8p24 = 0
display8x8p23 = 1
display8x8p22 = 2
display8x8p21 = 3

#ROW ENABLES on gpio expander 0x21
display8x8p17 = 7
display8x8p18 = 6
display8x8p19 = 5
display8x8p20 = 4
display8x8p29 = 12
display8x8p30 = 13
display8x8p31 = 14
display8x8p32 = 15

display8x8RedCol = [0 for a in range(8)]
display8x8GreenCol = [0 for a in range(8)]
display8x8BlueCol = [0 for a in range(8)]
display8x8Row = [0 for a in range(8)]

display8x8RedCol[0] = display8x8p9
display8x8RedCol[1] = display8x8p10
display8x8RedCol[2] = display8x8p11
display8x8RedCol[3] = display8x8p12
display8x8RedCol[4] = display8x8p13
display8x8RedCol[5] = display8x8p14
display8x8RedCol[6] = display8x8p15
display8x8RedCol[7] = display8x8p16

display8x8GreenCol[0] = display8x8p28
display8x8GreenCol[1] = display8x8p27
display8x8GreenCol[2] = display8x8p26
display8x8GreenCol[3] = display8x8p25
display8x8GreenCol[4] = display8x8p24
display8x8GreenCol[5] = display8x8p23
display8x8GreenCol[6] = display8x8p22
display8x8GreenCol[7] = display8x8p21

display8x8BlueCol[0] = display8x8p1
display8x8BlueCol[1] = display8x8p2
display8x8BlueCol[2] = display8x8p3
display8x8BlueCol[3] = display8x8p4
display8x8BlueCol[4] = display8x8p5
display8x8BlueCol[5] = display8x8p6
display8x8BlueCol[6] = display8x8p7
display8x8BlueCol[7] = display8x8p8

display8x8Row[0] = display8x8p17
display8x8Row[1] = display8x8p18
display8x8Row[2] = display8x8p19
display8x8Row[3] = display8x8p20
display8x8Row[4] = display8x8p29
display8x8Row[5] = display8x8p30
display8x8Row[6] = display8x8p31
display8x8Row[7] = display8x8p32


# 7 segment
#On GPIO Expander 0x23
sevenSegPinA = 0
sevenSegPinB = 1
sevenSegPinC = 2
sevenSegPinD = 3
sevenSegPinE = 4
sevenSegPinF = 5
sevenSegPinG = 6
sevenSegPinDP = 7
segments = range(7)
