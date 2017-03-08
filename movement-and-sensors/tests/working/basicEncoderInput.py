# basicEncoderInput.py
# Test program to read the encoders on the motors
# Note that if you power the motor, it will output really quickly because the encoder
# 	values are changing at a rapid pace. Use manual(with like... pliers...) to
#	get a better feel for it

# We will poll the pin and output the result if something changed
# In order for the pi to actually read anything, a pull-up resistor must be used
# 	Not completely sure why this works, but it does.

import RPi.GPIO as GPIO # Allows use of pins on the Pi

GPIO.setmode(GPIO.BOARD) # Refer to pins on the board by their number (reference pin schematic)
encoderA = 5 # Set the input on pin 5
encoderB = 7 # Set the input on pin 7


# Setup pins as input and activate pullup resistor
GPIO.setup(encoderA, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(encoderB, GPIO.IN, GPIO.PUD_UP)

# State save to tell if something changes, will either be a 0 or 1 so I default
# to 0 as the initial state
stateASave = 0
stateBSave = 0

# Infinite loop to print out 1 or 0 depending on encoder input
while True:
	# Read the encoder input
	stateA = GPIO.input(encoderA)
	stateB = GPIO.input(encoderB)

	# Print both states if something changes in either state and update the
	# 	current state
	# Also casts the states as a string to remove ambiguity. Likely not needed
	if str(stateA) != str(stateASave):
		print ("A: " , stateA),
		print ("B: " , stateB)
		stateASave = stateA
	if str(stateB) != str(stateBSave):
		print ("A: " , stateA),
		print ("B: " , stateB)
		stateBSave = stateB
