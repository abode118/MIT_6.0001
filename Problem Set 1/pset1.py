#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 20:45:51 2018

@author: abode118
"""

#Part 1

"""How many months until I can afford a downpayment on my dream home?"""
annual_salary = int(input("Starting salary: "))
portion_saved = float(input("Savings rate: "))
total_cost = int(input("Cost of dream home: "))
portion_down_payment = .25 * total_cost
current_savings = 0
r = 0.04
months = 0

while current_savings < portion_down_payment:
    current_savings = (current_savings * (1+r/12)) + \
    portion_saved*(annual_salary/12)
    months += 1
print("Number of months:",months)


#Part 2
"""How many months until I can afford a downpayment on my dream home, if I 
   have a semi annual raise?"""
annual_salary = int(input("Starting salary: "))
portion_saved = float(input("Savings rate: "))
total_cost = int(input("Cost of dream home: "))
semi_annual_raise = float(input("Semi-annual salary raise: "))
portion_down_payment = .25 * total_cost
current_savings = 0
r = 0.04
months = 0
while current_savings < portion_down_payment:
    if months > 0 and months % 6 == 0:
        annual_salary = annual_salary * (1+semi_annual_raise)
    current_savings = (current_savings * (1+r/12)) + \
    portion_saved*(annual_salary/12)
    months += 1
print("Number of months:",months)


#Part 3
"""What should my savings rate be if I want to put down a downpayment in a 
specified number of months/years?"""
starting_salary = int(input("Starting salary: "))
total_cost = 1000000
semi_annual_raise = .07
portion_down_payment = .25 * total_cost
current_savings = 0
r = 0.04

high = 10000
low = 0
savings_rate = int((high + low)/2)
num_guesses = 0
epsilon = 100

while abs(portion_down_payment - current_savings) >= epsilon:
    annual_salary = starting_salary #reset for each guess
    current_savings = 0 #reset for each guess
    num_guesses += 1 #keep track of guesses
    savings_rate = int((high + low)/2) #recalculate
    for month in range(36):
        if month > 0 and month % 6 == 0:
            annual_salary = annual_salary * (1+semi_annual_raise)
        current_savings = (current_savings * (1+r/12)) + \
        ((savings_rate/10000) * (annual_salary/12))
    if portion_down_payment - current_savings >= epsilon:
        low = savings_rate
        if high - low == 1: #highest "low" can get is 9999 bc ints round down
            break    
    elif portion_down_payment - current_savings > epsilon:
            high = savings_rate
   
if abs(portion_down_payment - current_savings) <= epsilon:
    print("Savings rate is", savings_rate/10000.00)
    print("Number of guesses =", num_guesses)
else:
     print("It is not possible to pay the downpayment in three years")
