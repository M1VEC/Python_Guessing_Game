import random

def selectRandomNumber(maxNumber):
    return random.randint(1,maxNumber)

def checkGuess(userNumber, answer):
    return userNumber == answer
    