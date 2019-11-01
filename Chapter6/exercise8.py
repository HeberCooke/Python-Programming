""" 
Heber Cooke 10/29/2019
Chapter 6 Exercise 8
The function works as expected. It prints the sentence.
It works by printing the first letter of the sentance then setting the index to the next letter. It then recursivly calls the function
with the new starting index until there are no more indexes. 
The hidden cost running the function is with large inputs could start to take a very long time and use a lot of memory.

"""


count = 1
def printAll(seq, count):
    
    if seq:
        print("call #%2d" % (count), end=" ")
        print(seq[0], end=" ")    
        print("<-->%-25s" % (seq))
        count = count + 1
        printAll(seq[1:], count)
        
s = "The most awesome sentence"
#s = ["The","most","awsome","sentence"]

printAll(s, count)