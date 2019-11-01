"""
Heber Cooke 10/24/2019
Chapter 5 Exercise 8
This program tracks the unique words in a file and there frequencies.
It prints the unique words and there frequencies in alphibetical order.
"""

fileName = input("Enter a file name: ")
f = open(fileName)  # opening the file 
s = f.read().split() #Spliting the file into words

dicto = {} 
for w in s:
    if dicto.__contains__ (w):
        dicto[w] += 1 # adding 1 to the count if the word is in the list       
    else:
        dicto[w] = 1 # ads the word and count 1 to the list

# sorts and prints the alphibetical list
for e in sorted(dicto.items()):
    print("%-9s%8s%6s" % (e[0] , e[1],"times" ))