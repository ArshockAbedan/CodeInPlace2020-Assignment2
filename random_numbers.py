"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random

NUM_RANDOM = 10
MIN_RANDOM = 0
MAX_RANDOM = 100


def main():
    """
    This program prints NUM_RANDOM i.e. 10 random integers. It uses a constant named NUM_RANDOM, which determines the
    number of random numbers to print (with a value of 10). It also uses constants named MIN_RANDOM and MAX_RANDOM
    to determine the minimal and maximal values of the random numbers generated (with respective values 0 and 100).
    """
    for i in range(NUM_RANDOM):
        print(random.randint(MIN_RANDOM, MAX_RANDOM))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
