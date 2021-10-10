# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 20:03:45 2021

@author: DA_VINCI
"""
def bal(balance, rate, payment):
    while True:
        monthlyrate = rate / 12.0
        pay = 0
        newbalance = balance
        lastbalance = 0
        for c in range(12):
            newbalance = newbalance - payment
            if newbalance <= 0:
                pay = payment
                return pay
            else:
                lastbalance = newbalance + (monthlyrate * newbalance)
                newbalance = lastbalance
        payment += 10
print(bal(3926, 0.2, 10))