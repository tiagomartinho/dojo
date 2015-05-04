import pytest

class Game:
	def __init__(self):
		self.totalScore = 0
	def roll(self,pins):
		self.totalScore += pins
	def score(self):
		return self.totalScore 
#TESTS
def test_empty_game():
	game = Game()
	for i in range(0,10):
		game.roll(0)
	assert (game.score() == 0) 