"""
Heber Cooke 10/15/2019
Chapter 4 Exercise 5
Shift Right
 takes a binary input and shifts the RIGHT most bit and moves it to the LEFT most position 
"""
# Right shift 
num = input("Enter a binary number: ")
#shiftAmount = 2
shiftAmount = int(input("Enter a shift amount: "))

for i in range(0,shiftAmount):
    temp = num[len(num) -1]
    num = temp + num[0:len(num) -1]
print(num)

