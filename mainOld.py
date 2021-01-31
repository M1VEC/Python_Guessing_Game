import userInterface
import userInput
import inPlay

def main(): 
    userInterface.firstStart()
    userName = userInput.inputName()
    userInterface.helloUserMessage(userName)
    
    maximumNumber = userInput.inputMaxNumber()

    answer = inPlay.selectRandomNumber(maximumNumber)
    
    print(str(maximumNumber) + " " + str(answer))
    playGame(answer)
    
    return

def playGame(answer):
    while True:
        userGuess = userInput.userGuess()
        if userGuess == 0:
            break
        elif inPlay.checkGuess(userGuess, answer):
             print("congrats")
             break
        else:
            print("Incorrect guess, try again")   
    



main()
