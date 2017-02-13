#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# what do drive pins 1-4 do??

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20,GPIO.OUT) # attached to pin 1
GPIO.setup(21,GPIO.OUT) # attacbed to pin 32
GPIO.setup(26,GPIO.OUT) # attached to pin 9
GPIO.setup(19,GPIO.OUT) # attacbed to pin 28

print "1" # white
GPIO.output(19,GPIO.LOW)
GPIO.output(20,GPIO.LOW)
GPIO.output(21,GPIO.HIGH)
GPIO.output(26,GPIO.LOW)
time.sleep(0.2)
print "2" # green
GPIO.output(19,GPIO.LOW)
GPIO.output(20,GPIO.HIGH)
GPIO.output(21,GPIO.HIGH)
GPIO.output(26,GPIO.HIGH)
time.sleep(0.2)
print "3" # blue
GPIO.output(19,GPIO.HIGH)
GPIO.output(20,GPIO.LOW)
GPIO.output(21,GPIO.HIGH)
GPIO.output(26,GPIO.HIGH)
time.sleep(0.2)
print "4" # red
GPIO.output(19,GPIO.HIGH)
GPIO.output(20,GPIO.HIGH)
GPIO.output(21,GPIO.HIGH)
GPIO.output(26,GPIO.LOW)
time.sleep(0.2)
print "5" # yellow
GPIO.output(19,GPIO.LOW)
GPIO.output(20,GPIO.HIGH)
GPIO.output(21,GPIO.HIGH)
GPIO.output(26,GPIO.LOW)
time.sleep(0.2)
print "6" # pink
GPIO.output(19,GPIO.HIGH)
GPIO.output(20,GPIO.LOW)
GPIO.output(21,GPIO.HIGH)
GPIO.output(26,GPIO.LOW)
time.sleep(0.2)
print "6" # cyan
GPIO.output(19,GPIO.LOW)
GPIO.output(20,GPIO.LOW)
GPIO.output(21,GPIO.HIGH)
GPIO.output(26,GPIO.HIGH)
time.sleep(0.2)
