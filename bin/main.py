myfolder = os.path.dirname(os.path.realpath(__file__))

#make sure these imports are correct
sys.path.append(myfolder + "/bin-imports/")
import map_data
import movement_wrapper
import displays
import vipro

import numpy

#TUTORIAL FOR USING MOVEMENT FUNCTIONS TO MAKE ALGORITHMS

#movement-wrapper.strafe_one_block(dir), strafe_to_block(x, y)
#strafe one block no turning. direction: 0=right, 1=fwd, 2=left, 3=back.
#sets its own new location, will not move if new location is not valid
#also have some code for turning the bot if needed

#map_data has location functions
#	map_data.getX(), getY()
#also has functions for storing information about each location
#	map_data.has_tunnel_for_loc(x, y), set_tunnel_here(), set_live_wire_here(), set_obstacle_here(), set_cache_here()
#if turning the bot there is code for get direction

#END OF TUTORIAL



def main():
	movement_wrapper.initMotors()
	find_live_tunnel_perimeter()
	# wireEnds now contains possible candidates for caches
	# check if we have time left, if we do, map out the rest of the map
	# and we are done

pastReadings = []
wireEnds = []

#TODO this algorithm should be going around the whole field
def find_live_tunnel_perimeter():
	# we start at the bottom left, start exploring north
	moveDirection = map_data.UP
	exploring = True
	while exploring:
		movement_wrapper.strafe_one_block(moveDirection)
		pos_x = map_data.getX()
		pos_y = map_data.getY()
		if is_infrastructure_below():
			map_data.set_live_wire_here(true)
			wireEnds.append([pos_x, pos_y])
			analyzeCache() # it's beneath us
		# check for obstacles above
		map_data.set_obstacle_at(pos_x-1, pos_y, IR_north.check())
		# do that for all other directions
		# [TODO]: don't move into an obstacle
		if pos_x == 0 and pos_y == 0: # top left
			moveDirection = map_data.RIGHT
		elif pos_x == 6 and pos_y == 0: # top right
			moveDirection = map_data.DOWN
		elif pos_x == 6 and pos_y == 6: # bottom right
			moveDirection = map_data.LEFT
		elif pos_x == 0 and pos_y == 6: # back at bottom left
			exploring = False

def is_infrastructure_below():
	# take a sample
	currentReading = magnetometer.x # Maybe a different axis
	pastReadings.append(currentReading)
	if len(pastReadings) > 20:
		pastReadings = pastReadings[-20:]
	# is this different from the usual?
	return currentReading > numpy.median(numpy.array(pastReadings))

def analyzeCache():
	arm.lower()
	#arm.raise() #need to rename this method, raise is a reserved word in python -carson
	count = vipro.analyze(takePicture()) # takePicture() should return a path to an image
	# save the count and map to be displayed later
	f = open(myfolder+"/finaldata", "w")
	f.write(str(count)+"\n")
	for y in range(0, map_data.gridsize):
		print y+1,
		for x in range(0, map_data.gridsize):
			if (x == 0 and y == 6):
				f.write("S"),
			elif map_data.has_live_wire_for_loc(x, y):
				f.write("L"),
			elif map_data.has_tunnel_for_loc(x, y):
				f.write("T"),
		f.write("\n")
	f.close()
