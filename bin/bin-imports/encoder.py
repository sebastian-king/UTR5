# a class to allow us to get the states of the encoders, i.e accumulated distance & speed

import RPi.GPIO as GPIO # Allows use of pins on the Pi
import time

p = 0
p_elapsed = 0
sa = 0
sb = 0
sa_old = 0
sb_old = 0

#get time since epoch in milliseconds
def millis():
    return time.time() * 1000
   
def encoderHandlerA(void):
    sa_old = sa
    sa = GPIO.input(pins.motorEncoderA[1])
    p_elapsed += 1

def reset():
        p = 0
        p_elapsed = 0
        sa_old = 0
        sb_old = 0
     
def encoderHandlerB(void):
    sb_old = sb
    sb = GPIO.input(pins.motorEncoderB[1])
    p_elapsed += 1


def initCallbacks():
    GPIO.setup(pins.motorEncoderA[1], GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(pins.motorEncoderB[1], GPIO.IN, GPIO.PUD_UP)
    #set up interrupts
    io.add_event_detect(pins.motorEncoderA[1], io.BOTH, callback = encoderHandlerA)
    io.add_event_detect(pins.motorEncoderB[1], io.BOTH, callback = encoderHandlerB)   

def getP():
    return p

def updateP():
    currentState = [sa, sb]
    oldState = [sa_old, sb_old]
    direction = getDirection(currentState, oldState)
    if (direction):
        p += p_elapsed
    else:
        p -= p_elapsed
    p_elapsed = 0

def getDirection(newData = [], oldData = []):
        if oldData == [0, 0]:
            return (newData == [0, 1])
        elif oldData == [0, 1]:
            return (newData == [1, 1])
        elif oldData == [1, 1]:
            return (newData == [1, 0])
        elif oldData == [1, 0]:
            return (newData == [0, 0])
    

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
         
    
    
    def monitorA(self):
        stateA = GPIO.input(self.pinA)
        currentState = [stateA, self.stateB_old]
        oldState = [self.stateA_old, self.stateB_old]
        direction = self.getDirection(currentState, oldState)
        print 'currentState: %s' % currentState
        print 'oldState: %s' % oldState 
        print 'current current direction: %s' % direction
        if (direction):
            self.pulses += 1
        else:
            self.pulses -= 1
        self.stateA_old = stateA
        
    def monitorB(self):
        stateB = GPIO.input(self.pinB)
        currentState = [self.stateA_old, stateB]
        oldState = [self.stateA_old, self.stateB_old]
        if (self.getDirection(currentState, oldState)):
            self.pulses += 1
        else:
            self.pulses -= 1
        self.stateB_old = stateB
    
    #call this continuously in the main class to monitor the encoders and accumulate distance values
    def monitor(self):
    # Infinite loop to print out 1 or 0 depending on encoder input
        # Read the encoder input        
        stateA = GPIO.input(self.pinA)
        stateB = GPIO.input(self.pinB)
        currentState = [stateA, stateB]
        oldState = [self.stateA_old, self.stateB_old]
        
        if (self.getDirection(currentState, oldState)):
            self.pulses += 1
        else:
            self.pulses -= 1
            
            
        #find time passed
        #timePass = millis() - self.oldTime
        #if timePass > 1000:
         #   self.speed = self.pulses - self.oldPulses
          #  self.oldPulses = self.pulses
           # timePass = 0
            #self.oldTime = millis()
    
        # Print both states if something changes in either state and update the current state
        # Also casts the states as a string to remove ambiguity. Likely not needed
        #if str(stateA) != str(self.stateA_old):
        #if ((stateA, self.stateB_old) == (0,0)) or ((stateA, self.stateB_old) == (1,1)):
                 # IF clockwise rotation
            #self.pulses += 1
                # print 'Encoder count is %s\nAB is %s %s' % (counts, stateA, stateB)
                # print 'Going clockwise'
    
        #if str(stateB) != str(self.stateB_old):
        #if ((stateA, self.stateB_old) == (0,1)) or ((stateA, self.stateB_old) == (1,0)):
                # IF counter-clockwise rotation
            #self.pulses -= 1
                # print 'Encoder count is %s\nAB is %s %s' % (counts, stateA, stateB)
                # print 'Going counter-clockwise'
                
        self.stateA_old, self.stateB_old = stateA, stateB
                
                
    #True = clockwise
    def getDirection(self, newData = [], oldData = []):
        if oldData == [0, 0]:
            return (newData == [0, 1])
        elif oldData == [0, 1]:
            return (newData == [1, 1])
        elif oldData == [1, 1]:
            return (newData == [1, 0])
        elif oldData == [1, 0]:
            return (newData == [0, 0])
        
    #returns the accumulated distance in pulses            
    def getPulses(self):
        return self.pulses
    
    #returns the accumulated distance in units of mm
    def getDistance(self):
        return self.pulses/90.0 * 60 #60mm wheel circumference referenced from movement_wrapper   
    
    #returns the speed in mm/sec
    def getSpeed(self):
        return self.speed / 90.0 * 60 #60mm wheel circumference
        
    def reset(self):
        self.pulses = 0
        self.stateA_old = 0
        self.stateB_old = 0 
        
            
