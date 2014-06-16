#!/usr/bin/python

import sys

balance = sys.argv[0]
annualInterestRate = sys.argv[1]
monthlyPaymentRate = sys.argv[2]

def pay_minimum(balance, annualInterestRate, monthlyPaymentRate):
    months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    monthlyInterestRate = (annualInterestRate) / 12.0
    minimumMonthlyPayment = (monthlyPaymentRate) * (balance)
    monthlyUnpaidBalance = (balance) - (minimumMonthlyPayment)
    updatedBalanceEachMonth = (monthlyUnpaidBalance) + (monthlyInterestRate * monthlyUnpaidBalance)

    for month in months:
        print "Month: " + month
        print "Minimum monthly payment: " + str(round(minimumMonthlyPayment, 2))
        print "Remaining balance: " + str(round(updatedBalanceEachMonth, 2))

    print "Total paid: " + balance
    print "Remaining balance: " + str(round(updatedBalanceEachMonth, 2))

pay_minimum(balance, annualInterestRate, monthlyPaymentRate)
