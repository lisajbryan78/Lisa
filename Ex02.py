"""Calculator Program Assignment"""

import math

# display Calculator Program title
from decimal import Decimal

print("\n-------------------------------------------------")
print("*Number of Terms for Investment Calculator*")
print("---------------------------------------------------")

# user input
PV = Decimal(input("Please enter PV: "))
FV = Decimal(input("Please enter FV: "))
r = Decimal(input("Please enter r: "))

# calculate n
n = math.log(FV/PV)/math.log(1 + r)  # you would insert the function shown in the exercise

# display results
print(f"\n The number of terms required for an initial investment of {PV} with a rate of {r} to appreciate to {FV} "
      f"is {n}.")

# say thank you
print("\n Thank You")
