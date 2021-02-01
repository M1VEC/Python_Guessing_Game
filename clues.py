import random
class clues:

    def __init__(self, answer, maxNumber):
        self.answer = answer
        self.maxNumber = maxNumber
        self.numberDividables = []
        self.isNumberDividable()
        self.clueChoice = ['Even', 'Higher', 'Dividable']
        return

    def selectClue(self, userGuess):
        if self.answer % userGuess == 0:
            return "The number is dividable by your guess"
        else:
            clue = random.choice(self.clueChoice)
            if clue == 'Even':
                self.clueChoice.remove('Even')
                return self.isNumberEven()
            elif clue == 'Higher':
                return self.isNumberHigher(userGuess)
            else:
                if self.getDividable() != "No more multiples remain":
                    return self.getDividable()
                else:
                    self.clueChoice.remove('Dividable')
                    return self.selectClue(userGuess)
        
    def isNumberHigher(self, userGuess):
        if userGuess < self.answer:
            return "Higher"
        else:
            return "Lower"

    def isNumberEven(self):
        if self.answer % 2 == 0:
            return "It is an even number"
        else:
            return "It is an odd number"

    def isNumberDividable(self):
        for number in range(2,self.answer+1):
            if self.answer % number == 0:
                self.numberDividables.append(number)    
        return
    
    def getDividable(self):
        if len(self.numberDividables) != 0:
            dividable = random.choice(self.numberDividables)
            self.numberDividables.remove(dividable)
            return "Number is a multiple of " + str(dividable)
        else:
            return "No more multiples remain"

    
    
    


