#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 10:56:19 2019

@author: ahmedshaban
"""

balance = 999999
annualInterestRate = 0.18
epslion = 0.01
monthlyInterestRate = annualInterestRate/12.0
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
minimumFixedpayment = (upperBound + lowerBound) / 2
remainingBalance = balance


while abs(remainingBalance) > epslion:
    
    for month in range(12):
        monthlyUnpaidBalance = remainingBalance - minimumFixedpayment
        remainingBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    

    if abs(remainingBalance) < epslion:
        print("Lowest Payment: ", round(minimumFixedpayment, 2))
        break;
        
    else: 
        if remainingBalance > epslion:
            lowerBound = minimumFixedpayment
            minimumFixedpayment = (upperBound + lowerBound) / 2
        else:
            upperBound = minimumFixedpayment
            minimumFixedpayment = (upperBound + lowerBound) / 2
    remainingBalance = balance
        