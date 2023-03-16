# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:00:02 2022

@author: Sohan Chatterjee

SSW 215 Assignment 4
"""
import random

print("1. Sum and Average")
print("2. Salary Table")
print("3. Lucky Sevens")
print("4. Exit")
choice = int(input("Please choose an option: "))
while (choice != 4):
    if(choice == 1):
        count = 0
        numSum = 0
        numbers = int(input("Enter several numbers. Press the enter key when done. "))
        while (numbers >= 1):
            numSum += int(numbers % 10)
            numbers /= 10
            count += 1
            print(count)
        print("The sum of the numbers is: ", numSum)
        average = numSum / count
        print("The average of the numbers is ", average)
        print("1. Sum and Average")
        print("2. Salary Table")
        print("3. Lucky Sevens")
        print("4. Exit")
        choice = int(input("Please choose an option: "))
    elif(choice == 2):
        startingSal= int(input("Please enter the starting salary: "))
        pctIncrease = int(input("Please enter the percentage increase: "))
        pctIncrease /= 100
        pctIncrease += 1
        numYears = int(input("Please enter the number of years: "))
        salary = []
        salaryInfo = {}
        salaryInfo["Year"] = "1"
        salaryInfo["Salary"] = startingSal
        if (numYears < 10):
            for year in range(numYears-1):
                salary.append(startingSal)
                startingSal *= pctIncrease
                print("Year: ", year+1, "Salary: $", salary[year])
        else:
            for year in range(9):
                salary.append(startingSal)
                startingSal *= pctIncrease
            for year in range(numYears-9):
                salary.append(startingSal)
            for year in range(numYears):
                print("Year: ", year+1, "Salary: $", salary[year])
        print("1. Sum and Average")
        print("2. Salary Table")
        print("3. Lucky Sevens")
        print("4. Exit")
        choice = int(input("Please choose an option: "))
    elif (choice == 3):
        pot = int(input("Enter the amount of money you'd like in the pot: $"))
        rollCount = 0
        maxPot = 0
        while (pot > 0):
            roll = random.randint(1,6)
            roll2 = random.randint(1,6)
            totalRoll = roll + roll2
            print(roll, roll2, totalRoll)
            rollCount += 1
            if(totalRoll == 7):
                pot += 4
            else:
                pot -= 1
            print("Your pot is now $", pot)
            if (pot > maxPot):
                maxPot = pot
        if(pot == 0):
            print("Game over, you are out of money. Your total rolls were ", rollCount)
            print("The maximum amount of money in the pot was $", maxPot)
        print("1. Sum and Average")
        print("2. Salary Table")
        print("3. Lucky Sevens")
        print("4. Exit")
        choice = int(input("Please choose an option: "))
    else:
        choice = int(input("Invalid option. Please choose 1-4: "))