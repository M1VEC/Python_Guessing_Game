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
        userGuess = userInput.userGuess(self.maxNumber)
        if userGuess == 0:
            return
        else:
            if self.gameLogic.startGame(userGuess):
                userInterface.gameWon(self.userName, self.score.getScoreBoard())
            else:
                self.wrongGuess()
                self.showClue(userGuess)
                return self.playGame()

    def wrongGuess(self):
        if self.gameLogic.getPenalty():
            self.score.penalty()
            userInterface.penalty()
        else:
            self.score.addPoint()
        return

    def showClue(self, userGuess):
        return userInterface.printClue(self.clue.selectClue(userGuess))
    