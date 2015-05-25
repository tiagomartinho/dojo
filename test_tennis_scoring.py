import pytest

class Score():
	def toString(self):
		pass
	def nextState(self,otherPlayerScore):
		pass

class Zero(Score):
	def toString(self):
		return "Zero"
	def nextState(self,otherPlayerScore):
		return Fifteen()

class Fifteen(Score):
	def toString(self):
		return "Fifteen"
	def nextState(self,otherPlayerScore):
		return Thirty()

class Thirty(Score):
	def toString(self):
		return "Thirty"
	def nextState(self,otherPlayerScore):
		return Forty()

class Forty(Score):
	def toString(self):
		return "Forty"
	def nextState(self,otherPlayerScore):
		return self

class Won(Score):
	def toString(self):
		return "Won"
	def nextState(self,otherPlayerScore):
		return self

class Lost(Score):
	def toString(self):
		return "Lost"
	def nextState(self,otherPlayerScore):
		return self

class TennisGame:
    PLAYER_ONE=0
    PLAYER_TWO=1
    def __init__(self):
        self.totalScore = [Zero(),Zero()]

    def add_point(self, player):
        if(self.totalScore[player].toString() == "Forty"):
            self.totalScore[player] = Won()
            self.totalScore[(player+1)%2] = Lost()
        else:
            self.totalScore[player] = self.totalScore[player].nextState(0)

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
	for i in range(0,3):
		game.add_point(TennisGame.PLAYER_ONE)
	assert (game.score()[0] == "Forty" and game.score()[1] == "Zero")

def test_first_player_wins():
	game = TennisGame()
	for i in range(0,4):
		game.add_point(TennisGame.PLAYER_ONE)
	assert (game.score()[0] == "Won" and game.score()[1] == "Lost")

def test_second_player_wins():
    game = TennisGame()
    for i in range(0,4):
        game.add_point(TennisGame.PLAYER_TWO)
    assert (game.score()[0] == "Lost" and game.score()[1] == "Won")
