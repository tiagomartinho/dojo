import pytest

class Game:

	rolls = [0] * 20
	currentRoll = 0

	def roll(self,pins):
		self.rolls[self.currentRoll] = pins 
		self.currentRoll+=1

	def score(self):
		score = 0
		i = 0 
		for frame in range(0,10):
			if self.rolls[i] + self.rolls[i+1] == 10:
				score += 10 + self.rolls[i+2]
			else:
				score += self.rolls[i] + self.rolls[i+1]
			i+=2
		return score

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

