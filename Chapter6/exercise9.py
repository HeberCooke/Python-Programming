"""
Heber Cooke  10/31/2019
Chapter 6 Exercise 9
Write a program that computes and prints the average of of the numbers in a text file.
You should make use of two higher-order functions to simplify the design.
"""
import random

inpu = input("Enter a file name or C to create one ")
if inpu == 'C' or inpu == 'c': # create a txt file 
    f = open("numbers.txt",'w')
    for i in range(100):    # put 100 random integers in the txt file
        f.write(str(random.randint(1,100)))
        f.write(' ')
    f.close() #close the file
    f = open('numbers.txt', 'r')#open the created file for reading
else: 
    f = open(inpu, 'r')


s = f.read().split()
f.close()
def total(s):
    n = 0
    for i in s:
        n += int(i)
    return n

def count(s):
    return len(s)

def average(t, c):
    return  t / c 
t = total
c = count
a = average


print("Total",t(s))
print("Count",c(s))
print("Average", a(t(s),c(s)))