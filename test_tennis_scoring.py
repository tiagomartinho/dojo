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

class Lost(Score):
	def toString(self):
		return "Lost"

class TennisGame:
	PLAYER_ONE=0
	PLAYER_TWO=1
	totalScore = [Zero(),Zero()]
	def add_point(self,player):
		if(self.totalScore[player].toString() == "Forty"):
			self.totalScore[player] = Won()
			self.totalScore[(player+1)%2] = Lost()
		elif(self.totalScore[player].toString() == "Thirty") :
			self.totalScore[player] = Forty()
		elif(self.totalScore[player].toString() == "Fifteen") :
			self.totalScore[player] = Thirty()
		elif(self.totalScore[player].toString() == "Zero") :
			self.totalScore[player] = Fifteen()

	def score(self):
		return (self.totalScore[self.PLAYER_ONE].toString(),self.totalScore[self.PLAYER_TWO].toString()) 
#TESTS
def test_empty_game():
	game = TennisGame()
	assert (game.score()[0] == "Zero" and game.score()[1] == "Zero") 

def test_first_player_makes_first_point():
	game = TennisGame()
	game.add_point(TennisGame.PLAYER_ONE)
	assert (game.score()[0] == "Fifteen" and game.score()[1] == "Zero") 

def test_first_player_goes_to_match_point():
	game = TennisGame()
	for i in range(0,2):
		game.add_point(TennisGame.PLAYER_ONE)
	assert (game.score()[0] == "Forty" and game.score()[1] == "Zero")

def test_first_player_wins():
	game = TennisGame()
	for i in range(0,3):
		game.add_point(TennisGame.PLAYER_ONE)
	assert (game.score()[0] == "Won" and game.score()[1] == "Lost")
