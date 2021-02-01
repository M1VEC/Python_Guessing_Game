class clues:

    def __init__(self, answer, maxNumber):
        self.answer = answer
        self.maxNumber = maxNumber
        self.numberDividables = self.numberDividable()
        return

    def isNumberHigher(self, userNumber):
        if userNumber > self.answer:
            return "Higher"
        else:
            return "Lower"

    def isNumberEven(self):
        if self.answer % 2 == 0:
            return "It is an even number"
        else:
            return "It is an odd number"

    def numberDividable(self):    
        return

