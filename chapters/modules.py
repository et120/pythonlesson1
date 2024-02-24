# Modules: small code libraries that are based on related features
from math import pi #specific item
import sys
import random as rdm #alias
from enum import Enum
import kansas
from rps7 import rock_paper_scissors

print(pi)

for item in dir(rdm):
    print(item)

# using custom module
print(kansas.capital)
kansas.randomfunfact()

print(__name__)
print(kansas.__name__)

rock_paper_scissors()