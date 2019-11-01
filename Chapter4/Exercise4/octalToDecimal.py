"""
Heber Cooke 10/15/2019
Chapter 4 Exercise 4
Octal number to decimal number
"""


# Octal to decimal
octNum = input("Enter a Octal number: ")
decimal = 0
exponent = len(octNum) -1
for digit in octNum:
    decimal = decimal + int(digit) * 8 ** exponent
    exponent = exponent - 1
print("The Decimal number is: ", decimal)