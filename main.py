from inPlay import inPlay
import userInterface
from game import game
import userInput


def main():
    userInterface.firstStart()

    userName = userInput.inputName()
    maxNumber = userInput.inputMaxNumber()
    
    currentGame = game(userName, maxNumber)
    currentGame.getAnswer()
    startGame(answer = currentGame.getAnswer())

    print(currentGame.getUsername())
    print(currentGame.getAnswer()) 
    return

def startGame(answer):
     while True:
        userGuess = userInput.userGuess()
        if userGuess == 0:
            break
        elif inPlay.checkGuess(userGuess,answer ):
             print("congrats")
             break
        else:
            print("Incorrect guess, try again")   



main()