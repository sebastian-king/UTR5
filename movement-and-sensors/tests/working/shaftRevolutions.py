# shaftRevolutions.py
# Test program to translate encoder input to revolutions (specific to 17rpm motor)
# We will poll the pin and update our revolutions if something changes
# At the specified number of encoder state changes(600 in this case), we increment or
#	decrement revolutions

import RPi.GPIO as GPIO # Allows use of pins on the Pi

GPIO.setmode(GPIO.BOARD) # Refer to pins on the board by their number (reference pin schematic)
encoderA = 5 # Set the input on pin 5
encoderB = 7 # Set the input on pin 7

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
	# Read the encoder input
	stateA = GPIO.input(encoderA)
	stateB = GPIO.input(encoderB)

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
