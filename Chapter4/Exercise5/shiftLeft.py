"""
Heber Cooke 10/15/2019
Chapter 4 Exercise 5
Shift Left
takes a binary input and shifts the LEFT most bit and moves it to the RIGHT most position 
"""
# shift Left
num = input("Enter a binary number: ")
#shiftAmount = 2
shiftAmount = int(input("Enter a shift amount: "))

for i in range(0,shiftAmount):
    temp = num[0]
    num = num[1:len(num)] + temp
print(num)