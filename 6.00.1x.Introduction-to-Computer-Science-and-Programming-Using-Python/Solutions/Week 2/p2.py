payment_base = 0
balance_new = balance

while balance_new > 0:
    balance_new = balance
    payment_base += 10
    if payment_base > (balance_new * annualInterestRate / 12):
        for i in range(12):
            balance_new -= payment_base
            balance_new += (balance_new * annualInterestRate / 12)

print 'Lowest Payment: %s' % (payment_base)
