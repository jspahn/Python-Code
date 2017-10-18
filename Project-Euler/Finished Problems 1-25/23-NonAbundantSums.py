# Project Euler
# Problem 23:  Non-abundant Sums
#       A perfect number is a number for which the sum of its proper
#       divisors is exactly equal to the number.  For example, the sum
#       of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
#       which means that 28 is a perfect number.
#
#       A number n is called deficient if the sum of its proper divisors
#       is less than n and it is called abundant if this sum exceeds n.
#
#       As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
#       the smallest number that can be writen as the sum of two abundant
#       numbers is 24.  By mathematical analysis, it can be shown that all
#       integers greater than 28123 can be written as the sum of two abundant
#       numbers.  However, this upper limit cannot be reduced any further by
#       analysis even though it is known that the greatest number that cannot
#       be expressed as the sum of two abundant numbers is less than this
#       limit.
#
#       Find the sum of all the positive integers which cannot be written
#       as the sum of two abundant numbers.

# Jeffrey Spahn
# Created for Python 3.x

import time
import itertools


def proper_divisors(n):
    """Returns the proper divisors of n"""
    prop_divs = [1]
    for i in range(2,int(n/2)+1):
        if n%i == 0:
            prop_divs.append(i)
    return prop_divs


def is_abundant(n):
    """returns True if n is an abundant number"""
    return sum(proper_divisors(n)) > n


# ------------------------------------------------------------
#  Main
# ------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()

    maximum_number = 28123

    sum_all = maximum_number* (maximum_number+1) /2
    s_abun = set()     # Set of all numbers that can be written as a sum of two abundant numbers

    l_abundant_numbers = []
    for number in range(2,maximum_number+1):
        if is_abundant(number):
            l_abundant_numbers.append(number)

    sum_options = itertools.combinations_with_replacement(l_abundant_numbers,2)

    for so in sum_options:
        if sum(so) <= maximum_number:
            s_abun.add(sum(so))

    print()
    print("            Number of Abundant Numbers between 1 and {0} : {1}".format(maximum_number, len(l_abundant_numbers)))
    print("                The Sum of all Numbers between 1 and {0} : {1}".format(maximum_number, sum_all))
    print("The Sum of all Numbers that are sums of 2 Abundant Numbers : {} ".format(sum(s_abun)))
    print("  The Sum of all Numbers not the sum of 2 Abundant Numbers : {} ".format(sum_all - sum(s_abun)))
    print()
    print("Completion time: {}".format(time.time()-start_time))

    # Output:
    #                 Number of Abundant Numbers between 1 and 28123 : 6965
    #                     The Sum of all Numbers between 1 and 28123 : 395465626.0
    #     The Sum of all Numbers that are sums of 2 Abundant Numbers : 391285755
    #       The Sum of all Numbers not the sum of 2 Abundant Numbers : 4179871.0
    #
    #     Completion time: 29.262778759002686
