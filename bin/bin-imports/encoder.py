# a class to allow us to get the states of the encoders, i.e accumulated distance & speed


# We will interrupt when A goes from 0->1 (False->True) and then check the state
#     of B. If B is high, we are going clockwise, otherwise, we are going
#     counterclockwise.



import RPi.GPIO as GPIO # Allows use of pins on the Pi
import time
import pins

speedUpdateMs = 20

def millis():
    return time.time() * 1000

class encoder:
    
    def __init__(self, pinA, pinB):
        GPIO.setmode(GPIO.BCM)
        self.pinA = pinA
        self.pinB = pinB        
        self.pulses = 0
        
        self.speed = 0
        self.oldTime = millis()
        self.oldPulses = 0
    
        GPIO.setup(pinA, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(pinB, GPIO.IN, GPIO.PUD_UP)
        #set up interrupts
        GPIO.add_event_detect(self.pinA, GPIO.RISING, callback = self.encoderHandlerA)
        GPIO.add_event_detect(self.pinB, GPIO.RISING, callback = self.encoderHandlerB)   

    def encoderHandlerA(self, void):
        b = GPIO.input(self.pinB)
        if b == 1:
            self.pulses += .5
        else:
            self.pulses -= .5
        if(millis() - self.oldTime >= speedUpdateMs):
            self.speed = self.pulses-self.oldPulses
            self.oldPulses = self.pulses
            self.oldTime = millis()
         
    def encoderHandlerB(self, void):
        a = GPIO.input(self.pinA)
        if a == 1:
            self.pulses -= .5
        else:
            self.pulses += .5
        if(millis() - self.oldTime >= speedUpdateMs):
            self.speed = self.pulses-self.oldPulses
            self.oldPulses = self.pulses
            self.oldTime = millis()
 
    #returns the accumulated distance in pulses            
    def getPulses(self):
        return self.pulses
   
    def reset(self):
        self.pulses = 0
 
    #returns the accumulated distance in units of mm
    def getDistance(self):
        return self.pulses/90.0 * 60 #60mm wheel circumference referenced from movement_wrapper   
    
    #TODO
    #returns the speed in RPM
    def getSpeed(self):
        return self.speed * (1000.0/speedUpdateMs) * 60.0 / 90.0  #pulses traveled during speedUpdateMs * number of updates per second
                                                            # * 60 seconds in a minute / 90 pulses per rotation = RPM
        



#OLD CODE FROM ENCODER
#we might want to use some of the speed code for multiple motors


#get time since epoch in milliseconds
#def millis():
#    return time.time() * 1000


#===========================================================================
# 
# #call this continuously in the main class to monitor the encoders and accumulate distance values
# def monitor(self):
# # Infinite loop to print out 1 or 0 depending on encoder input
#     # Read the encoder input        
#     stateA = GPIO.input(self.pinA)
#     stateB = GPIO.input(self.pinB)
#     currentState = [stateA, stateB]
#     oldState = [self.stateA_old, self.stateB_old]
#     
#     if (self.getDirection(currentState, oldState)):
#         self.pulses += 1
#     else:
#         self.pulses -= 1
#         
#         
#     find time passed
#     timePass = millis() - self.oldTime
#     if timePass > 1000:
#         self.speed = self.pulses - self.oldPulses
#         self.oldPulses = self.pulses
#         timePass = 0
#         self.oldTime = millis()
# 
#     # Print both states if something changes in either state and update the current state
#     # Also casts the states as a string to remove ambiguity. Likely not needed
#     #if str(stateA) != str(self.stateA_old):
#     #if ((stateA, self.stateB_old) == (0,0)) or ((stateA, self.stateB_old) == (1,1)):
#              # IF clockwise rotation
#         #self.pulses += 1
#             # print 'Encoder count is %s\nAB is %s %s' % (counts, stateA, stateB)
#             # print 'Going clockwise'
# 
#     #if str(stateB) != str(self.stateB_old):
#     #if ((stateA, self.stateB_old) == (0,1)) or ((stateA, self.stateB_old) == (1,0)):
#             # IF counter-clockwise rotation
#         #self.pulses -= 1
#             # print 'Encoder count is %s\nAB is %s %s' % (counts, stateA, stateB)
#             # print 'Going counter-clockwise'
#             
#     self.stateA_old, self.stateB_old = stateA, stateB
#===========================================================================
 
        
