# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def bal(balance, rate, paid):
    for c in range(12):
        monthrate = rate / 12.0
        currentmonthpayment = balance * paid
        unpaidbalance = balance - currentmonthpayment
        newbalance = unpaidbalance + (monthrate * unpaidbalance)
        balance = newbalance
    return round(balance, 2)

print('remaining is: ', bal(484, 0.2, 0.04))

    