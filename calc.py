#!/usr/bin/python

import sys

balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
monthlyInterestRate = (annualInterestRate) / 2.0
minimumMonthlyPayment = (monthlyPaymentRate) * (balance)
monthlyUnpaidBalance = (balance) - (minimumMonthlyPayment)


def pay_minimum(balance, annualInterestRate, monthlyPaymentRate):
    updatedBalanceEachMonth = (monthlyUnpaidBalance) + (monthlyInterestRate * monthlyUnpaidBalance)
    minimumMonthlyPayment = (monthlyPaymentRate) * (updatedBalanceEachMonth)
    totalPaymentsMade = 0
    for month in months:
        balance = round(updatedBalanceEachMonth, 2)
        updatedBalanceEachMonth -= minimumMonthlyPayment
        minimumMonthlyPayment = (monthlyPaymentRate) * (updatedBalanceEachMonth)
        print "Month: " + month
        print "Minimum monthly payment: " + str(round(minimumMonthlyPayment, 2))
        print "Remaining balance: " + str(round(updatedBalanceEachMonth, 2))
        totalPaymentsMade += minimumMonthlyPayment

    print "Total paid: " + str(round(totalPaymentsMade, 2))
    print "Remaining balance: " + str(round(updatedBalanceEachMonth, 2))

pay_minimum(balance, annualInterestRate, monthlyPaymentRate)
