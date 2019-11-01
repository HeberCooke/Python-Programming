"""
Heber Cooke 10/3/2019
Chapter 2 exercise 10

This program calculates the total pay for time and overtime

the program takes an input of the hourly wage
an input of the regular pay hours 
an input of the overtime pay hours
the program calculates the overtime pay by multiplying wage by 1.5
the reg pay and the overtime pay are added together
the program prints out the totla pay
"""

payRate = float(input("Enter the payRate: "))
regHours = float(input("Enter regular hours worked "))
overTimeHours = float(input("Enter overtime hours worked "))

totalPay = (payRate * regHours) + (overTimeHours * payRate * 1.5)
print("Total Pay is $",totalPay)
