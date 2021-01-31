def firstStart():
    welcomeMessage()
    printInstructions()

def welcomeMessage():
    print("\n                            Random Number Guessing Game")
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
    return

def helloUserMessage(userName):
    print("Hello " + userName)
