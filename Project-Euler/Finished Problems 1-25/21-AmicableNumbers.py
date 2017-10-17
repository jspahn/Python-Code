# Project Euler
# Problem 21: Amicable numbers
#       Let d(n) be defined as the sum of proper divisors of n
#           (numbers less that n which divide evenly into n).
#           If d(a) = b and d(b) = a, where a != b, then a and b
#           are an amicable pair and each of a and b are called amicable
#           numbers.
#       For example, the proper divisors of 220 are:
#           1, 2, 4, 5, 10, 11, 20, 22, 44, 55, and 110;
#       therefore d(220) = 284.  The proper divisors of 284 are:
#           1, 2, 4, 71, 142; so d(284) = 220.
#
#       Evaluate the sum of all amicable numbers under 10 000
#

# Jeffrey Spahn
# Created for Python 3.x

import time


def divisor_sum(number):
    """Finds the divisors of the number and returns the sum of the numbers"""
    div_sum = 0
    divisors = []
    for div in range(1, int(number**0.5) + 1):
        if number % div == 0:
            divisors.append(div)
    for d in divisors:
        div_sum += d + number //d
    div_sum -= number
    return div_sum


# ------------------------------------------------------------
#  Main
# ------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()
    n = 10000

    to_check_number = [True] * (n+1)
    amicable_numbers = []
    am_sum = 0

    for i in range(1, n):
        if to_check_number[i]:
            a = divisor_sum(i)
            if i != a and i == divisor_sum(a):
                amicable_numbers.append((i, a))
                am_sum += i + a
            to_check_number[i] = False
            if a < n:
                to_check_number[a] = False

    print(amicable_numbers)
    print("Their total sum: {}".format(am_sum))
    print("    Completion time: {}".format(time.time() - start_time))

    # Output
    #     [(220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368)]
    #     Their total sum: 31626
    #         Completion time: 0.4639449119567871
