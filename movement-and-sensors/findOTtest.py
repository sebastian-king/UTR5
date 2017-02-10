#!/usr/bin/env python
import sys
import time

pos_x, pos_y = 0, 6;
w, h = 7, 7
Map = [[0 for a in range(w)] for b in range(h)]

FACING = int(sys.argv[1]) # 1 = NORTH, 0 = EAST

def x(str):
        return ord(str)-65
def y(int):
        return int-1
def xr(int):
        return unichr(int+65)
def yr(int):
        return int+1
def get_pos():
        return pos_x, pos_y;
def set_pos(x, y):
        global pos_x, pos_y
        pos_x=x; pos_y=y;
def print_map():
        global w, h, Map
        print "---------------"
        print "  A B C D E F G"
        for y in range(0, h):
                print y+1,
                for x in range(0, w):
                        if x == pos_x and y == pos_y:
                                print "X",
                        else:
                                print Map[pos_x][pos_y],
                print
def is_infrastructure_below():
        global pos_x, pos_y
        if pos_x == 6 and pos_y == 2: # let's pretend the OT starts at (6,2)
                return True
        else:
                return False

set_pos(x("A"),y(7))
print_map()
print get_pos()

while not is_infrastructure_below():
        if FACING == 1:
                if pos_x == 0 and pos_y == 6:
                        set_pos(pos_x, pos_y-1) # MOVE NORTH
                elif pos_x == 0 and pos_y == 0:
                        set_pos(pos_x+1, pos_y)
                elif pos_x == 6 and pos_y == 0:
                        print "E: Was not able to locate OT"
                        sys.exit(0) # uh oh, since we were supposed to be facing the cache and have traversed half of the perimeter, something has gone wrong.
                elif pos_y == 0:
                        set_pos(pos_x+1, pos_y)
                elif pos_x == 0:
                        set_pos(pos_x, pos_y-1)
        else:
                if pos_x == 0 and pos_y == 6:
                        set_pos(pos_x+1, pos_y) # MOVE EAST
                elif pos_x == 6 and pos_y == 6:
                        set_pos(pos_x, pos_y-1)
                elif pos_x == 6 and pos_y == 0:
                        print "E: Was not able to locate OT"
                        sys.exit(1) # uh oh, since we were supposed to be facing the cache and have traversed half of the perimeter, something has gone wrong.
                elif pos_y == 6:
                        set_pos(pos_x+1, pos_y)
                elif pos_x == 6:
                        set_pos(pos_x, pos_y-1)
        print_map()
        time.sleep(1)
print "Infrastructure found at (" + str(xr(get_pos()[0])) + ", " + str(yr(get_pos()[1])) + ")"
