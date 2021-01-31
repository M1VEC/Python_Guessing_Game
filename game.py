# import inPlay
class game:
    
    # __userName__ = ""
    # __answer__ = 0
    # __maximumNumber__ = 0
    # __currentScore__ = 0
    
    
    def __init__(self, userName, currentScore):
        self.userName = userName
        self.currentScore = currentScore
        
    def setUserName(self, name):
        self.userName = name
        
    def setAnswer(self, answer):
        self.answer = answer
    
    def setMaximum(self, maximum):
        self.maximumNumber = maximum    
        
    def setScore(self, score):
        self.currentScore = score    
    
    def getUsername(self):
        return self.userName
    
    def getAnswer(self):
        return str(self.answer)
        
        