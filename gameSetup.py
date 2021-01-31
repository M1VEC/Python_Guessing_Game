import random

class gameSetup:
    
    def __init__(self, userName, maxNumber):
        self.userName = userName
        self.maxNumber = maxNumber
        self.setAnswer = self.setAnswer()
        
    def setUserName(self, name):
        self.userName = name
        
    def setAnswer(self):
        return self.generateRandomNumber()
    
    def setMaximum(self, maximum):
        self.maxNumber = maximum    
        
    def setScore(self, score):
        self.currentScore = score    
    
    def generateRandomNumber(self):
        self.answer = random.randint(1, self.maxNumber)        
    
    def getUsername(self):
        return self.userName
    
    def getAnswer(self):
        return self.answer
        
        