import sys, getopt

sys.path.append('.')
import RTIMU
import os.path, time, math, numpy
from threading import Thread

pastReadings = []

def readData():
	while True:
		# x, y, z = imu.getFusionData()
		# print("%f %f %f" % (x,y,z))
		pastReadings.append(getReading())
		if len(pastReadings) > samples:
			pastReadings = pastReadings[-samples:]
		time.sleep(poll_interval*1.0/1000.0)

def getReading():
	data = imu.getIMUData()
	return data["fusionPose"][2]

def unusual():
	median = numpy.median(numpy.array(pastReadings))
	yaw = getReading()
	return yaw > median + threshold or yaw < median + threshold


SETTINGS_FILE = "RTIMULib"
threshold = 10
samples = 20

print("Using settings file " + SETTINGS_FILE + ".ini")
if not os.path.exists(SETTINGS_FILE + ".ini"):
	print("Settings file does not exist, will be created")

s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

print("IMU Name: " + imu.IMUName())

if (not imu.IMUInit()):
	print("IMU init failed")
	sys.exit(1)
else:
	print("IMU init succeeded")

imu.setSlerpPower(0.02)
imu.setGyroEnable(False)
imu.setAccelEnable(False)
imu.setCompassEnable(True)

poll_interval = imu.IMUGetPollInterval()
print("Recommended poll interval: %dmS, attempting to connect\n" % poll_interval)

while not imu.IMURead():
	# waiting...
	print "."

monitor = Thread(target = readData())
monitor.start()
