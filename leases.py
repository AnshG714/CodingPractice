class LeaseCalc:
    def __init__(self, fmv, interest, monthlyPayment, numPeriods=12):
        self.fmv = fmv
        self.interest = interest / (numPeriods * 100)
        self.monthlyPayment = monthlyPayment
        self.numPeriods = numPeriods
        self.carryingValue = fmv

    def computePeriods(self, n=2):
        for i in range(n):
            print("Month " + str(i + 1))
            interestExpense = self.carryingValue * self.interest
            leaseLiability = self.monthlyPayment - interestExpense
            print("Interest Expense", interestExpense)
            print("Lease Liability", leaseLiability)
            self.carryingValue -= leaseLiability
            print()


l = LeaseCalc(100000.03, 8, 2027.64)
l.computePeriods()
