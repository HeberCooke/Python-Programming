"""
Heber Cooke 10/17/2019
Chapter 4 Exercise 7
This program takes in a coded input and converts the charactures to ascii
adds 1, and right shifts the bits and places it on the other side. It converts the bits back to ascii 
and prints the decoded message
"""
code = input("Enter the code: ")
print("Deciphered code is: ")
for i in code:
    charValue = ord(i) - 1
    binaryString = ''
    while charValue > 0:
        remander = charValue % 2
        charValue = charValue // 2
        binaryString = str(remander) + binaryString
    # bit wrap one place to the right
    num = binaryString
    shiftAmount = 1
    for i in range(0,shiftAmount):
        temp = num[len(num) -1]
        num = temp + num[0:len(num) -1]

    decimal = 0
    exponent = len(binaryString) - 1
    for digit in binaryString:
        decimal = decimal + int(digit) * 2 ** exponent
        exponent = exponent -1
    print(chr(decimal), end="")
print()