import RPi.GPIO as GPIO  
import time

def listen_for_stop():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)  
	GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(26, GPIO.OUT)
	GPIO.output(26, GPIO.LOW)

	#i=0;
	while True:
		#i=i+1
		time.sleep(0.1)
		val = GPIO.input(5)
		#print str(i) + " " + str(val)
		if val == 0:
			break

	#print "GO"

	GPIO.cleanup()           # clean up GPIO on normal exit  

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(26, GPIO.OUT)
	GPIO.output(26, GPIO.HIGH)
