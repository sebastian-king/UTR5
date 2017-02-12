#!/usr/bin/env python

import RPi.GPIO as GPIO
import os, sys

NUMBER = int(sys.argv[1])

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#setup output pins
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
#define 7 segment digits
d = [ None for y in range( 11 ) ]
d[10]=[1,1,1,1,1,1,1]
d[0]=[0,0,0,0,0,0,1]
d[1]=[1,0,0,1,1,1,1]
d[2]=[0,0,1,0,0,1,0]
d[3]=[0,0,0,0,1,1,0]
d[4]=[1,0,0,1,1,0,0]
d[5]=[0,1,0,0,1,0,0]
d[6]=[0,1,0,0,0,0,0]
d[7]=[0,0,0,1,1,1,1]
d[8]=[0,0,0,0,0,0,0]
d[9]=[0,0,0,1,1,0,0]
gpin=[11,12,13,15,16,18,22]
#routine to clear and then write to display
def digdisp(digit):
        for x in range (0,7):
                GPIO.output(gpin[x], d[10][x])
                for x in range (0,7):
                        GPIO.output(gpin[x], digit[x])
digdisp(d[NUMBER])
