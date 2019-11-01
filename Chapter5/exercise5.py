"""
Heber Cooke 10/23/2019
Chapter 5 Exercise 5
This program takes an input number and a base number and converts the number to the 
representation of the number in that base
"""

#Dictionary conversion 
conversion = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, \
        "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

# function that returns a decimal number given a input number and a base number 
def repToDecimal(num,base):                                 
    number = 0                                                           
    ex = 0                                                                
    for i in range ((len(num)),0, -1):                                
        number += conversion[num[i-1]] * (int(base) ** ex)     
        ex += 1                                                          
     
    return number


def main():
    while True:
        num = input("Enter Q to quit,A for automatic or Enter a number: ").upper()
        if num == "Q" or num == "q":
            break
        elif num == "A" or num =="a":
            # test cases for automatic print out
            print("The A in base 16 is",repToDecimal("A",16))
            print("123 in base 4 is ", repToDecimal("123",4))
            print("777 in base 8 is ", repToDecimal("777",8))
            print("A7F in base 16 is ",repToDecimal("A7F",16))
            break
        else:           
            base = int(input("Enter a base: "))
            print(repToDecimal(num,base))

#Calling main 
main()