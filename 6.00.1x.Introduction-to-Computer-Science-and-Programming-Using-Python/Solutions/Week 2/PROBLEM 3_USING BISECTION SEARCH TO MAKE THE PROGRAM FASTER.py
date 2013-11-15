def run(balance, annualInterestRate):
    lowerBound = balance / 12.0
    upperBound = (balance * (1 + (annualInterestRate / 12.0)) ** 12) / 12.0

    E = 0.01
    while(True):
        newBalance = balance
        monthlyPayout = (lowerBound + upperBound) / 2.0
        for month in range(12):
            newBalance = (newBalance - monthlyPayout) * (1 + (annualInterestRate / 12))
        if round(newBalance, 2) < E:
            upperBound = monthlyPayout
        elif round(newBalance, 2) > E:
            lowerBound = monthlyPayout
        else:
            return round(monthlyPayout, 2)

print "Lowest Payment: %s" % (run(balance, annualInterestRate))