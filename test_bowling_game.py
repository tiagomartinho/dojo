import pytest

class Game:
	rolls = [0] * 20
	currentRoll = 0

	def roll(self,pins):
		self.rolls[self.currentRoll] = pins 
		self.currentRoll+=1

	def score(self):
		score = 0
		frameIndex = 0 
		for frame in range(0,10):
			if self.isStrike(frameIndex):
				score += 10 + self.strikeBonus(frameIndex) 
				frameIndex+=1
			else:
				if self.isSpare(frameIndex):
					score += 10 + self.rolls[frameIndex+2]
					frameIndex+=2
				else:
					score += self.rolls[frameIndex] + self.rolls[frameIndex+1]
					frameIndex+=2
		return score

	def isSpare(self,roll):
		return self.rolls[roll] + self.rolls[roll+1] == 10

	def strikeBonus(self,frameIndex):
		return self.rolls[frameIndex+1] + self.rolls[frameIndex+2]

	def isStrike(self,roll):
		return self.rolls[roll] == 10

#TESTS
def rollMany(game,n,pins):
	for i in range(0,n):
		game.roll(pins)

def rollSpare(game):
	game.roll(4)
	game.roll(6)

def rollStrike(game):
	game.roll(10)

def test_empty_game():
	game = Game()
	rollMany(game,20,0)
	assert (game.score() == 0) 

def test_one_pin_game():
	game = Game()
	rollMany(game,20,1)
	assert (game.score() == 20) 

def test_one_spare_game():
	game = Game()
	rollSpare(game)
	game.roll(3)
	rollMany(game,17,0)
	assert (game.score() == 16) 

def test_one_strike_game():
	game = Game()
	rollStrike(game)
	game.roll(3)
	game.roll(2)
	rollMany(game,16,0)
	assert (game.score() == 20) 
