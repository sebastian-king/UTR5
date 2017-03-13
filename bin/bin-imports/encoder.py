# a class to allow us to get the states of the encoders, i.e accumulated distance & speed

import RPi.GPIO as GPIO # Allows use of pins on the Pi

class Encoder:
    
    def __init__(self, pinA, pinB):
        GPIO.setmode(GPIO.BOARD)
        self.pinA = pinA
        self.pinB = pinB
        GPIO.setup(pinA, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(pinB, GPIO.IN, GPIO.PUD_UP)
        self.pulses = 0
    
    #call this continuously in the main class to monitor the encoders and accumulate distance values
    def monitor():
    # Infinite loop to print out 1 or 0 depending on encoder input
        # Read the encoder input
        if 'stateA_old' not in locals():
            stateA_old = 0
        if 'stateB_old' not in locals():
            stateB_old = 0
        
        stateA = GPIO.input(encoderA)
        stateB = GPIO.input(encoderB)
    
        # Print both states if something changes in either state and update the current state
        # Also casts the states as a string to remove ambiguity. Likely not needed
        if str(stateA) != str(stateA_old):
            if ((stateA, stateB_old) == (0,0)) or ((stateA, stateB_old) == (1,1)):
                 # IF clockwise rotation
                self.pulses += 1
                # print 'Encoder count is %s\nAB is %s %s' % (counts, stateA, stateB)
                # print 'Going clockwise'
    
        if str(stateB) != str(stateB_old):
            if ((stateA, stateB_old) == (0,1)) or ((stateA, stateB_old) == (1,0)):
                # IF counter-clockwise rotation
                self.pulses -= 1
                # print 'Encoder count is %s\nAB is %s %s' % (counts, stateA, stateB)
                # print 'Going counter-clockwise'
                
        stateA_old, stateB_old = stateA, stateB
                
    #returns the accumulated distance in pulses            
    def getPulses():
        return self.pulses
    
    #returns the accumulated distance in units of our choosing, 5 is a placeholder for wheel circumference in that unit
    def getDistance():
        return self.pulses/600.0 * 5           