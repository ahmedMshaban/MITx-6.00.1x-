#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 12:24:56 2019

@author: ahmedshaban
"""

low = 0
heigh = 100
ans = int((low + heigh) / 2)
instructionMesage = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "
print ("Please think of a number between 0 and 100!")
guessCheck = ''

while guessCheck != "c":
    print ("Is your secret number", ans, end='' "? \n")
    guessCheck = input (instructionMesage)
    if guessCheck == "h":
        heigh = ans
        ans = int((low + heigh) / 2)
    elif guessCheck == "l":
        low = ans
        ans = int((low + heigh) / 2)
    elif guessCheck == "c":
        print("Game over. Your secret number was: ", ans)
    else: 
        print("Sorry, I did not understand your input.")
        

