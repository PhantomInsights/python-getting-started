"""
This file should only work on Python 3.6 and newer.
Its purpose is to test a correct installation of Python 3.
"""

from random import randint

print("Generating one thousand random numbers...")

for i in range(1000):

    random_number = randint(0, 100000)
    print(f"Number {i} was: {random_number}")
