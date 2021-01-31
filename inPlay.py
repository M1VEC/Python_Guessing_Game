class inPlay:
    
    def __init__(self, answer, maxNumber):
        self.answer = answer
        self.maxNumber = maxNumber
        self.listOfGuess = []
        self.isPenalty = None
        
    def startGame(self, userGuess):
            if self.checkGuess(userGuess):
                return True
            else:
                self.verifyNumber(userGuess)
                return False
                
    def checkGuess(self, userGuess):
        return userGuess == self.answer

    def verifyNumber(self, userGuess):
        if userGuess in self.listOfGuess:
            self.isPenalty = True
        else:
            self.listOfGuess.append(userGuess)
            self.isPenalty = False    
    
    def getPenalty(self):
        return self.isPenalty