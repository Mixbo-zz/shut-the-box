from abc import ABCMeta, abstractmethod

class Node:
	__metaclass__ = ABCMeta
	@abstractmethod
	def play(self,rolled):
		raise NotImplementedError()
	def printTree(self,pre=""):
		remaining = ""
		for left in self.tiles:
			remaining += str(left)+','
		remaining = remaining[:len(remaining)-1]
		ex = "|----|"
		if not self.branches:
			tot = 0
			for tile in self.tiles:
				tot+= tile
			print pre+ex+remaining+'->'+str(self.rolled)+"total: "+str(tot)
		else:
			print pre+ex+remaining+'->'+str(self.rolled)

		if not self.parent:
			extension = '\x20'*5
		elif self.parent.branches[-1] == self:
			extension = '\x20'*5
		else:
			extension = '|\x20'*4
		for branch in self.branches:
			branch.printTree(pre+extension)
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
