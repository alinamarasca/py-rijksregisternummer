import random

class rrn:
  # class variables
  
    def __init__(self, dateOfBirth, gender = "female"):
        self.current = ""
        self.dateOfBirth = dateOfBirth
        self.gender = gender
        self.temp = self.dateOfBirth.split('/')
        self.dayOfBirth = ""
        self.monthOfBirth = ""
        self.yearOfBirth = ""
        # self.current = "".join(self.temp)
        # self.firstBlock = ".".join(self.temp)

        # method returns bis first bloc
    # def calc1blockBis(self):
    #     self.num = random.choice([20, 40])
    #     self.temp[1] = str(int(self.temp[1]) + (self.num))
    #     self.current = ".".join(self.temp)
    #     return print(".".join(self.temp))

        # method return isnz first block
    def calc1blockIsnz(self):
        # self.dayOfBirth = self.temp[0]
        # self.monthOfBirth = self.temp[1]
        # self.yearOfBirth = self.temp[2]
        self.temp = self.dateOfBirth.split('/')
        self.current = ".".join(self.temp)
        return print(".".join(self.temp))

      

a = rrn('10/10/10')  
a.calc1blockIsnz()
print(a.current)







