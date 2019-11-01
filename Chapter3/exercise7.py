"""
Heber Cooke 10/8/2019   
Chapter 3 Exercise 7
This program calculates the total salary per year with a
salary increase up to 10 years. 

The inputs are: starting salary,percent increase,years scheduled
The output is: year number , salary for the year 
"""

salary = float(input("Enter starting salary: "))
years = int(input("Enter the number of years sceduled: "))
salaryIncreace = float(input("Enter salary increace: "))
percent = salaryIncreace / 100
year = 1

print(percent)
print("%-3s%12s" % ("Year", "Salary"))
while True:
    print("%-3d  %12.2f" % (year, salary))   
    
    if year < 10:       
       salary += (percent * salary)

    if (year + 1) == (years + 1) :
        break
    year += 1
    
