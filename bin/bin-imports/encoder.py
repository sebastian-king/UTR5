# a class to allow us to get the states of the encoders, i.e accumulated distance & speed

import RPi.GPIO as GPIO # Allows use of pins on the Pi

class encoder:
    
    def __init__(self, pinA, pinB):
        GPIO.setmode(GPIO.BCM)
        self.pinA = pinA
        self.pinB = pinB
        GPIO.setup(pinA, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(pinB, GPIO.IN, GPIO.PUD_UP)
        self.pulses = 0
    
    #call this continuously in the main class to monitor the encoders and accumulate distance values
    def monitor(self):
    # Infinite loop to print out 1 or 0 depending on encoder input
        # Read the encoder input
        if 'stateA_old' not in locals():
            self.stateA_old = 0
        if 'stateB_old' not in locals():
            self.stateB_old = 0
        
        stateA = GPIO.input(self.pinA)
        stateB = GPIO.input(self.pinB)
    
        # Print both states if something changes in either state and update the current state
        # Also casts the states as a string to remove ambiguity. Likely not needed
        if str(stateA) != str(stateA_old):
            if ((stateA, self.stateB_old) == (0,0)) or ((stateA, self.stateB_old) == (1,1)):
                 # IF clockwise rotation
                self.pulses += 1
                # print 'Encoder count is %s\nAB is %s %s' % (counts, stateA, stateB)
                # print 'Going clockwise'
    
        if str(stateB) != str(self.stateB_old):
            if ((stateA, self.stateB_old) == (0,1)) or ((stateA, self.stateB_old) == (1,0)):
                # IF counter-clockwise rotation
                self.pulses -= 1
                # print 'Encoder count is %s\nAB is %s %s' % (counts, stateA, stateB)
                # print 'Going counter-clockwise'
                
        self.stateA_old, self.stateB_old = stateA, stateB
                
    #returns the accumulated distance in pulses            
    def getPulses(self):
        return self.pulses
    
    #returns the accumulated distance in units of our choosing, 5 is a placeholder for wheel circumference in that unit
    def getDistance(self):
        return self.pulses/600.0 * 5   
    
    def resetPulses(self):
        self.pulses = 0    
        
            