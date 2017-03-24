import sys, os

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
#	map_data.has_tunnel_for_loc(x, y), set_tunnel_here(True), set_live_wire_here(True), set_obstacle_here(True), set_cache_here(True)
#if turning the bot there is code for get direction

#END OF TUTORIAL

count = -1 # this will store the 7-segment count

def main():
	movement_wrapper.initMotors()
	find_live_tunnel_perimeter()
	mapOut()
	# and we are done, save and go back to starting location
	saveResults()
	movement_wrapper.strafe_to_block(0, 6)

def mapOut():
	lastDirection = map_data.UP # let's just start moving upwards
	if map_data.getY() is 0: # uh, if we're at the top, let's not
		lastDirection = map_data.DOWN
	exploring = True
	while exploring:
		if not wireBelowBlockIn(lastDirection): # try the preferred direction first
			for direction in range(0,3): # will loop through all directions
				if direction is not lastDirection: # we don't want to waste time
					if wireBelowBlockIn(direction):
						lastDirection = direction # the wire probably moves towards this direction
						pass # skip trying other directions
					else: # no wire :(
						# flip the direction
						if direction > 1:
							direction -= 2
						else:
							direction += 2
						# move back to the previous block
						movement_wrapper.strafe_one_block(direction)
		if map_data.getX() is 0 or map_data.getY() is 0:
			# we're at an edge, so we're back on the other side
			exploring = False

def wireBelowBlockIn(direction):
	x, y = map_data.coordsFor(map_data.getX(), map_data.getY(), direction)
	if map_data.has_not_been_explored(x, y):
		movement_wrapper.strafe_one_block(direction)
		return is_infrastructure_below()

pastReadings = []
wireEnds = []

def find_live_tunnel_perimeter():
	# we start at the bottom left, start exploring north
	moveDirection = map_data.UP
	exploring = True
	while exploring:
		movement_wrapper.strafe_one_block(moveDirection)
		pos_x = map_data.getX()
		pos_y = map_data.getY()
		if is_infrastructure_below():
			wireEnds.append([pos_x, pos_y])
			analyzeCache() # it's beneath us!
			exploring = False # we are done
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
	# is this different from the usual?
	if magnetometer.unsual():
		map_data.set_live_wire_here(True)
		return True
	return False

def analyzeCache():
	movement_wrapper.move(map_data.UP, movement_wrapper.blocklength/2) # position the arm
	movement_wrapper.removeCacheLid()
	count = vipro.analyze(takePicture()) # takePicture() should return a path to an image
	saveResults()
	movement_wrapper.move(map_data.DOWN, movement_wrapper.blocklength/2) # move back to where we were

def saveResults():
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
			else:
				f.write("."),
		f.write("\n")
	f.close()
