import queue
from node import *
import copy

#find x and y value form an 8puzzle grid
def coord(i):
	y = 0
	x = 0
	if (i <= 3 and i >= 1):
		y = 1
	elif (i <= 6 and i >= 4):
		y = 2
	else:
		y = 3

	if (i % 3 == 1):
		x = 1
	elif (i % 3 == 2):
		x = 2
	else:
		x = 3
	return x, y

#used for manhattan distance
#input is node and location of misplaced tile
#returns misplaced distance for one piece
def manhattan(node, j):
	#missplaced, x and y axis of node and j
	a = coord(node.state[j])
	b = coord(j + 1)
	#print( "y1 =", a[1], "y2=", b[1], "x1 =", a[0], "x2 =", b[0])
	return abs(a[1] - b[1]) + abs(a[0] - b[0])

#input is current state and witch heuristic to use
#0 = uniforcost, 1 = misplaced tile, 2 = manhattan distance
def heuristic(node, i):
	if i ==  0:
		return 0
	elif i == 1:
		misplaced = 0
		for j in range(0, len(node.state)):
			if node.state[j] != j + 1:
				misplaced += 1
		return misplaced
	elif i == 2:
		misplaced = 0
		for j in range(0, len(node.state)):
			if node.state[j] != j + 1:
				misplaced += manhattan(node, j)
		return misplaced
	else:
		print("not 0, 1, or 2")
		exit()
		
#input is state to expand and hurist value
#returns a list of  expansions 
def expand(node, hurist):
	#list for expanded childern and their heuristics
	children = []
	heuristics = []
	#for all possible moves make deep copy and if you can move 
	#add to childern list and add heuristic + depth 
	nodeU = copy.deepcopy(node)
	if (nodeU.moveU()):
		nodeU.depth += 1
		children.append(nodeU)
		heuristics.append(heuristic(nodeU, hurist) + nodeU.depth)
	nodeD = copy.deepcopy(node)
	if (nodeD.moveD()):
		nodeD.depth += 1
		children.append(nodeD)
		heuristics.append(heuristic(nodeD, hurist) + nodeD.depth)
	nodeL = copy.deepcopy(node)
	if (nodeL.moveL()):
		nodeL.depth += 1
		children.append(nodeL)
		heuristics.append(heuristic(nodeL, hurist) + nodeL.depth)
	nodeR = copy.deepcopy(node)
	if (nodeR.moveR()):
		nodeR.depth += 1
		children.append(nodeR)
		heuristics.append(heuristic(nodeR, hurist) + nodeR.depth)
	return (heuristics , children)
