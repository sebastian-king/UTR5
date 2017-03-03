import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(25,GPIO.OUT)

#GPIO.output(25,GPIO.LOW)
#time.sleep(5)
#GPIO.output(25,GPIO.HIGH)

for a in range(10):
	time.sleep(0.2)
	GPIO.cleanup()
	time.sleep(0.2)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(25,GPIO.OUT)
	GPIO.output(25,GPIO.LOW)

GPIO.cleanup()
