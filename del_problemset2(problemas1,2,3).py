# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:28:20 2020

@author: carlo
"""
# PROBLEM SET 2
# PROBLEM 1

def remaining_balance(balance, mrate, arate):
    Unpaid_balance = monthly_unpaid_balance(balance, mrate)
    This_months_interest = interest_after_monthly_min_payment(arate, mrate, balance)
    return Unpaid_balance + This_months_interest


def minimum_monthly_payment(balance, mrate):
    """
    balance is float
    mrate is float and represents the minimum rate of payment PER MONTH
    """
    return balance*mrate


def monthly_unpaid_balance(balance, mrate):
    return balance - minimum_monthly_payment(balance, mrate)


def interest_after_monthly_min_payment(arate, mrate, balance):
    return arate/12*monthly_unpaid_balance(balance, mrate)

current_balance = balance
ARATE = annualInterestRate
MRATE = monthlyPaymentRate
summ = 0
for i in range(12):
    """ print("Month "+ str(i+1) + 
          "\nBalance:\t\t", remaining_balance(current_balance, MRATE, ARATE),
          "\nMinimum Payment:\t\t", minimum_monthly_payment(current_balance, MRATE), 
          "\nUnpaid Balance:\t\t", monthly_unpaid_balance(current_balance,MRATE),
          "\nInterest:\t\t", interest_after_monthly_min_payment(ARATE,MRATE,current_balance))
    print("\n\n")"""
    summ += minimum_monthly_payment(current_balance,MRATE)
    current_balance = remaining_balance(current_balance, MRATE, ARATE)
# print("Added payments:\t\t", summ)
print(round(current_balance,2))


# PROBLEM 2

balance = 319; annualInterestRate = 0.25



balance1 = balance
payment=0

while True:
    if balance1 < 0:
        break
    balance1 = balance
    for i in range(12):
        balance1=balance1-payment
        balance1=balance1*(1+annualInterestRate/12)
    payment += 10
    # print(balance1)
print(payment-10)


# PROBLEM 3

#Given the annualInterestRate and balance
# variables...

def chekar(monthlyPaymentRate,monthlyInterestRate,balance):
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    return balance

def confuso(bottom,top,inter,balance):
    
    if abs(chekar((bottom+top)/2,inter,balance)) > 0.01:
        if chekar((bottom+top)/2,inter,balance) > 0.01:
            return confuso((bottom+top)/2,top,inter,balance)
        else:
            return confuso(bottom,(bottom+top)/2,inter,balance)
    else:
        return (bottom+top)/2

actual_monthly_rate=annualInterestRate/12
actual_yearly_rate=(1+actual_monthly_rate)**12
top = balance*actual_yearly_rate/12
bottom = balance/12
print(confuso(bottom,top,actual_monthly_rate,balance1))



# 3