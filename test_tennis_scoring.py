import pytest

class Score():
 def toString(self):
  pass
 def nextState(self,otherPlayerScore):
  return self
 def updateState(self,otherPlayerScore):
  if otherPlayerScore.toString() == Won().toString():
   return Lost()
  else:
   return self

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
  if otherPlayerScore.toString() == Forty().toString():
   return Deuce()
  else:
   return Forty()

class Forty(Score):
 def toString(self):
  return "Forty"
 def nextState(self,otherPlayerScore):
  if otherPlayerScore.toString() != Deuce().toString():
   return Won()
 def updateState(self,otherPlayerScore):
  if otherPlayerScore.toString() == Deuce().toString():
   return Deuce()

class Won(Score):
 def toString(self):
  return "Won"

class Deuce(Score):
 def toString(self):
  return "Deuce"
 def nextState(self,otherPlayerScore):
  if otherPlayerScore.toString() != Advantage().toString():
   return Advantage()
  else:
   return self

class Advantage(Score):
 def toString(self):
  return "Advantage"
 def nextState(self,otherPlayerScore):
  return Won()
 def updateState(self,otherPlayerScore):
  return Deuce()

class Lost(Score):
 def toString(self):
  return "Lost"

class TennisGame:
 PLAYER_ONE=0
 PLAYER_TWO=1
 def __init__(self):
  self.totalScore = [Zero(),Zero()]

 def add_point(self, player):
  other=(player+1)%2
  self.totalScore[player] = self.totalScore[player].nextState(self.totalScore[other])
  self.totalScore[other] = self.totalScore[other].updateState(self.totalScore[player])

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

def test_first_player_makes_second_point():
    game = TennisGame()
    for i in range(0,2):
     game.add_point(TennisGame.PLAYER_ONE)
    assert (game.score()[0] == "Thirty" and game.score()[1] == "Zero")

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

def test_game_goes_to_deuce():
    game = TennisGame()
    for i in range(0,3):
        game.add_point(TennisGame.PLAYER_ONE)
        game.add_point(TennisGame.PLAYER_TWO)
    assert (game.score()[0] == "Deuce" and game.score()[1] == "Deuce")

def test_game_goes_to_deuce_p1_gets_advance():
    game = TennisGame()
    for i in range(0,3):
        game.add_point(TennisGame.PLAYER_ONE)
        game.add_point(TennisGame.PLAYER_TWO)
    game.add_point(TennisGame.PLAYER_ONE)
    assert (game.score()[0] == "Advantage" and game.score()[1] == "Deuce")

def test_game_goes_to_deuce_p1_gets_advance_and_wins():
    game = TennisGame()
    for i in range(0,3):
        game.add_point(TennisGame.PLAYER_ONE)
        game.add_point(TennisGame.PLAYER_TWO)
    game.add_point(TennisGame.PLAYER_ONE)
    game.add_point(TennisGame.PLAYER_ONE)
    assert (game.score()[0] == "Won" and game.score()[1] == "Lost")

def test_game_goes_to_deuce_p1_gets_advance_and_loses_it():
    game = TennisGame()
    for i in range(0,3):
        game.add_point(TennisGame.PLAYER_ONE)
        game.add_point(TennisGame.PLAYER_TWO)
    game.add_point(TennisGame.PLAYER_ONE)
    assert (game.score()[0] == "Advantage" and game.score()[1] == "Deuce")
    game.add_point(TennisGame.PLAYER_TWO)
    assert (game.score()[0] == "Deuce" and game.score()[1] == "Deuce")