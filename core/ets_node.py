from core.node import Node
class ETSNode(Node):
	def __init__(self, parent, tiles, depth):
		self.parent = parent
		self.done = False
		self.tiles = tiles
		self.depth = depth
		self.branches = []

	def play(self,rolled):
		found = False
		retval = True
		if not self.done:
			if not self.branches:
				self.rolled = rolled
				for x in range(0,rolled/2+(rolled%2)):
					if rolled-x in self.tiles:
						if x == 0:
							t = list(self.tiles)
							t.remove(rolled)
							self.branches.append(ETSNode(self,t,self.depth+1))
							found = True
							break
						elif x in self.tiles:
							t = list(self.tiles)
							t.remove(rolled-x)
							t.remove(x)
							self.branches.append(ETSNode(self,t,self.depth+1))
							found = True
							break
				self.done = not found
				retval = self.done
			else:
				retval = self.branches[0].play(rolled)
		return retval
