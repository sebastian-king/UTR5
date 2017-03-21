
#encoder.py has encoder class that takes 2 pins for quadrature encoders
import encoder

motorEncoders = [0 for a in range(4)]

def initMotors(void):
    motorEncoders[0] = encoder(pins.leftFrontEncoderChA, leftFrontEncoderChB)
    motorEncoders[1] = encoder(pins.rightFrontEncoderChA, rightFrontEncoderChA)
    motorEncoders[2] = encoder(pins.leftRearEncoderChA, leftRearEncoderChB)
    motorEncoders[3] = encoder(pins.rightRearEncoderChA, rightRearEncoderChB)


def encoderHandler(void):
    movementEncoder.monitor();

#for any GPIO initialization
def initializeGPIO(void):    
    
    #set up encoder interrupt, call encoderHandler if either pins change
    GPIO.add_event_detect(encoderPinA, GPIO.BOTH, callback = encoderHandler)
    GPIO.add_event_detect(encoderPinB, GPIO.BOTH, callback = encoderHandler)

def run_all_motors(speed, pulses, dir1, dir2, dir3, dir4):
    number = 0