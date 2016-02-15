import random

class Dice:
	def __init__(self):
		self.faces = 6
	def roll(self):
		rolled = random.randint(1,self.faces)
		return rolled
