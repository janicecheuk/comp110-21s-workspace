"""A vaccination calculator."""

__author__ = "730310198"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

print("Population:")
pop_input = input()
pop_input = int (pop_input)

print("Doses administered:")
dose_admin = input()
dose_admin = int (dose_admin)

print("Doses per day:")
dose_day = input()
dose_day = int (dose_day)

print("Target percent vaccinated:")
target = input()
target = int (target)

target = (target/100)

amount: int = ((2 * (target * pop_input)) - dose_admin)//dose_day

days_since_today: int = abs(amount)

fortnight = timedelta(days_since_today)
today: datetime = datetime.today()

future: datetime = today + fortnight

target = round(target * 100)
days: int = round(days_since_today) 
print("We will reach " + str(target) + "% vaccination in " + str(days) + " days, which falls on " + future.strftime("%B %d, %Y") + ".")


