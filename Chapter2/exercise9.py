"""
Heber Cooke 10/3/2019
Chapter 2 exercise 9

A program that takes an input of kolometers and prints
the number of nautical miles

gets input of kilometers
gets conversion from degrees * miniuts of arc
gets miles from kilometers * conversion divide 1/10000th
prints number of miles

"""
kilometers  = float(input("Enter Kilometers "))
conversion = 90 * 60  # deg * min of arc
miles = (kilometers * conversion)/10000 # 1/10000 distance

print(miles,"Number of Nautical Miles")
