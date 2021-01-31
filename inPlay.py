import userInput

class inPlay:
    
    def __init__(self, answer, maxNumber):
        self.answer = answer
        self.maxNumber = maxNumber
        
    def startGame(self):
        while True:
            userGuess = userInput.userGuess()
            if userGuess == 0:
                return
            elif inPlay.checkGuess(self, userGuess):
                return print("congrates")
    
    def checkGuess(self, userGuess):
        return userGuess == self.answer

    