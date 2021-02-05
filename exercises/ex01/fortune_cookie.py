"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730310198"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")

lowerBound: int = 0
upperBound: int = 4
randomNumber: int = randint(lowerBound, upperBound)


if randomNumber == 0:
    print("You will see a cute dog today.")
else:
    if randomNumber == 1:
        print("You will find $20 today.")
    else:
        if randomNumber == 2: 
            print("Soon life will become more interesting.")
        else:
            if randomNumber == 3:
                print("You will get free food today.")
            else:
                if randomNumber == 4:
                    print("You will win your next league of legends game.")

print("Now, go spread positive vibes!")