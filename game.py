import userInput
import userInterface
from inPlay import inPlay
from gameSetup import gameSetup
from scoreBoard import scoreBoard
from clues import clues

class game:
    
    def __init__(self, currentGame):
        self.currentGame = currentGame
        self.userName = self.currentGame.getUserName()
        self.maxNumber = self.currentGame.getmaxNumber()
        self.answer = self.currentGame.getAnswer()
        self.gameLogic = inPlay(self.answer, self.maxNumber)
        self.score = scoreBoard()
        self.clue = clues(self.answer, self.maxNumber)
    
    def playGame(self):
        self.userGuess = userInput.userGuess(self.maxNumber)
        if self.userGuess == 0:
            return
        else:
            if self.gameLogic.checkGuess(self.userGuess):
                userInterface.gameWon(self.userName, self.score.getScoreBoard())
            else:
                self.wrongGuess()
                return self.playGame()

    def wrongGuess(self):
        if self.gameLogic.getPenalty():
            self.score.penalty()
            return userInterface.penalty()
        else:
            self.score.addPoint()
        return self.showClue()

    def showClue(self):
        return userInterface.printClue(self.clue.selectClue(self.userGuess))
    