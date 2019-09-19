#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:32:09 2019

@author: ahmedshaban
"""

import math

def polysum (n, s):
    '''
    n: number of sides
    s: Each side has length s
    
    returns: total =  area + perimeter squared rounded to 4 decimal places.
    '''
    return round((0.25*n*s**2)/math.tan(math.pi/n) + (n*s)**2 , 4)