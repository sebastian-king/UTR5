#!/usr/bin/env python

#this file can contain all the data for the map
#current location and direction of bot
#grid of Map_Block, each Map_Block contains information about the location on the map
#Map_Block determines if that location has a tunnel, live wire, surface obstacle, cache
#getters and setters for all map data

class Map_Block():
	#all data fields true/False
	def __init__(self):
		self.visited = False
		self.has_tunnel = False
		self.has_live_wire = False
		self.has_obstacle = False
		self.has_cache = False
	def visit(self):
		self.visited = True
	def set_tunnel(self, bool):
		self.has_tunnel = bool
	def set_live_wire(self, bool):
		self.has_live_wire = bool
	def set_obstacle(self, bool):
		self.has_obstacle = bool
	def set_cache(self, bool):
		self.has_cache = bool

#storage for Map_Block data for the field
gridsize = 7
grid = [[Map_Block() for a in range(gridsize)] for b in range(gridsize)]

current_direction = 90      #starting direction (relative to field). 0 to 360 0=+x=east, 90=+y=north,, etc
RIGHT, UP, LEFT, DOWN = 0, 1, 2, 3		#directions relative to bot

#location [x,y] 0-7. top left of feild is A0
loc = [0, 6]         #starting x, y



#finds the adjacent coordinate to loc (x, y) in a direction
def coordsFor(x, y, direction):
	if direction == RIGHT:
		return [x + 1, y]
	elif direction == UP:
		return [x, y - 1]
	elif direction == LEFT:
		return [x - 1, y]
	elif direction == DOWN:
		return [x, y + 1]


#tests if a loc is within the grid
def is_valid_loc(x, y):
	return (0 <= x < gridsize) and (0 <= y < gridsize )


#getters and setters for location and direction that the bot is facing
def getX():
	return loc[0]
def getY():
	return loc[1]
def setX(newX):
	loc[0] = newX
def setY(newY):
	loc[0] = newY
def getDir():
	return current_direction
def setDir(dir):
	current_direction = dir


#getters and setters for all the data in the current map grid

def set_tunnel_here(object):
	grid[loc[0]][loc[1]].set_tunnel(object)
def has_tunnel_for_loc(x, y):
	return grid[x][y].has_tunnel

def set_live_wire_here(object):
	grid[loc[0]][loc[1]].set_live_wire(object)
def has_live_wire_for_loc(x, y):
	return grid[x][y].has_live_wire

def set_obstacle_here(object):
	grid[loc[0]][loc[1]].set_obstacle(object)
def set_obstacle_at(x, y, object):
	grid[x][y].set_obstacle(object)
def has_obstacle_for_loc(x, y):
	return grid[x][y].has_obstacle

def set_cache_here(object):
	grid[loc[0]][loc[1]].set_cache(object)
def has_cache_for_loc(x, y):
	return grid[x][y].has_cache

#tells you if a block has been visited
def has_been_explored(x, y):
	return grid[x][y].visited
def visit_here():
	grid[x][y].visit()







#translate between A0 and [0, 0] notation
def x(str):
    return ord(str)-65
def y(int):
    return int-1
def xr(int):
    return unichr(int+65)
def yr(int):
    return int+1
   
#for testing purposes
#Legend: C=Cache, O=(Live) Objective Tunnel, E=Dead Ends, B=Obstruction, X=Start and End point, H=bot
def print_map():
    print "---------------"
    print "  A B C D E F G"
    for y in range(0, gridsize):
		print y+1,
		for x in range(0, gridsize):
			if (x == getX() and y == getY()):
				print "H",
			elif (x == 0 and y == 6):
				print "X",
			elif has_cache_for_loc(x, y):
				print "C",
			elif has_obstacle_for_loc(x, y):
				print "B",
			elif has_live_wire_for_loc(x, y):
				print "O",
			elif has_tunnel_for_loc(x, y):
				print "E",
		print
