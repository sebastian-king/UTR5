# basicEncoderInput.py
# Test program to read encoders on the motors
# 	currently only tested by manual movement of the motor

# We will constantly poll the pin and output the result
# In order for the pi to actually read anything, a pull-up resistor must be used
# 	Not completely sure how this works, but it does
#	What this also does is that it causes the input read to be HIGH 

import RPi.GPIO as GPIO # Allows use of pins on the Pi


GPIO.setmode(GPIO.BOARD) # Refer to pins on the board by their number (reference pin schematic)
encoderA = 5 # Set the input on pin 7


# Setup pins as input and activate pullup resistor
GPIO.setup(encoderA, GPIO.IN, GPIO.PUD_UP)

# Infinite loop to constantly print out HIGH or LOW depending on encoder input
# By default the pin will be high because of the pull-up resistor
while True:
	state = GPIO.input(encoderA)
	if state == GPIO.HIGH:
		print "HIGH"
	else:
		print "LOW"
