"""
Heber Cooke 10/15/2019
Chapter 4 Exercise 4
Convert a decimal number to an octal number 
"""

#decimal to octal
decimal = int(input("Enter a Decimal number: "))
if decimal == 0:
    print(0)
else:
    bString = ""
    while decimal > 0:
        remainder = decimal % 8   
        decimal = decimal // 8
        bString = str(remainder) + bString
    print("The Octal number is: ", bString)