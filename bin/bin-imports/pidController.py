#This class will act as a general PID Controller for various applications, including speed control of wheels
#example usage:
#pid = pidController(.1, .01, .001)
#while True:
#    pid.update()
#    motors.setSpeed(pid.getOutput())

#TODO-may need to implement windup protection if it becomes an isssue

#returns time since epoch in milliseconds
import time

def millis():
    return time.time() * 1000

class pidController:
     
    def __init__(self, kP, kI, kD):
        
        self.Kp = kP
        self.Ki = kI 
        self.Kd = kD 
        self.Integral = 0.0
         
        self.sampleTime = 15 #in milliseconds, this will make the PID update its output at 50Hz default
        self.currentTime = millis()
        self.previousTime = self.currentTime
        
        self.setPoint = 0.0
        self.previousError = 0.0
        
        self.previousOutput = 0
        
        self.output = 0
    
    def update(self, currentMeasure):
        
        self.currentTime = millis()
        dt = self.currentTime - self.previousTime
        
        if(dt >= self.sampleTime): #only update at specific interval determined by the formula 1000/sampleTime (in Hz)
            
            error = self.setPoint - currentMeasure
            #deltaError = error - self.previousError
            
            P_value = self.Kp * error
            self.Integral += ((error + self.previousError)/2) * dt
            #derivative = 0.0
            #derivative = deltaError / dt
            
            self.previousTime = self.currentTime
            self.previousError = error
            
            I_value = self.Integral * self.Ki
            out = max(0, min((self.previousOutput + P_value + I_value),1000))#+ (derivative*self.Kd) //currently not using derivative
            print "pid out VALUE : %s" % (out)
            
            self.previousOutput = self.output
            self.output = out
              
        
    def getOutput(self):
        return self.output
         
    def setSetpoint(self, setPoint):
        self.previousOutput = setPoint      #initial value
        self.output = setPoint
        self.setPoint = setPoint
        self.clear()
    
    def setKp(self, kP):
        self.Kp = kP
    
    def setKd(self, kI):
        self.Ki = kI
        
    def setKi(self, kD):
        self.Kd = kD
        
    def setSampleTime(self, sampleTime):
        self.sampleTime = sampleTime
        
    def clear(self):
        self.Integral = 0
        self.previousError = 0
        self.currentTime = millis()
        self.previousTime = self.currentTime
         