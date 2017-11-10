# Project Euler
# Problem 26: Reciprocal cycles
#         A unit fraction contains 1 in the numerator. The decimal representation
#         of the unit fractions with denominators 2 to 10 are given:
#
#           1/2	= 	0.5
#           1/3	= 	0.(3)
#           1/4	= 	0.25
#           1/5	= 	0.2
#           1/6	= 	0.1(6)
#           1/7	= 	0.(142857)
#           1/8	= 	0.125
#           1/9	= 	0.(1)
#           1/10	= 	0.1
#
#         Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
#         It can be seen that 1/7 has a 6-digit recurring cycle.
#
#         Find the value of d < 1000 for which 1/d contains the longest
#         recurring cycle in its decimal fraction part.


# Jeffrey Spahn
# Created for Python 3.x

import time
from decimal import *


def is_recurring(d):
    """Looks at the fraction 1/d and returns True if its decimal representation is a recurring cycle"""
    if d % 2 == 0 or d % 5 == 0:
        return False
    else:
        return True


def recurring_length(d):
    """Looks at the fraction 1/d and returns the length of the recurring cycle.
        Every Fraction of the form 1/d that has a recurring cycle can be made into the form:
                        X/(10^i - 1)
        where X is the recurring digits and i is the number of digits that recurs.

        Example:    1/3 =  0.(3)      = 3/9
                    1/7 =  0.(142857) = 142857/999999
        To reverse this process, we simply find the value for i such that (10^i - 1) mod d == 0
        """
    if is_recurring(d):
        b_found = False
        i = 1
        while True:
            if (10**i-1) % d == 0:
                return i
            else:
                i = i+1
    else:
        return 0
    pass

# ------------------------------------------------------------
#  Main
# ------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()

    largest_recurring_length = 0
    largest_d = 0
    for d in range(2,1000):
        r_length = recurring_length(d)
        if r_length > largest_recurring_length:
            largest_recurring_length = r_length
            largest_d = d

    print("The fraction 1/{} has the largest recurring cycle of {} repeating digits.".format(largest_d,largest_recurring_length))
    print("Completion time: {}".format(time.time()-start_time))
    # Output:
