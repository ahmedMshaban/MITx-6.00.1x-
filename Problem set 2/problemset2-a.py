#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 07:42:50 2019

@author: ahmedshaban
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
remainingBalance = balance
unpaidBalance = balance
interest = 0

for month in range(12):
    minimumPayment = remainingBalance * monthlyPaymentRate
    unpaidBalance = remainingBalance - minimumPayment
    interest = unpaidBalance * (annualInterestRate/12.0)
    remainingBalance = remainingBalance - (minimumPayment - interest)

print("Remaining balance:", round(remainingBalance,2))