import userInterface
from game import game
import userInput


def mainOPP():
    userInterface.firstStart()

    userName = userInput.inputName()
    currentGame = game(userName, '0')

    currentGame.setAnswer(15)

    print(currentGame.getUsername())
    print(currentGame.getAnswer()) 
    return

mainOPP()