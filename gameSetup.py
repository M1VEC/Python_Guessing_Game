import random
class game:
    
    def __init__(self, userName, maxNumber):
        self.userName = userName
        self.maxNumber = maxNumber
        self.setAnswer(self.maxNumber)
        
    def setUserName(self, name):
        self.userName = name
        
    def setAnswer(self, maxNumber):
        self.answer = random.randint(1,maxNumber)
    
    def setMaxNumber(self, maxNumber):
        self.maximumNumber = maxNumber    
        
    def getUsername(self):
        return self.userName
    
    def getAnswer(self):
        return self.answer
    
    def getMaxNumber(self):
        return self.maxNumber
        
