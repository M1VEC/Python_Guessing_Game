def firstStart():
    welcomeMessage()
    printInstructions()

def welcomeMessage():
    print("*********************************************************************************************")
    print("                             Random Number Guessing Game")
    print(" ")
    print("                                  ***Welcome User***")
    print(" ")
    print("              Your Goal is to guess the number randomly chosen by me")
    return

def printInstructions():
    print("\n            You will be asked to enter a maximum number I can choose from")
    print("         I will then select a number at random and you will have to try and guess it")
    print("             The quicker you guess the number the better your score will be")
    print("                    Enter a number in twice and you will be penalised")
    print("                                   Enter 0 to end game")
    print("*********************************************************************************************")
    
    return

def helloUserMessage(userName):
    print("Hello " + userName)
    return

def gameWon(userName, score):
    print("*********************************************************************************************")
    print("\n                                 Congratulationsv " + userName + "!")
    print("                                 You guessed correctly")
    print("                                     Your Score was")
    print("                                       " + str(score) + " points")
    print("*********************************************************************************************")
    return

def penalty():
    print("*********************************************************************************************")
    print("                          That number has been entered already!")
    print("                             2 Penalty Points added to score")
    print("                                       Try again!")
    print("*********************************************************************************************")
    
    
    