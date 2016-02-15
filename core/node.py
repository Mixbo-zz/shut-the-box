from abc import ABCMeta, abstractmethod

class Node:
	__metaclass__ = ABCMeta
	@abstractmethod
	def play(self,rolled):
		raise NotImplementedError()
	def printTree(self):
		remaining = ""
		for left in self.tiles:
			remaining += str(left)+','
		remaining = remaining[:len(remaining)-1]
		if not self.branches:
			tot = 0
			for tile in self.tiles:
				tot+= tile
			print ('-'*4+'|')*self.depth+'\x20'+remaining+'->'+str(self.rolled)+"total: "+str(tot)
		else:
			print ('-'*4+'|')*self.depth+'\x20'+remaining+'->'+str(self.rolled)

		for branch in self.branches:
			branch.printTree()
	def bestResult(self):
		if self.done:
			tot = 0
			for tile in self.tiles:
				tot+= tile
			return tot
		else:
			tot = 200
			for branch in self.branches:
				tmp = branch.bestResult()
				if tmp < tot:
					tot = tmp
			return tot
