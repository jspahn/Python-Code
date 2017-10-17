# Project Euler
# Problem 20:  Factorial Digit Sum
#       n! means n * (n-1) * ... * 3 * 2 * 1
#       For example:
#           10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
#       and the sum of the digits in the number 10! is:
#           3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
#       Find the sum of the digits in the number 100!

# Jeffrey Spahn
# Created for Python 3.x

import time


def factorial(n):
    """Calculates n factorial: n!"""
    result = 1
    for i in range(1,n+1):
        result *= i
    return result


# ------------------------------------------------------------
#  Main
# ------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()

    n = 100
    s = str(factorial(n))

    digit_sum = 0
    for i in s:
        digit_sum += int(i)

    print("{0}! = {1}".format(n, s))
    print("The Sum of Digits = {}".format(digit_sum))

    print("Completion time: {}".format(time.time()-start_time))

    # Output:
    #     100! = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
    #     The Sum of Digits = 648
    #     Completion time: 9.202957153320312e-05