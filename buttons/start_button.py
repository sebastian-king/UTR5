import RPi.GPIO as GPIO
import sys, os, time

myfolder = os.path.dirname(os.path.realpath(__file__))
sys.path.append(myfolder + "/../bin/")
sys.path.append(myfolder + "/../bin/bin-imports")
import main
import pins

def listen_for_start():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	#GPIO.setup(12, GPIO.OUT)
	#GPIO.output(12, GPIO.LOW)

	# we should always have the bottom left lit yellow
	#GPIO.output(pins.matrix[8], GPIO.HIGH)
	#GPIO.output(pins.matrix[29], GPIO.HIGH)
	#GPIO.output(pins.matrix[31], GPIO.HIGH) # 31 = rowpins[6]

	#i=0;
	while True: # this waits for the start button to be pressed
		#i=i+1
		time.sleep(0.1)
		val = GPIO.input(18)
		#print str(i) + " " + str(val)
		if val == 0:
			break

	import displays
	print "GO"
#	main.main()

	"""GPIO.cleanup()           # clean up GPIO on normal exit

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12, GPIO.HIGH)"""
