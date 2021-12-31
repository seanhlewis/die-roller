# Simple die roller by Sean Lewis
# Uses Python's random and math library
import random
import math

choice = "y"
while "n" not in choice:
    choice = input("Would you like to roll the die? ")
    roll = math.floor(random.random() * 6) + 1
    print("You rolled a", roll)