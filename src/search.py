import queue
from node import *

#find x and y value form an 8puzzle grid
def coord(i):
	y = 0
	x = 0
	if (i <= 9 or i >= 7):
		y = 3
	elif (i <= 6 or i >= 4):
		y = 2
	else:
		y = 1

	if (i % 3 == 1):
		x = 1
	elif (i % 3 == 2):
		x = 2
	else:
		x = 0
	return x, y

#used for manhattan distance
#input is node and location of misplaced tile
#returns misplaced distance for one piece
def manhattan(node, j):
	#missplaced, x and y axis of node and j
	a = coord(node)
	b = coord(j + 1)
	return abs(a[1] - b[1]) + abs(a[0] - b[0])

#input is current state and witch heuristic to use
#0 = uniforcost, 1 = misplaced tile, 2 = manhattan distance
def heuristic(node, i):
	if i ==  0:
		return 0
	elif i == 1:
		misplaced = 0
		for j in range(0, len(node) - 1):
			if node[j] != j + 1:
				misplaced += 1
		return misplaced
	elif i == 2:
		misplaced = 0
		for j in range(0, len(node) - 1):
			if node[j] != j + 1:
				misplaced += manhattan(node, j)
		return misplaced
	else:
		print("not 0, 1, or 2")
		exit()
		
#input is state to expand and hurist value
#returns a list of  expansions 
def expand(node, hurist):
	depth = node.depth + 1
	child = node
	if (node.moveU()):
		child = node
		child.depth = depth
	if (node.moveD()):
		child = node
		child.depth = depth
	if (node.moveL()):
		child = node
		child.depth = depth
	if (node.moveR()):
		child = node
		child.depth = depth
	h = heuristic(node, hurist)
	return (h + depth, child)
