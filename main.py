import userInterface
import userInput
from inPlay import inPlay
from gameSetup import gameSetup
from scoreBoard import scoreBoard
from clues import clues

def main():
    score = scoreBoard()
    userInterface.firstStart()

    userName = userInput.inputName()
    maxNumber = userInput.inputMaxNumber()

    currentGame = gameSetup(userName, maxNumber)
    answer = currentGame.getAnswer()
    clue = clues(answer, maxNumber)

    runGame = inPlay(answer, maxNumber)
    playGame(runGame, score, userName, maxNumber, clue)

def playGame(runGame, score, userName, maxNumber, clue):
    userGuess = userInput.userGuess(maxNumber)
    if userGuess == 0:
        return
    else:
        if runGame.startGame(userGuess):
            userInterface.gameWon(userName, score.getScoreBoard())
        else:
            wrongGuess(runGame, score)
            showClue(clue, userGuess)
            return playGame(runGame, score, userName, maxNumber, clue)

def wrongGuess(runGame, score):
    if runGame.getPenalty():
        score.penalty()
        userInterface.penalty()
    else:
        score.addPoint()
    return

def showClue(clue, userGuess):
    return userInterface.printClue(clue.selectClue(userGuess))
        
main()