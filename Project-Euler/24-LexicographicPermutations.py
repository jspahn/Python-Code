# Project Euler
# Problem 24: Lexicographic Permutations
#       A permutation is an ordered arragement of objects.  For example,
#       3124 is one possible permutations of the digits 1, 2, 3, and 4.
#       If all the permutations are listed numerically or alphabetically,
#       we call it lexicographic order.  The lexicographic permutations
#       of 0, 1, and 2 are:
#                012,  021,  102,  120,  201,  210
#
#       What is the millionth lexicographic permutation of the digits
#       0, 1, 2, 3, 4, 5, 6, 7, 8, and 9?

# Todo

# Jeffrey Spahn
# Created for Python 3.x

import time

start_time = time.time()


# There are 10! permutations.  9! permutations start with 0

def factorial(n):
    product = 1
    for i in range(1,n+1):
        product *= i
    return product



print("Completion time: {}".format(time.time()-start_time))