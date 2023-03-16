# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 21:34:17 2022

@author: Sohan Chatterjee

SSW 215 Assignment 5
"""

def fibonacci(n):
    if(n<=0):
        print("Number of terms must be greater than 0")
    last = 0
    second = 1
    if n == 1:
        print(last)
    elif n==2:
        print(second)
    else:
        for i in range(3, n+1):
            result = last + second
            last = second
            second = result
        print(result)
        
fibonacciNum = int(input("Enter a number display the Fibonacci sequence up to: "))
fibonacci(fibonacciNum)
        
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primeDict():
    myDict = {"A": 11, "B": 4, "C": 7, "D": 15, "E": 1}
    for i in myDict.keys():
        if isPrime(myDict[i]) == True:
            print(i, "is a prime key")
            
primeDict()

def powerLoop(n, m):
    if (m<0):
        print("Use a positive number")
    result = 1;
    for i in range(m):
        result *= n
    print(result)
        
powerLoop(2, 4)