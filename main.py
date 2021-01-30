import userInterface
import userInput

def main(): 
    userInterface.firstStart()
    userName = userInput.inputName()
    userInterface.helloUserMessage(userName)
    
    maximumNumber = userInput.inputMaxNumber()
    print(maximumNumber)
    
    
    return




main()
