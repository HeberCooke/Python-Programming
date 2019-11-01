"""
Heber Cooke 10/20/2019
Chapter 5 Exercise 3

Generating Sentences modified Case Study 5.3
"""
import random

#Function to get words from file 
def getWords(fileName):
    temp = open(fileName, "r").read().split()
    return temp

#Calling the function with the file name as argument
articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")

def sentance():
    """ Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase() + "."

def nounPhrase():
    """Builds and returns a noun phrase"""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase"""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase"""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """ Allows the user to input the number of sentaances to generate."""
    number = int(input("Enter a nummber of sentences: "))
    
    for count in range(1,number + 1):
        print("#" + str(count) + " " + sentance())
       

main()