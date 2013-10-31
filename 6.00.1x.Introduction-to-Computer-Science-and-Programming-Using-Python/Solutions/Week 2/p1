balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12
annualPayment = 0.0
for month in range(1, 13):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    updatedBalanceEachMonth = (balance - minimumMonthlyPayment) * (1 + monthlyInterestRate)
    annualPayment += minimumMonthlyPayment
    print("Month: {0}".format(month))
    print("Minimum monthly payment: {0:.2f}".format(minimumMonthlyPayment))
    print("Remaining balance: {0:.2f}".format(updatedBalanceEachMonth))
    balance = updatedBalanceEachMonth
print("Total paid: {0:.2f}".format(annualPayment))
print("Remaining balance: {0:.2f}".format(balance))
