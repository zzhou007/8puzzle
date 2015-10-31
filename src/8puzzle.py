from node import *
from search import *
from Queue import PriorityQueue

#the solution to 8 puzzle
solution = node(1, 2, 3, 4, 5, 6, 7, 8, 0, 8)
#the places visited 
visited = []

#search takes the initial state of the problem and the search type
#prints all expansions
#returns false if no sol
#returns true if sol found
def search(initial, searchType):
	#create a priority queue of problem states
	nodes = PriorityQueue(initial, heuristic(initial, searchType))
	
	while True:
		#no solution 
		if nodes.empty():
			return False
		#get lowest cost
		node = nodes.get()
		visited.append(node)
		#print node and value of node
		print("""The best state to expand with a g(n) = {} 
			and h(n) = {} is ...""".format( 
			heuristic(node[1], searchType),
			node.depth)))
		node[1].printP()
		#solution
		if (node == solution):
			return True
		#checks if node is visited already if not add to que
		print("expanding this node ...")
		for possible in aStar(node[1], searchType):
			if possible[1] not in visited:
				nodes = nodes + possible
		


def main():
	search()
