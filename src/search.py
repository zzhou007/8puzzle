from Queue import PriorityQueue
from node import *

#find x and y value form an 8puzzle grid
def distance(i):
	y = 0
	x = 0
	if (i <= 9 or i >= 7):
		y = 3
	elif (i <= 6 or i >= 4):
		y = 2
	else 
		y = 1
	if (i - 6 >= 0

#used for manhattan distance
#input is node and location of misplaced tile
#returns misplaced distance for one piece
def manhattan(node, j):
	#missplaced, x and y axis of node and j
	miss = 0
#input is current state and witch heuristic to use
#0 = uniforcost, 1 = misplaced tile, 2 = manhattan distance
def heuristic(node, i):
	if i ==  0:
		return 0
	elfi i == 1:
		misplaced = 0
		for j in range(0, len(node) - 2)
			if node[j] != j + 1:
				misplaced += 1
		return misplaced
	elfi i == 2:
		misplaced = 0
		for j in range(0, len(node) -2)
			if node[j] != j + 1:
				misplaced += manhattan(node, j)
		return misplaced
	else:
		print("not 0, 1, or 2")
		exit()
		
#input is state to expand and hurist value
#returns a list of  expansions 
def aStar(node, hurist):
	
