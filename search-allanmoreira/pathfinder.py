#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import sys
import Queue
from common import *

# ==========================================
# PathFinder A Star
# ==========================================

class PathFinder_A_Star:

    def __init__(self):
        # TODO initialize your attributes here if needed
        pass

    # ------------------------------------------
    # Cost
    # ------------------------------------------

    def f(self, x1, y1, x2, y2):
        # TODO priority function to use with the PriorityQueue
        # You are free not to use this function
 	    # (it is not tested in the unit test)
        return None

    # ------------------------------------------
    # Heuristic
    # ------------------------------------------

    def h(self, x1, y1, x2, y2):
       # TODO heuristic function 
       # You are free not to use this function
       # (it is not graded in the unit test)
       return 0
    
    # ------------------------------------------
    # Solve
    # ------------------------------------------

    def solve(self, map):
        # TODO returns a list of movements (may be empty) 
		# if plan found, otherwise return None
        return None

    # ------------------------------------------
    # Get solvable
    # ------------------------------------------

    def get_solvable(self, map):
        # TODO returns True if plan found, 
        # otherwise returns False
        return False

    # ------------------------------------------
    # Get max tree height
    # ------------------------------------------

    def get_max_tree_height(self, map):
        # TODO returns max tree height if plan found, 
		# otherwise, returns None
        return None

    # ------------------------------------------
    # Get min moves
    # ------------------------------------------

    def get_min_moves(self, map):
        # TODO returns size of minimal plan to reach goal if plan found, 
		# otherwise returns None
        return None

# ------------------------------------------
# Main
# ------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) == 2:
        map_name = sys.argv[1]
    else:
        map_name = DEFAULT_MAP
    print "Loading map: " + map_name
    plan = PathFinder_A_Star().solve(read_map(map_name))
    if plan == None:
        print "No plan was found"
    else:
        print "Plan found:"
        for i, move in enumerate(plan):
            if move == MOVE_UP:
                print i, ": Move Up"
            elif move == MOVE_DOWN:
                print i, ": Move Down"
            elif move == MOVE_LEFT:
                print i, ": Move Left"
            elif move == MOVE_RIGHT:
                print i, ": Move Right"
            else:
                print i, ": Movement unknown = ", move