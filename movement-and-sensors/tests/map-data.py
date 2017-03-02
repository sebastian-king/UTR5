#!/usr/bin/env python

#this file can contain all the data for the map
#current location and direction of bot
#grid of Map_Block, each Map_Block contains information about the location on the map
#Map_Block determines if that location has a tunnel, live wire, surface obstacle, cache
#getters and setters for all map data

gridsize = 7
grid = [[Map_Block() for j in range(gridsize)] for i in range(gridsize)]


current_direction = 90      #starting direction. 0 to 360 0=+x, 90=+y,, etc
#location [x,y] 0-7. [0,0] is bottom left (we can change this)
loc = [1, 0]         #starting x, y


def is_valid_loc(x, y):
	return (0 <= x <= gridsize) and (0 <= y <= gridsize )

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
def has_obstacle_for_loc(x, y, object):
	return grid[x][y].has_obstacle

def set_cache_here(object):
	grid[loc[0]][loc[1]].set_cache(object)
def has_cache_for_loc(x, y, object):
	return grid[x][y].has_cache


class Map_Block():
	#all data fields true/false
	def __init__(self):
		self.has_tunnel = false
		self.has_live_wire = false
		self.has_obstacle = false
		self.has_cache = false
	def set_tunnel(self, object):
		self.has_tunnel = object
	def set_live_wire(self, object):
		self.has_live_wire = object
	def set_obstacle(self, object):
		self.has_obstacle = object
	def set_cache(self):
		self.has_cache = object