import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pin = 16

GPIO.setup(pin, GPIO.IN)

for a in range(10):
	print GPIO.input(pin)
	time.sleep(0.2)
