import userInterface
import userInput
from gameSetup import gameSetup
from game import game

def main():
    userInterface.firstStart()
    userName = userInput.inputName()
    
    while True:
        currentGame = gameSetup(userName)
        runGame = game(currentGame)
        runGame.playGame()
        if not userInput.playAgain(userName):
            break
    

main()