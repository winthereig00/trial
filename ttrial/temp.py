# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("hello world")

print(2+2+1)

def p(x):
    if x<10:
        return(x**2+1)
    return(p(x-1))

print(p(5)) 