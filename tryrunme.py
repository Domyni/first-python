from car import Car

while True:

    totalAmount = input("\n\nWelcome to the RBA Car Loan Calculator.\n\n Please enter the total amount.\n")
    try:
        totalAmount = int(totalAmount)
        break

    except ValueError:
        print("\nPlease enter a number.")

# Part2 : Store the downPayment

while True:

    downPayment = input("Please enter the down payment.\n")
    try:
        downPayment = int(downPayment)
        break

    except ValueError:
        print("\nPlease enter a number.")



# Part3 : Store the interestRate

while True:

    interestRate = input("Please enter the interest rate.\n")
    try:
        interestRate = float(interestRate)
        break

    except ValueError:
        print("\nPlease enter a number.")


# Part4 : Store the loanPeriod

while True:

    loanPeriod = input("Please enter the loan period.\n")
    try:
        loanPeriod = float(loanPeriod)
        break

    except ValueError:
        print("\nPlease enter a number.")


yourcar = Car(totalAmount, downPayment, interestRate, loanPeriod)
print("")
print("The loan amount is: {:.2f} dollars".format (yourcar.getLoanAmount()))
print("")
print("The total payment (including interest) you need to pay is: {:.2f} dollars".format (yourcar.getTotalPayment()))
print("")
print("The total interest incurred is: {:.2f} dollars".format (yourcar.getTotalInterest()))  
print("")
print("The monthly installment is: {:.2f} dollars".format (yourcar.getMonthlyInstallment())) 