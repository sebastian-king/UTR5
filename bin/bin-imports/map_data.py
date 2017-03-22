#!/usr/bin/env python

#this file can contain all the data for the map
#current location and direction of bot
#grid of Map_Block, each Map_Block contains information about the location on the map
#Map_Block determines if that location has a tunnel, live wire, surface obstacle, cache
#getters and setters for all map data

class Map_Block():
	#all data fields true/False
	def __init__(self):
		self.has_tunnel = False
		self.has_live_wire = False
		self.has_obstacle = False
		self.has_cache = False
	def set_tunnel(self, object):
		self.has_tunnel = object
	def set_live_wire(self, object):
		self.has_live_wire = object
	def set_obstacle(self, object):
		self.has_obstacle = object
	def set_cache(self):
		self.has_cache = object

gridsize = 7
grid = [[Map_Block() for a in range(gridsize)] for b in range(gridsize)]

current_direction = 90      #starting direction. 0 to 360 0=+x=east, 90=+y=north,, etc

#location [x,y] 0-7. top left of feild is A0
loc = [0, 6]         #starting x, y

RIGHT, UP, LEFT, DOWN = 0, 1, 2, 3

def is_valid_loc(x, y):
	return (0 <= x < gridsize) and (0 <= y < gridsize )

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

#translate between A0 and [0, 0] notation
def x(str):
    return ord(str)-65
def y(int):
    return int-1
def xr(int):
    return unichr(int+65)
def yr(int):
    return int+1


def set_tunnel_here(object):
	grid[loc[0]][loc[1]].set_tunnel(object)
def has_tunnel_for_loc(x, y, object):
	return grid[x][y].has_tunnel

def set_live_wire_here(object):
	grid[loc[0]][loc[1]].set_live_wire(object)
def has_live_wire_for_loc(x, y, object):
	return grid[x][y].has_live_wire

def set_obstacle_here(object):
	grid[loc[0]][loc[1]].set_obstacle(object)
def set_obstacle_at(x, y, object):
	grid[x][y].set_obstacle(object)
def has_obstacle_for_loc(x, y, object):
	return grid[x][y].has_obstacle

def set_cache_here(object):
	grid[loc[0]][loc[1]].set_cache(object)
def has_cache_for_loc(x, y, object):
	return grid[x][y].has_cache



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
