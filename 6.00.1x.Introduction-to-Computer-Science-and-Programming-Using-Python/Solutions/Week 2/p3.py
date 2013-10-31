def pay_off_debt_in_a_year(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12
    updatedBalanceEachMonth = balance
    monthlyPaymentLowerBound = balance / 12
    monthlyPaymentUpperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12
    minimumMonthlyPayment = (monthlyPaymentUpperBound + monthlyPaymentLowerBound) / 2.0
    
    while abs(monthlyPaymentUpperBound - monthlyPaymentLowerBound) > 0.000001:
        minimumMonthlyPayment = (monthlyPaymentUpperBound + monthlyPaymentLowerBound) / 2.0
        updatedBalanceEachMonth = balance
        
        for i in range(12):
            updatedBalanceEachMonth = (updatedBalanceEachMonth - minimumMonthlyPayment) * (1 + monthlyInterestRate)
            
            
        if updatedBalanceEachMonth >= 0.0:
            monthlyPaymentLowerBound = minimumMonthlyPayment
        else:
            monthlyPaymentUpperBound = minimumMonthlyPayment
        

    print("Lowest Payment: {0:.2f}".format(minimumMonthlyPayment))

pay_off_debt_in_a_year(balance, annualInterestRate)
  
pay_off_debt_in_a_year(320000, 0.2)
pay_off_debt_in_a_year(999999, 0.18)
  
pay_off_debt_in_a_year(3329, 0.2)
pay_off_debt_in_a_year(4773, 0.2)
pay_off_debt_in_a_year(3926, 0.2)