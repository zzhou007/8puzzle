class node:
	#makes node input = puzzle state, location of blank, and depth in tree
	def __init__(self, tl, tm, tr, ml, mm, mr, bl, bm, br):
		self.state = [tl, tm, tr, ml, mm, mr, bl, bm, br]
		for i in self.state:
			if (self.state[i] == 0):
				self.blankP = i
		self.depth = 0
	#moves the blank space 
	#returns true if can be moved returns false if cannot be moved 
	def moveL(self):
		if self.blankP - 1 < 0:
			return False
		self.state[self.blankP] = self.state[self.blankP - 1]
		self.state[self.blankP - 1] = 0
		self.blankP -= 1
		return True
	def moveR(self):
		if self.blankP + 1 > 8:
			return False
		self.state[self.blankP]  = self.state[self.blankP + 1]
		self.state[self.blankP + 1] = 0
		self.blankP += 1	
		return True
	def moveU(self):
		if self.blankP - 3 < 0:
			return False
		self.state[self.blankP] = self.state[self.blankP - 3]
		self.state[self.blankP - 3] = 0
		self.blankP -= 3
		return True
	def moveD(self):
		if self.blankP + 3 > 8:
			return False
		self.state[self.blankP] = self.state[self.blankP + 3]
		self.state[self.blankP + 3] = 0
		self.blankP += 3
		return True
	#prints the state of the puzzle
	def printP(self):
		i = 0
		while i < 9:
			if (i != self.blankP):
				print(self.state[i], end = " ")
			else:
				print(" ", end = " ")
			if (i == 2 or i == 5 or i == 8):
				print()
			i += 1
