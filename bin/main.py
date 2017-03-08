
#make sure these imports are correct
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/bin-imports/")
import map_data
import movement_wrapper

#movement-wrapper.strafe_one_block(dir)
#strafe one block no turning. direction: 0=right, 1=fwd, 2=left, 3=back.
#sets its own new location, will not move if new location is off map

#map-data has location functions
#getX(), getY(), setX(x), setY(y), getDir(), setDir(dir)
#also has functions for storing information about each location

def main():
	find_live_tunnel_perimeter()

#TODO this algorithm should be going around the whole field
def find_live_tunnel_perimeter():
	if map-data.getDir() == 90 and map-data.getX() == 0 and map-data.getY() == 6:
		while not is_infrastructure_below():
			pos_x = map-data.getX()
			pos_y = map-data.getY()
			#this function is only for when bot facing north and in start position
		
                	if pos_x == 0 and pos_y == 6:
                        	movement-wrapper.strafe_one_block(1) # MOVE NORTH
                	elif pos_x == 0 and pos_y == 0:
                        	movement-wrapper.strafe_one_block(0)
                	elif pos_x == 6 and pos_y == 0:
                        	print "E: Was not able to locate OT"
                        	sys.exit(0) 
				# uh oh, since we were supposed to be facing the cache and have traversed half of the perimeter, something has gone wrong.
                	elif pos_y == 0:
                       		movement-wrapper.strafe_one_block(0)
                	elif pos_x == 0:
                        	movement-wrapper.strafe_one_block(1)
	else:
		#should not call if not facing north
		pass

def is_infrastructure_below():
	live_wire = false
        if (live_wire):	#need to import sensor functions for em field, true if live wire
                map-data.set_live_wire_here(true)
		map-data.set_cache_here(true)
		return true
        else:
                return false