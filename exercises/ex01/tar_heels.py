"""An exercise in remainders and boolean logic."""

__author__ = "730310198"


# Begin your solution here...
print("Enter an int")
user_input = input()
user_input = int (user_input)

if (user_input % 2 == 0) and (user_input % 7 == 0):
    print("TAR HEELS")
else:
    if user_input % 7 == 0:
        print("HEELS")
    else:
        if user_input % 2 == 0:
            print("TAR")
        else:
            print("CAROLINA")

