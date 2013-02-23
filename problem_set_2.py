#MITx: 6.00x Introduction to Computer Science and Programming
#Problem Set 2 Code
#These are my version of codes for 6.00x open course provided on edxonline.org 

#minimum payment

def minimumPayment(balance, annualInterestRate, monthlyPaymentRate):
    monthlyInterestRate=annualInterestRate/12.0
    minimumMonthlyPaymentRate=monthlyPaymentRate
    totalPayment=0
    for month in range(1,13):
        print('Month: ' + str(month))
        minimumMonthlyPayment= (minimumMonthlyPaymentRate*balance)
        totalPayment+=minimumMonthlyPayment
        print('Minimum monthly payment: ' + str(round(minimumMonthlyPayment,2)))
        monthlyUnpaidBalance=balance-minimumMonthlyPayment
        balance=monthlyUnpaidBalance+(monthlyInterestRate*monthlyUnpaidBalance)
        print('Remaining balance: ' + str(round(balance,2)))
    print('Total paid: ' + str(round(totalPayment,2)))
    print('Remaining balance: ' + str(round(balance,2)))

#fixed payment

def fixedPayment(balance, annualInterestRate):
    monthlyInterestRate=annualInterestRate/12.0
    lowestPayment=10
    b=balance
    while True:
        for month in range(1,13):
            monthlyUnpaidBalance=balance-lowestPayment
            balance=monthlyUnpaidBalance+(monthlyUnpaidBalance*monthlyInterestRate)
        if balance>=0:
            lowestPayment+=10
            balance=b
        else:
            break
    print('Lowest Payment: '+str(lowestPayment))

#Bisection

def bisection(balance, annualInterestRate):
    monthlyInterestRate=annualInterestRate / 12.0
    low=balance/12
    high=(balance*(1 + monthlyInterestRate)**12) / 12.0
    b=balance
    epsilon=0.01
    lowestPayment=(low+high)/2
    while abs(balance)>epsilon:
        balance=b
        for month in range(1,13):
            monthlyUnpaidBalance=balance-lowestPayment
            balance=monthlyUnpaidBalance+(monthlyUnpaidBalance*monthlyInterestRate)
        if balance>0:
            low=lowestPayment
        elif balance<0:
            high=lowestPayment
        lowestPayment=(low+high)/2    
    print('Lowest Payment: '+str(round(lowestPayment,2)))                                  


#end of problem set 2
