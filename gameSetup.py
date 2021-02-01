import random
import userInput

class gameSetup:
    
    def __init__(self, userName):
        self.userName = userName
        self.setMaximum()
        self.setAnswer()
        
    def setAnswer(self):
        self.answer = random.randint(1, self.maxNumber)        
    
    def setMaximum(self):
        self.maxNumber = userInput.inputMaxNumber()        
    
    # def generateRandomNumber(self):
    #     self.answer = random.randint(1, self.maxNumber)        
    
    def getUserName(self):
        return self.userName
    
    def getAnswer(self):
        return self.answer
    
    def getmaxNumber(self):
        return self.maxNumber
        
        