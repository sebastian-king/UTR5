# interruptEncoders.py
# Interrupt based encoder reading so the program can do other things but
# 	not focus on polling the encoders

# Allow use of the Pi and clock in python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) # Use pin numbering

# These gets called when a change is read on the encoder
def interruptHandler1(void):
	print "A: " + str(GPIO.input(encoderA))

def interruptHandler2(void):
	print "B: " + str(GPIO.input(encoderB))



# Designate which pin to use
encoderA = 5
encoderB = 7

# Setup pins as input and use pull-up resistor
GPIO.setup(5, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN, GPIO.PUD_UP)

# This is what actually sets up the interrupt on pin 5 and 7
# It sets up the interrupt to trigger any time the pin changes
# The interrupt will then "callback"  to the interrupt handler which will
# 	print out the input
GPIO.add_event_detect(5, GPIO.BOTH, callback = interruptHandler1)
GPIO.add_event_detect(7, GPIO.BOTH, callback = interruptHandler2)

# Infinite loop, if no interrupt encountered, will print this forever
# sleep time is used to actually see the interrupts
while 1:
	print "Waiting"
	time.sleep(1)
