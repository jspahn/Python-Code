# Project Euler
# Problem 32: Pandigital Products
#           We shall say that an n-digit number is pandigital if it makes use
#           of all the digits 1 to n exactly once; for example, the 5-digit number,
#           15234, is 1 through 5 pandigital.
#
#           The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
#           multiplicand, multiplier, and product is 1 through 9 pandigital.
#
#           Find the sum of all products whose multiplicand/multiplier/product identity
#           can be written as a 1 through 9 pandigital.
#
#           HINT: Some products can be obtained in more than one way so be sure to only
#           include it once in your sum.

# Jeffrey Spahn
# Created for Python 3.x

import time
import math


def num_of_digits(test_number):
    """Finds the number of digits in the test_number (log base 10 of number + 1)"""
    return int(math.log(test_number,10))+1


def is_pandigital(test_numbers, digit_length):
    total_num_digits = 0
    test = []
    for tn in test_numbers:
        total_num_digits += num_of_digits(tn)
        test.extend([int(x) for x in str(tn)])
    if total_num_digits != digit_length:
        return False

    test.sort()
    digits = list(range(1,digit_length+1))
    if test == digits:
        return True
    return False


# ------------------------------------------------------------
#  Main
# ------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()

    l_poss_sol = []
    for a in range(1,9999+1):
        for b in range(1,pow(10,5 - num_of_digits(a))):
            ab = a * b
            tot_num_digits = num_of_digits(a) + num_of_digits(b) + num_of_digits(ab)
            if tot_num_digits > 9:
                break
            if tot_num_digits == 9:
                l_poss_sol.append([a, b, ab])

    l_products = []
    for poss in l_poss_sol:
        if is_pandigital(poss,9):
            l_products.append(poss[2])
    l_products = list(set(l_products))

    print("The Sum of all the products is {}".format(sum(l_products)))
    print("Completion time: {}".format(time.time() - start_time))

    # Output:
    #       The Sum of all the products is 45228
    #       Completion time: 0.7163009643554688