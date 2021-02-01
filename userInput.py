from inPlay import inPlay

def inputName():
    return input("\nWhat is your name User: ")

def inputMaxNumber():
    return validateMaxNumberInput("\nWhat is my maximum number limit: ")
    
def userGuess(maxNumber):
    return validateGuess("\nEnter your guess: ", maxNumber)

def playAgain(userName):
    playAnotherGame =  input(userName + " do you want to play again? ( Y or N): ")
    if playAnotherGame == 'y' or playAnotherGame == 'Y':
        return True
    else:
        return False

def validateMaxNumberInput(prompt):
    while True:
        try:
            response = int(input(prompt))
            break
        except ValueError:
            print("Please only enter a valid number! ")
    return response

def validateGuess(prompt, maxNumber):
    while True:
        try:
            response = int(input(prompt))
            break
        except ValueError:
            print("Please only enter a valid number! ")

    if response < (maxNumber +1):
        return response
    else:
        print("Please enter a number less than " + str(maxNumber)) 
        return validateGuess(prompt, maxNumber)


