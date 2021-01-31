from inPlay import inPlay
import userInterface
from gameSetup import gameSetup
import userInput
from scoreBoard import scoreBoard

def main():
    score = scoreBoard()
    userInterface.firstStart()

    userName = userInput.inputName()
    maxNumber = userInput.inputMaxNumber()

    currentGame = gameSetup(userName, maxNumber)
    answer = currentGame.getAnswer()

    runGame = inPlay(answer, maxNumber)
    playGame(runGame, score)

    total = score.getScoreBoard()
    print(total)


def playGame(runGame, score):
    userGuess = userInput.userGuess()
    if userGuess == 0:
        return
    else:
        if runGame.startGame(userGuess):
            gameWon(score)
        else:
            wrongGuess(runGame, score)
            return playGame(runGame, score)


def wrongGuess(runGame, score):
    if runGame.getPenalty():
        score.penalty()
        userInterface.penalty()
    else:
        score.addPoint()
    return


def gameWon(score):
    print("game won")

        
main()