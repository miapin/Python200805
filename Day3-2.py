# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 09:58:33 2020

@author: AE401
"""

def add3(a,b,c):
    ans=a+b+c
    return ans

num1=int(input("Please enter a number:"))
num2=int(input("Please enter a number:"))
num3=int(input("Please enter a number:"))

#A=add3(num1,num2,num3) #sol1 以變數儲存
print(add3(num1,num2,num3)) #sol2 直接呼叫
