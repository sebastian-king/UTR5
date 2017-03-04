import RPi.GPIO as GPIO
import time
import wiringpi

GPIO.setmode(GPIO.BCM)

#wiringpi.wiringPiSetupGpio()
#wiringpi.pinMode(18, 2)
#wiringpi.pwmWrite(18, 0)

GPIO.setup(22,GPIO.OUT) # attached to pin 9
GPIO.setup(27,GPIO.OUT) # attached to pin 9
GPIO.setup(19,GPIO.OUT) # attached to pin 9
GPIO.setup(26,GPIO.OUT) # attacbed to pin 28

GPIO.setup(17,GPIO.OUT) # attacbed to pin 28
GPIO.setup(18,GPIO.OUT) # attacbed to pin 28

p1 = GPIO.PWM(17, 1024)
p2 = GPIO.PWM(18, 1024)

p1.start(40)
p2.start(40)

print "1"
#wiringpi.pwmWrite(18, 400)
GPIO.output(19,GPIO.LOW)
GPIO.output(26,GPIO.HIGH)
time.sleep(1)
print "2"
#wiringpi.pwmWrite(18, 512)
GPIO.output(19,GPIO.HIGH)
GPIO.output(26,GPIO.LOW)
time.sleep(1)
print "3"

GPIO.output(19,GPIO.LOW)
GPIO.output(26,GPIO.LOW)

#wiringpi.pwmWrite(18, 0)
time.sleep(2)

print "1"
GPIO.output(22,GPIO.LOW)
GPIO.output(27,GPIO.HIGH)
time.sleep(2)
print "2"
GPIO.output(22,GPIO.HIGH)
GPIO.output(27,GPIO.LOW)
time.sleep(2)
print "3"

GPIO.output(22,GPIO.LOW)
GPIO.output(27,GPIO.LOW)

#for a in range(10):
#	print "PWM: " + str(a*100)
#	#wiringpi.pwmWrite(18, a*100)
#	p.ChangeDutyCycle(a*10)
#	time.sleep(0.2)

p1.ChangeDutyCycle(0)
p2.ChangeDutyCycle(0)
#wiringpi.pwmWrite(18, 0)
GPIO.cleanup()
