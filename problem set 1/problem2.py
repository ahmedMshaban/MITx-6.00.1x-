#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:58:20 2019

@author: ahmedshaban
"""

count = 0
current_start = 0
current_end = 3
s = 'azcbobobegghakl'
string_length = len(s)

while current_end <= string_length:
    if 'bob' == s[current_start: current_end]:
        count += 1
    current_start += 1
    current_end += 1
    
print (count)