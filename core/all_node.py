from core.node import Node
class AllNode(Node):
	def __init__(self, parent, tiles, depth):
		self.done = False
		self.tiles = tiles
		self.depth = depth
		self.branches = []
	def play(self,rolled):
		branchDone = True
		retval = True
		if not self.done:
			if not self.branches:
				self.rolled = rolled
				self.createBranches()
				retval = self.done
			else:
				for branch in self.branches:
					val = branch.play(rolled)
					branchDone = branchDone and val
				retval = branchDone
		return retval
	def createBranches(self):
		if not self.done:
			found = False
			for x in range(0,self.rolled/2+(self.rolled%2)):
				a = self.rolled-x
				if a in self.tiles:
					if self.rolled-a == 0:
						t = list(self.tiles)
						t.remove(self.rolled)
						self.branches.append(AllNode(self,t,self.depth+1))
						found = True
					elif self.rolled-a in self.tiles:
						t = list(self.tiles)
						t.remove(a)
						t.remove(self.rolled-a)
						self.branches.append(AllNode(self,t,self.depth+1))
						found = True
			self.done = not found
			return self.done
