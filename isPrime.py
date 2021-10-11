# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:03:40 2018

@author: EMAN
"""
import math

def isPrime(x):
    c=True
    i=3
    while i<=int(math.sqrt(x)):
        if x==2 :
            c=True
        elif x==0 :
            c=False
        elif int(x%2)==0:
             c=False
        elif int(x%i)==0:
             c=False
        i=i+2
    if c==True:
        print(x,"Is prime")
    else:
        print(x,"Not prime")

isPrime(int(input("Enter the number ")))






