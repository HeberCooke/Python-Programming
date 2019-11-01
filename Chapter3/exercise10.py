"""
Heber Cooke 10/8/2019
Chapter 2 Exercise 10

The Credit Plan calculates the payments for the life as a loan
with a 10% down payment and payments 5% of price after down payment
annual interest rate of 12%
input: price of item

output: table 
    month number (start at 1)
    current total balance owed
    intrest owed for the month
    amount of principal owed for the month
    the payment for the month
    the balance remaining after payment
"""
price = float(input("Enter the price: "))

down = price * .1
balance = price - down
payment = balance * .05
rate = (0.12 / 12)

month = 0
print("%-8s%-12s%-12s%-12s%-12s%-12s" % ("Month", "Balance", "Interest","Principal", "Payment", "Balance after Payment"))


while balance > payment:
    month += 1
    interest = balance * rate
    principal = payment - interest
    bal = balance - principal
    print("%-8d%-12.2f%-12.2f%-12.2f%-12.2f%-12.2f"% (month, balance, interest, principal, payment, bal))
    
    balance = bal

payment = balance
interest = 0
principal = payment
bal = 0
month += 1
print("%-8d%-12.2f%-12.2f%-12.2f%-12.2f%-12.2f"% (month, balance, interest, principal, payment, bal))