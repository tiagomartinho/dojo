import pytest

class TennisGame:
	def score(self):
		return (0,0) 
#TESTS
def test_empty_game():
	game = TennisGame()
	assert (game.score()[0] == 0 and game.score()[1] == 0) 
