# Project Euler
# Problem 6: Sum Square Difference
#         The Sum of the squares of the first ten natural numbers is,
#         1^2 + 2^2 + ... + 10^2 = 385
#         The square of the sum of the first ten natural numbers is,
#         (1 + 2 + ... + 10)^2 = 55^2 = 3025
#         Hence the difference between the sum of the squares of the
#         first ten natural numbers and square of the sum is 3025 - 385 = 2640.
#         Find the difference between th sum of the squares of the first one
#         hundred natural numbers and the square of the sum.

# Jeffrey Spahn
# Created for Python 3.x

import time



def sumOfSquares(n):
    """Returns the Sum of the Squares between 1 and n(inclusive)"""
    result = 0
    for i in range(n+1):
        result += pow(i,2)
    return result

def squareOfSums(n):
    """Returns Square of the Sum between 1 and n(inclusive)
            Uses Equation: Sum(i) = i*(i+1)/2"""
    return pow(n*(n+1)/2,2)

#------------------------------------------------------------
#  Main
#------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()


    maxValue = 100
    solution = squareOfSums(maxValue) - sumOfSquares(maxValue)

    print("The difference between the sum of squares and the square of sums of the"
          + " numbers 1 to {0} is {1} ".format(maxValue,solution))
    print("   Completion time: {}".format(time.time() - start_time))

    # Output:
    #    The difference between the sum of squares and the square of sums of the numbers 1 to 100 is 25164150.0
    #         Completion time: 9.393692016601562e-05