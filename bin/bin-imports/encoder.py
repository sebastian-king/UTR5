# a class to allow us to get the states of the encoders, i.e accumulated distance & speed

import RPi.GPIO as GPIO # Allows use of pins on the Pi
import time

#get time since epoch in milliseconds
def millis():
    return time.time() * 1000

class encoder:
    
    def __init__(self, pinA, pinB):
        GPIO.setmode(GPIO.BCM)
        self.pinA = pinA
        self.pinB = pinB
        GPIO.setup(pinA, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(pinB, GPIO.IN, GPIO.PUD_UP)
        self.pulses = 0
        self.stateA_old = 0
        self.stateB_old = 0
        self.oldTime = millis()
        self.speed = 0 #this value is in pulses/second
        self.oldPulses = 0
    
    #call this continuously in the main class to monitor the encoders and accumulate distance values
    def monitor(self):
    # Infinite loop to print out 1 or 0 depending on encoder input
        # Read the encoder input        
        stateA = GPIO.input(self.pinA)
        stateB = GPIO.input(self.pinB)
        
        #find time passed
        timePass = millis() - oldTime
        if timePass > 1000:
            speed = self.pulses - self.oldPulses
            self.oldPulses = self.pulses
            timePass = 0
            oldTime = millis()
    
        # Print both states if something changes in either state and update the current state
        # Also casts the states as a string to remove ambiguity. Likely not needed
        if str(stateA) != str(self.stateA_old):
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
    
    #returns the accumulated distance in units of mm
    def getDistance(self):
        return self.pulses/600.0 * 60 #60mm wheel circumference referenced from movement_wrapper   
    
    #returns the speed in mm/sec
    def getSpeed(self):
        return self.speed / 600.0 * 60 #60mm wheel circumference
        
    def reset(self):
        self.pulses = 0
        self.stateA_old = 0
        self.stateB_old = 0 
        
            