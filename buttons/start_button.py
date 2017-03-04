import RPi.GPIO as GPIO
import time

def listen_for_start():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)  
	GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12, GPIO.LOW)

	#i=0;
	while True:
		#i=i+1
		time.sleep(0.1)
		val = GPIO.input(22)
		#print str(i) + " " + str(val)
		if val == 0:
			break

	#print "GO"

	GPIO.cleanup()           # clean up GPIO on normal exit  

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12, GPIO.HIGH)
