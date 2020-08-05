# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:17:45 2020

@author: AE401
"""




scores=[]

def score(p):
    total=0
    for a in scores:
        total=total+a
    return total/n

def high(h):
    highest=0
    for c in scores:
        if c>highest:
            highest=c
    return highest

def low(l):
    lowest=100
    for d in scores:
        if d<lowest:
            lowest=d
    return lowest

n=int(input("How many people are there in your class?"))
for b in range(n):
    S=int(input ("please enter the scores:"))
    scores.append(S) 
print("The average is",score(scores))
print("The highest is",high(scores))
print("The lowest is",low(scores))