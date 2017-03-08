# basicEncoderInput.py
# Test program to read encoders on the motors
# 	currently only tested by manual movement of the motor

# We will poll the pin and output the result if something changed
# In order for the pi to actually read anything, a pull-up resistor must be used
# 	Not completely sure how this works, but it does
#	What this also does is that it causes the input default to be HIGH 

import RPi.GPIO as GPIO # Allows use of pins on the Pi
import time # Time delay function to not kill the processor =\

GPIO.setmode(GPIO.BOARD) # Refer to pins on the board by their number (reference pin schematic)
encoderA = 5 # Set the input on pin 5
encoderB = 7 # Set the input on pin 7


# Setup pins as input and activate pullup resistor
GPIO.setup(encoderA, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(encoderB, GPIO.IN, GPIO.PUD_UP)

# Infinite loop to print out HIGH or LOW depending on encoder input
# By default the pin will be high because of the pull-up resistor
while True:
	# Read the encoder input
	stateA = GPIO.input(encoderA)
	stateB = GPIO.input(encoderB)

	# State save to tell if something changes
	stateASave = GPIO.HIGH
	stateBSave = GPIO.HIGH
	
	# Print both states if something changes and update the current state
	# must cast the state as a string
	if stateA != stateASave:
		print ("A: " , str(stateA)),
		print ("B: " , str(stateB))
		stateASave = stateA

	if stateB != stateBSave:
		print ("A: " , str(stateA)),
		print ("B: " , str(stateB))
		stateBSave = stateB

	time.sleep(.5) # Tells the pi to chill for half a second