import pytest

class TennisGame:
	PLAYER_ONE = 0
	totalScoreP1=0
	def add_point(self,player):
		self.totalScoreP1+=15
	def score(self):
		return (self.totalScoreP1,0) 
#TESTS
def test_empty_game():
	game = TennisGame()
	assert (game.score()[0] == 0 and game.score()[1] == 0) 

def test_first_player_makes_first_point():
	game = TennisGame()
	game.add_point(TennisGame.PLAYER_ONE)
	assert (game.score()[0] == 15 and game.score()[1] == 0) 

def test_first_player_goes_to_match_point():
	game = TennisGame()
	game.add_point(TennisGame.PLAYER_ONE)
	game.add_point(TennisGame.PLAYER_ONE)
	game.add_point(TennisGame.PLAYER_ONE)
	assert (game.score()[0] == 40 and game.score()[1] == 0) 
