class BondCalc:
    def __init__(self, faceValue, yld, interest, numYears, numPeriods=2):
        self.faceValue = faceValue
        self.i = yld / (numPeriods * 100)
        self.n = numPeriods * numYears
        self.numPeriods = numPeriods
        self.interest = interest / 100
        self.isPremium = False

    def calculatePV(self):
        A = self.faceValue * (self.interest / self.numPeriods)
        self.A = A

        firstTerm = A * (1 - ((1 + self.i) ** (-self.n))) / self.i
        secondTerm = self.faceValue / ((1 + self.i) ** self.n)
        presentVal = firstTerm + secondTerm
        if presentVal > self.faceValue:
            self.isPremium = True

        return presentVal

    def getInitialBuyout(self):
        self.carryingValue = self.faceValue
        res = ""
        res += "cash \t" + str(self.calculatePV())
        if not self.isPremium:
            res += "\nbond discount \t" + \
                str(self.faceValue - self.calculatePV())
            self.carryingValue -= self.faceValue - self.calculatePV()
        else:
            res += "\n\t\t\t Bond Premium\t" + \
                str(self.calculatePV() - self.faceValue)
            self.carryingValue += self.calculatePV() - self.faceValue
        res += "\n\t\t\t Bond Payable\t" + str(self.faceValue)
        return res

    def getNInterests(self, n):
        print("Recording Purchase: \n")
        print(self.getInitialBuyout() + "\n")
        for _ in range(n):
            interestExpense = self.carryingValue * self.i
            if self.isPremium:
                print("Interest Expense \t" + str(interestExpense))
                print("Bond Premium \t" + str(self.A - interestExpense))
                print("\t\t\t Cash\t" + str(self.A))
                self.carryingValue -= self.A - interestExpense
            else:
                print("Interest Expense \t" + str(interestExpense))
                print("\t\t\t Bond Discount \t" +
                      str(interestExpense - self.A))
                print("\t\t\t Cash\t" + str(self.A))
                self.carryingValue += interestExpense - self.A
            print("\n")


b = BondCalc(10000000, 8, 7.70, 5)
b.getNInterests(2)
