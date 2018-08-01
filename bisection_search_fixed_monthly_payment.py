monthlyInterest = annualInterestRate/12.0
originalBalance = balance
lowerBound = balance/12
upperBound = (balance * (1 + monthlyInterest)**12)/12

while round(balance,2) != 0:
    balance = originalBalance
    midpoint = (lowerBound + upperBound)/2
    #print("midpoint: ", midpoint)
    payment = midpoint
    #print("payment: ", payment)

    for i in range(1,13):
        balance = (balance - payment) * (1 + monthlyInterest)
    if balance < 0:
        #print("low balance",balance)
        upperBound = midpoint
    elif balance > 0:
        #print("high balance",balance)
        lowerBound = midpoint
print("Lowest Payment: ", round(payment,2))
