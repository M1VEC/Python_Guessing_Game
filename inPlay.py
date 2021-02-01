class inPlay:
    
    def __init__(self, answer, maxNumber):
        self.answer = answer
        self.maxNumber = maxNumber
        self.listOfGuess = []
        self.isPenalty = None
        
    def checkGuess(self, userGuess):
            if userGuess == self.answer:
                return True
            else:
                self.verifyGuess(userGuess)
                return False

    def verifyGuess(self, userGuess):
        if userGuess in self.listOfGuess:
            self.isPenalty = True
        else:
            self.listOfGuess.append(userGuess)
            self.isPenalty = False    
    
    def getPenalty(self):
        return self.isPenalty