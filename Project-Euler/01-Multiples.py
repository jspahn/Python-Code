# Project Euler
# Problem 1: Multiples of 3 and 5
# Problem Details:
#     If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
#     3, 5, 6, and 9.  The sum of these multiples is 23.
#     Find the sum of all the multiples fof 3 and 5 below 1000.
#

# Jeffrey Spahn
# created for Python 3.x
import time


def sum_of_multiples(n, divisors):
    """Returns the sum of all natural numbers below n that are divisible by divisors"""
    result = 0
    for x in range(1, n):
        if any([x % div == 0 for div in divisors]):
            result += x
    return result


if __name__ == "__main__":
    start_time = time.time()

    print("The sum of all multiples of 3 or 5 below 1000 is {}".format(sum_of_multiples(1000,[3,5])))
    print("Completion time: {}".format(time.time() - start_time))
    # Output:
    #      The sum of all multiples of 3 or 5 below 1000 is 233168
    #      Completion time: 0.0006198883056640625




