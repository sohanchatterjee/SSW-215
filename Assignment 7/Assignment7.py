# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 19:08:30 2022

@author: Sohan Chatterjee

SSW 215 Assignment 7

November 28, 2022
"""
import numpy as np
import numpy.random
import numpy.linalg as LA
import pandas as pd

#Problem 1
A = np.random.randint(50, 120, size=(3,5))
B = np.random.randint(10, 60, size=(5,6))
C = np.dot(A,B)
R = C*10
print(C, "\n")
print(R, "\n")

#Problem 2
X = np.array([[4,-8,-2,7],[-4,1,-9,-4],[-2,-64,-6,5],[-7,-8,-25,-2]])
Y = np.array([9,-5,5,2])
Z = LA.solve(X,Y)
print(Z, "\n")

#Problem 3
df = pd.read_csv('salary.txt', sep=' ', names=["Employee", "Salary", "Year", "Gender"])
print(df, "\n")
print(df.iloc[:,:2], "\n")

salaryData = df.iloc[:,[1,3]]
grouped = salaryData.groupby('Gender')
print(grouped.describe(), "\n")
df.plot.scatter(x='Year', y='Salary')