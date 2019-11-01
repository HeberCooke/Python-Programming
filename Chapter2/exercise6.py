"""
Heber Cooke 10/3/2019
Chapter 2 Exercise 6

This program Calculates the kinetic energy of a moving object

The program takes objects mass, its velosity and
outputs the objects kinetic energy and its mass
"""

mass = float(input("Enter the mass in kg "))
velosity = int(input("Enter the velocity in meters pr second "))
kineticEnergy = 0.5 * mass * velosity **2
print("Momentum is ",mass * velosity)
print("Kinetic Energy is ",kineticEnergy)
