#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:22:15 2019

@author: ahmedshaban
"""

s = 'bsclgvioabjqu'

current_substring = ''
longest_substring = ''
left_pointer = 0
right_pointer = 1
string_length = len(s)

while right_pointer < string_length:
    
    if s[left_pointer] > s[right_pointer]:
        current_substring += s[left_pointer]
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
        current_substring = ''
        
    else: 
        current_substring += s[left_pointer]
    
    left_pointer += 1
    right_pointer += 1
    
    if (right_pointer == string_length) and (s[left_pointer] > s[left_pointer-1]): 
        current_substring += s[left_pointer]
        

if len(current_substring) > len(longest_substring):
    longest_substring = current_substring

print ("Longest substring in alphabetical order is: " + longest_substring)