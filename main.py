from inPlay import inPlay
import userInterface
import gameSetup
import userInput
import scoreboard

def main():
    userInterface.firstStart()

    userName = userInput.inputName()
    maxNumber = userInput.inputMaxNumber()

    currentGame = gameSetup(userName, maxNumber)
    answer = currentGame.getAnswer()

    runGame = inPlay(answer, maxNumber)
    runGame.startGame()
  
    return
        
main()