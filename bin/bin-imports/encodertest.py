import RPi.GPIO as GPIO # Allows use of pins on the Pi
import time
import pins


#lets try only checking the rising edge of the step
#count every 2 phases as 1 pulse this time


pulses = 0

    
def initEncoderCallbacks():
    global pulses
    pulses = 0

    GPIO.setup(pins.motorEncoderA[1], GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(pins.motorEncoderB[1], GPIO.IN, GPIO.PUD_UP)
    #set up interrupts
    GPIO.add_event_detect(pins.motorEncoderA[1], GPIO.RISING, callback = encoderHandlerA)
    GPIO.add_event_detect(pins.motorEncoderB[1], GPIO.RISING, callback = encoderHandlerB)   
   

def reset():
    global pulses
    pulses = 0
    
def encoderHandlerA(void):
    global pulses
    b = GPIO.input(pins.motorEncoderB[1])
    if b == 1:
        pulses += 1
    else:
        pulses -= 1
     
def encoderHandlerB(void):
    global pulses  
    a = GPIO.input(pins.motorEncoderA[1])
    if a == 1:
        pulses -= 1
    else:
        pulses += 1

def getPulses():
    global p
    return p






















#another test based on old code

p = 0
p_elapsed = 0
sa = 0
sb = 0
sa_old = 0
sb_old = 0

    
def initCallbacksV2():
    global p
    global p_elapsed
    global sa
    global sb
    global sa_old
    global sb_old
    p = 0
    p_elapsed = 0
    sa = 0
    sb = 0
    sa_old = 0
    sb_old = 0

    GPIO.setup(pins.motorEncoderA[1], GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(pins.motorEncoderB[1], GPIO.IN, GPIO.PUD_UP)
    #set up interrupts
    GPIO.add_event_detect(pins.motorEncoderA[1], GPIO.BOTH, callback = encoderHandlerA)
    GPIO.add_event_detect(pins.motorEncoderB[1], GPIO.BOTH, callback = encoderHandlerB)   
   

def resetV2():
    global p
    global p_elapsed
    global sa
    global sb
    global sa_old
    global sb_old
    p = 0
    p_elapsed = 0
    sa_old = 0
    sb_old = 0

def encoderHandlerA(void):
    global p_elapsed
    global sa
    global sa_old
    sa_old = sa
    sa = GPIO.input(pins.motorEncoderA[1])
    p_elapsed += 1
     
def encoderHandlerB(void):
    global p_elapsed
    global sb
    global sb_old
    sb_old = sb
    sb = GPIO.input(pins.motorEncoderB[1])
    p_elapsed += 1


def getP():
    global p
    return p

def updateP():
    global p
    global p_elapsed
    global sa
    global sb
    global sa_old
    global sb_old
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
    

