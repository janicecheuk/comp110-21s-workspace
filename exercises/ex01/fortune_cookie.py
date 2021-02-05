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

lower_bound: int = 0
upper_bound: int = 4
random_number: int = randint(lower_bound, upper_bound)


if random_number == 0:
    print("You will see a cute dog today.")
else:
    if random_number == 1:
        print("You will find $20 today.")
    else:
        if random_number == 2: 
            print("Soon life will become more interesting.")
        else:
            if random_number == 3:
                print("You will get free food today.")
            else:
                if random_number == 4:
                    print("You will win your next league of legends game.")

print("Now, go spread positive vibes!")