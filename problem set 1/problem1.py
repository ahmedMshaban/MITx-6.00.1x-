#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 13:14:05 2019

@author: ahmedshaban
"""


count = 0
s = 'azcbobobegghakl'
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o'  or letter == 'u':
        count += 1

print ("Number of vowels: " + str(count))