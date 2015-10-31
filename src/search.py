from Queue import PriorityQueue
from node import *

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
	else:
		
#input is state to expand and hurist value
#returns a list of  expansions 
def aStar(node, hurist):
	
