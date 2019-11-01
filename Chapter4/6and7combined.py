"""
Heber Cooke 10/17/2019
Chapter 4 Exercise 6
This program takes in a message converts the characters  to ascii, adds 1, and left shifts the bit and 
places it on the other side. It converts the bits back to ascii to print the code

"""

message = input("Enter a message: ")
word = message.split()  # splits the mesage into words list
print("The CODE: ",end=" ")
for i in message: # each word
    word = i
    for j in word:  # each letter
        charValue = ord(j) + 1 # adding 1 to the ascii value
        # convert decimal to binary
        binaryString = ''
        while charValue > 0:
            remander = charValue % 2
            charValue = charValue // 2
            binaryString = str(remander) + binaryString

        # bit wrap one place to the left
        #print(binaryString)
        num = binaryString
        shiftAmount = 1
        for i in range(0,shiftAmount):# shift Left
            temp = num[0]
            num = num[1:len(num)] + temp
       # print(num)
        # create the code from shifted bit string
        decimal = 0
        exponent = len(binaryString) - 1

    for digit in binaryString:
        decimal = decimal + int(digit) * 2 ** exponent
        exponent = exponent -1
    print(chr(decimal), end="")
print()    
        
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