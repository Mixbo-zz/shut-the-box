#!/usr/bin/env python
from core.node import Node
from core.all_node import AllNode
from core.ets_node import ETSNode
from core.dice import Dice

class Game:
	def __init__(self):
		self.dices = []
		self.joueurs = []
		self.startGame()

		self.resEts = self.joueurs[0].bestResult()
		self.resAll = self.joueurs[1].bestResult()

		for joueur in self.joueurs:
			joueur.printTree()
			print '\n'

	def startGame(self):
		tiles = self.initBoard()
		self.joueurs.append(ETSNode(None, list(tiles),0))
		self.joueurs.append(AllNode(None, list(tiles),0))
		self.gameLoop()
	
	def gameLoop(self):
		done = False
		while not done:
			rolled = self.getRoll()
			doneEts = self.joueurs[0].play(rolled)
			doneAll = self.joueurs[1].play(rolled)
			done = doneEts and doneAll

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
	i = 0
	for x in range(0,1):
		game = Game()
		if game.resEts != game.resAll:
			i += 1
if __name__ == "__main__":
	main()
