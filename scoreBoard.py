class scoreBoard:
    
    def __init__(self):
        self.scoreBoard = 0
        
    def addPoint(self):
        self.scoreBoard = self.scoreBoard + 1
        
    def penalty(self):
        self.scoreBoard = self.scoreBoard + 2
        
    def getScoreBoard(self):
        return self.scoreBoard
    
    
