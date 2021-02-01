import userInterface
import userInput
from inPlay import inPlay
from gameSetup import gameSetup
from scoreBoard import scoreBoard

def main():
    score = scoreBoard()
    userInterface.firstStart()

    userName = userInput.inputName()
    maxNumber = userInput.inputMaxNumber()

    currentGame = gameSetup(userName, maxNumber)
    answer = currentGame.getAnswer()

    runGame = inPlay(answer, maxNumber)
    playGame(runGame, score, userName, maxNumber)


def playGame(runGame, score, userName, maxNumber):
    userGuess = userInput.userGuess(maxNumber)
    if userGuess == 0:
        return
    else:
        if runGame.startGame(userGuess):
            userInterface.gameWon(userName, score.getScoreBoard())
        else:
            wrongGuess(runGame, score)
            return playGame(runGame, score, userName, maxNumber)


def wrongGuess(runGame, score):
    if runGame.getPenalty():
        score.penalty()
        userInterface.penalty()
    else:
        score.addPoint()
    return
        
main()