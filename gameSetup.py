import random
import userInput

class gameSetup:
    
    def __init__(self, userName):
        self.userName = userName
        self.setMaximum()
        self.setAnswer()
        
    def setAnswer(self):
        self.answer = random.randint(2, self.maxNumber)        
    
    def setMaximum(self):
        self.maxNumber = userInput.inputMaxNumber()           
    
    def getUserName(self):
        return self.userName
    
    def getAnswer(self):
        return self.answer
    
    def getmaxNumber(self):
        return self.maxNumber
        
        