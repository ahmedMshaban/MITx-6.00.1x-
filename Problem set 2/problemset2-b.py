#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 08:20:42 2019

@author: ahmedshaban
"""

balance = 3329
annualInterestRate = 0.2
monthlyUnpaidBalance = 0
remainingBalance = balance
minimumFixedpayment = 10

while remainingBalance > 0:
    for month in range(12):
        monthlyUnpaidBalance = remainingBalance - minimumFixedpayment
        remainingBalance = monthlyUnpaidBalance + ((annualInterestRate/12) * monthlyUnpaidBalance)
        
    if remainingBalance <= 0:
        print(round(minimumFixedpayment, 2))
        
    else: 
        minimumFixedpayment += 10
        remainingBalance = balance
        