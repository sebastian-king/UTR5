import RPi.GPIO as GPIO
import sys, os, time

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../bin/bin-imports")
#import displays

def listen_for_stop():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

	#i=0;
	while True: # wait for the stop button to be pressed
		#i=i+1
		time.sleep(0.1)
		val = GPIO.input(23)
		#print str(i) + " " + str(val)
		if val == 1:
			break

	print "Stop pressed"
	#displays.show()
	import displays
	displays.showNumber(4)

	"""GPIO.cleanup()           # clean up GPIO on normal exit

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(26, GPIO.OUT)
	GPIO.output(26, GPIO.HIGH)"""
