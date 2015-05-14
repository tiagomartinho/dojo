import pytest

class Game:
	rolls = [0] * 21
	currentRoll = 0
	def __init__(self):
		self.totalScore = 0
	def roll(self,pins):
		self.totalScore += pins
		self.rolls[self.currentRoll] = pins 
		self.currentRoll+=1
	def score(self):
		score = 0
		for i in range(0,len(self.rolls)):
			score += self.rolls[i]
		return self.totalScore 
#TESTS
def test_empty_game():
	game = Game()
	for i in range(0,20):
		game.roll(0)
	assert (game.score() == 0) 

def test_one_pin_game():
	game = Game()
	for i in range(0,20):
		game.roll(1)
	assert (game.score() == 20) 

def test_one_spare_game():
	game = Game()
	game.roll(4)
	game.roll(6)
	game.roll(3)
	for i in range(0,17):
		game.roll(0)
	assert (game.score() == 16) 

