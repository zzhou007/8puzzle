import queue
import time
from node import *
from search import *

#the solution to 8 puzzle
solution = node([1, 2, 3, 4, 5, 6, 7, 8, 0])
#the places visited 

#search takes the initial state of the problem and the search type
#prints all expansions
#returns false if no sol
#returns true if sol found
def search(initial, searchType):
	#count is used incase the heuristic is the same
	count = 0
	#to hold visited nodes
	visited = []
	#create a priority queue of problem states
	i = heuristic(initial, searchType)
	initial.printP()
	nodes = queue.PriorityQueue()
	nodes.put((i, count, initial))
	while True:
		#no solution 
		if nodes.empty():
			return False
		#get lowest cost
		node = nodes.get()
		visited.append(node[2])
		#print node and value of node
		print("""The best state to expand with a 
			h(n) = {} 
			g(n) = {} is ...""".format( 
			heuristic(node[2], searchType),
			node[2].depth))
		node[2].printP()
		#solution
		if (node[2].state == solution.state):
			return True
		#checks if node is visited already if not add to que
		print("expanding this node ...")
		tmp = expand(node[2], searchType)
		j = 0
		for i in tmp[1]:
			if i not in visited:
				count += 1
				nodes.put((int(tmp[0][j]), count, i))
			j += 1
		


def main():
	#get 8 puzzle
	print("Enter an 8puzzle")
	r1 = input()
	r2 = input()
	r3 = input()
	#split input into seperate numbers
	r1 = r1.split()
	r2 = r2.split()
	r3 = r3.split()
	r1 = r1 + r2 + r3
	#make all into int
	r1 = list(map(int, r1))
	r1 = node(r1)
	print (""""Enter the type of search
		(0) Uniform cost
		(1) A* with misplaced tile heuristic
		(2) A* with manhattan distance
		""")
	s = input()
	if search(r1, int(s)):
		print("solution found")
	else:
		print("no solution")

main()
