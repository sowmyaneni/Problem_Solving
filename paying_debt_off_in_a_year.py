'''
    balance: outstanding balance on credit card, int or float
    annualInterestRate: annual interest rate as decimal
    monthlyPaymentRate: Min. monthy payment rate as decimal
'''
for i in range(1,13):

    min_payment = balance*monthlyPaymentRate
    unpaid_balance = balance - min_payment
    interest_accrued=(annualInterestRate/12.0)*unpaid_balance
    balance = unpaid_balance + interest_accrued
    #print('Month ' + str(i)+ ' Remaining balance: ' ,round(balance,2))
print("Remaining Balance: ", round(balance,2))
