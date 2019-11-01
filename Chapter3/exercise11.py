"""
Heber Cooke 10/10/2019  
Chapter 3 Exercise 11

Lucky Sevens Game   
If the dice total 7 the player gets $4 
if the dice not 7 the player loses  $1

The program takes a imput of the total amount to play
Rolls the dice until the amount is 0
prints the number of rolls it took to get to 0
prints the max amount in the pot at its greatest
prints losses and wins count
"""
import random

credit = int(input("Enter an amount to play: "))
rolls = 0
total = 0
timesWon = 0
timesLoss = 0
while credit > 0:

    #run = input("press any key to play")
    dice1 =  random.randint(1, 6)
    dice2 =  random.randint(1, 6)
    rolls += 1
    print(dice1," ", dice2)
    #
    if(dice1 + dice2 == 7):
        credit += 4 # adds $4 to player win
        print("Win! $4")
        timesWon +=1
        if credit > total:
            total = credit
    else:
        credit -= 1 # subtracts $1 loss
        print("Lose $1")
        timesLoss += 1
print()
print("%-13s" % "Highest Won $",total)
print("%-13s" % "Rounds", rolls)
print("%-13s" % "WON ",timesWon, "times")
print("%-13s" % "LOSS ",timesLoss, "times")