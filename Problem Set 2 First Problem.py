# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def bal(balance, rate, paid, i):
    if i == 13:
        return balance
    else:
        monthrate = rate / 12.0
        currentmonthpayment = balance * paid
        unpaidbalance = balance - currentmonthpayment
        newbalance = unpaidbalance + (monthrate * unpaidbalance)
        i += 1
    return bal(newbalance, rate, paid, i)

print('remaining is: ', bal(484, 0.2, 0.04, 1))

    