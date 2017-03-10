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
encoderA_old = 0
encoderB_old = 0

# Setup pins as input and activate pullup resistor
GPIO.setup(encoderA, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(encoderB, GPIO.IN, GPIO.PUD_UP)

# State save to tell if something changes, will either be a 0 or 1 so I default
# to 0 as the initial state
stateA_old = 0
stateB_old = 0

# Revolution state save
rev = 0
rev_old = 0
# Increments based on motor phase changes
counts = 0

while True:
	# Infinite loop to print out 1 or 0 depending on encoder input
	# Read the encoder input
	stateA = GPIO.input(encoderA)
	stateB = GPIO.input(encoderB)

	# Print both states if something changes in either state and update the current state
	# Also casts the states as a string to remove ambiguity. Likely not needed
	if str(stateA) != str(stateA_old):
		if ((stateA, stateB_old) == (0,0)) or ((stateA, stateB_old) == (1,1)):
	 		# IF clockwise rotation
			counts += 1
			# print 'Encoder count is %s\nAB is %s %s' % (counts, stateA, stateB)
			# print 'Going clockwise'

	if str(stateB) != str(stateB_old):
		if ((stateA, stateB_old) == (0,1)) or ((stateA, stateB_old) == (1,0)):
			# IF counter-clockwise rotation
			counts -= 1
			# print 'Encoder count is %s\nAB is %s %s' % (counts, stateA, stateB)
			# print 'Going counter-clockwise'

	# Increments revolutions per 600 phase counts if clockwise
	if counts == 600:
		counts = 0
		rev += 1 

	# Decrements revolutions per 600 phase counts if counter-clockwise
	if counts == -600:
		counts = 0;
		rev -= 1

	if str(rev) != str(rev_old):
		print 'Shaft revolutions: ' + str(rev)
	
	rev_old = rev
	stateA_old, stateB_old = stateA, stateB
