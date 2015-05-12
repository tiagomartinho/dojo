import pytest

class Score():
	love=0
	fifteen=15
	thirty=30
	forty=40
	deuce="Deuce"
	advantage="Advantage"
	won="Won"
	lost="Lost"
	def toString(self):
		return ""

class Zero(Score):
	def toString(self):
		return "Zero"

class Fifteen(Score):
	def toString(self):
		return "Fifteen"

class Thirty(Score):
	def toString(self):
		return "Thirty"

class Forty(Score):
	def toString(self):
		return "Forty"

class Won(Score):
	def toString(self):
		return "Won"

class TennisGame:
	PLAYER_ONE = 0
	totalScoreP1=Zero()
	def add_point(self,player):
		if(self.totalScoreP1.toString() == "Forty"):
			self.totalScoreP1 = Won()
		elif(self.totalScoreP1.toString() == "Thirty") :
			self.totalScoreP1 = Forty()
		elif(self.totalScoreP1.toString() == "Fifteen") :
			self.totalScoreP1 = Thirty()
		elif(self.totalScoreP1.toString() == "Zero") :
			self.totalScoreP1 = Fifteen()

	def score(self):
		return (self.totalScoreP1.toString(),0) 
#TESTS
def test_empty_game():
	game = TennisGame()
	assert (game.score()[0] == "Zero" and game.score()[1] == 0) 

def test_first_player_makes_first_point():
	game = TennisGame()
	game.add_point(TennisGame.PLAYER_ONE)
	assert (game.score()[0] == "Fifteen" and game.score()[1] == 0) 

def test_first_player_goes_to_match_point():
	game = TennisGame()
	for i in range(0,3):
		game.add_point(TennisGame.PLAYER_ONE)
	assert (game.score()[0] == "Forty" and game.score()[1] == 0)

def test_first_player_wins():
	game = TennisGame()
	for i in range(0,4):
		game.add_point(TennisGame.PLAYER_ONE)
	assert (game.score()[0] == "Won")
	#assert (gome.score()[1] == "lost")
