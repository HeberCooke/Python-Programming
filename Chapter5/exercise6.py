"""
Heber Cooke 10/24/2019
Chapter 5 Exercise 6

This program takes a number and converts it to base 10
"""
conversion = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, \
        "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

def decimalToRep(num,base): 
    s = 0
    ex = len(num) -1

    for digit in num:
        digit = int(conversion.get(digit))
        s = s + int(digit) * int(base) ** ex   
        ex = ex -1

    return(s)

def main():
    while True:
        number = input("Enter Q to quit, Enter A for automatic, Enter a number: ").upper()
        # fancy print format for the output
        if number == "A" or number =="a":
            print("%-20s%-8s%-9s" % ("65F6 base 16 is:",decimalToRep("65F6",16), "Base 10"))
            print("%-20s%-8s%-9s" % ("876 base 8 is:", decimalToRep("876",8), "Base 10"))
            print("%-20s%-8s%-9s" % ("76543 base 7 is:", decimalToRep("76543",7), "Base 10"))
            print("%-20s%-8s%-9s" % ("654 base 6 is:", decimalToRep("654",6), "Base 10"))
            print("%-20s%-8s%-9s" % ("543 base 5 is:", decimalToRep("543",5), "Base 10"))
            print("%-20s%-8s%-9s" % ("432 base 4 is:", decimalToRep("432",4), "Base 10"))
            print("%-20s%-8s%-9s" % ("3212 base 3 is:", decimalToRep("3212",3), "Base 10"))
            print("%-20s%-8s%-9s" % ("1011110 base 2 is:", decimalToRep("1011110",2), "Base 10"))

        elif number =="Q" or number =="q":
            break
        else:
            base = input("Enter a base: ")
            print(decimalToRep(number,base))
main()