import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(22,GPIO.OUT) # motor 1
GPIO.setup(27,GPIO.OUT)
GPIO.setup(19,GPIO.OUT) # motor 2
GPIO.setup(26,GPIO.OUT)

GPIO.setup(17,GPIO.OUT) # PWM for motor 1
GPIO.setup(18,GPIO.OUT) # PWM for motor 2

p1 = GPIO.PWM(17, 1024)
p2 = GPIO.PWM(18, 1024)

p1.start(40)
p2.start(40)

print "MOTOR 1 CW"
GPIO.output(19,GPIO.LOW)
GPIO.output(26,GPIO.HIGH)
time.sleep(1)
print "MOTOR 1 CCW"
GPIO.output(19,GPIO.HIGH)
GPIO.output(26,GPIO.LOW)
time.sleep(1)
print "MOTOR 1 STOP"
GPIO.output(19,GPIO.LOW)
GPIO.output(26,GPIO.LOW)
time.sleep(2)

print "MOTOR 2 CW"
GPIO.output(22,GPIO.LOW)
GPIO.output(27,GPIO.HIGH)
time.sleep(1)
print "MOTOR 2 CCW"
GPIO.output(22,GPIO.HIGH)
GPIO.output(27,GPIO.LOW)
time.sleep(1)
print "MOTOR 2 STOP"
GPIO.output(22,GPIO.LOW)
GPIO.output(27,GPIO.LOW)

p1.ChangeDutyCycle(0)
p2.ChangeDutyCycle(0)
GPIO.cleanup()
