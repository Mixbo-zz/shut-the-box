#!/usr/bin/env python
from core.node import Node
from core.dice import Dice

class Game:
	def __init__(self):
		self.dices = []
		self.startGame()
		self.root.printTree()
		self.result = self.root.bestResult()
	def startGame(self):
		self.root = Node(None, self.initBoard(),0)
		self.gameLoop()
	def gameLoop(self):
		done = False
		while not done:
			done = self.root.play(self.getRoll())

	def getRoll(self):
		total = 0
		for dice in self.dices:
			total += dice.roll()
		return total

	def initBoard(self):
		for x in range(0,2):
			self.dices.append(Dice())
		tiles = []
		for x in range(1,13):
			tiles.append(x)
		return tiles


def main():
	result = 1
	i = 0
	total = 0
	while result != 0: 
		game = Game()
		result = game.result
		total += result
		i +=1
	print "Nombre de parties avant une parfaite: "+str(i)
	print "Moyenne des parties jouees (meilleur resultat): "+str(total/i)
if __name__ == "__main__":
	main()
