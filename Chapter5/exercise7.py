"""
Heber Cooke 10/24/2019
Chapter 5 Exercise 7

This program takes a text file and prints the unique words in alphibetical order 
"""
fileName = input("Enter the file name: ")
f = open(fileName)
s = f.read().split() #Spliting the file into words
d =[] #List for already seen words
for x in s:  # looping the empty list to check for used words
    if x not in d: #If word not used add the word to main list
        d.append(x)

d.sort() # sorting the main list
print(d)        