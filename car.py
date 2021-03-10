class Car():
    """
    totalAmount: The car price, in dollar
    downPayment: The downpayment you want to pay, in dollar
    interestRate: The annual interest, in %
    loanPeriod: The loan period, in year

    """

    def __init__(self, totalAmount=100000, downPayment=10000, interestRate=3.5, loanPeriod=9):
        self.totalAmount = totalAmount
        self.downPayment = downPayment
        self.interestRate = interestRate
        self.loanPeriod = loanPeriod

    def getLoanAmount(self):
        return self.totalAmount - self.downPayment

    def getTotalPayment(self):
        return self.getLoanAmount()*(1+self.loanPeriod*self.interestRate/100)

    def getTotalInterest(self):
        return self.getTotalPayment()-self.getLoanAmount()

    def getMonthlyInstallment(self):
        return self.getTotalPayment()/(12*self.loanPeriod)