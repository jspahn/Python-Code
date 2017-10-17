# Project Euler
# Problem 24: Lexicographic Permutations
#       A permutation is an ordered arrangement of objects.  For example,
#       3124 is one possible permutations of the digits 1, 2, 3, and 4.
#       If all the permutations are listed numerically or alphabetically,
#       we call it lexicographic order.  The lexicographic permutations
#       of 0, 1, and 2 are:
#                012,  021,  102,  120,  201,  210
#
#       What is the millionth lexicographic permutation of the digits
#       0, 1, 2, 3, 4, 5, 6, 7, 8, and 9?

# Jeffrey Spahn
# Created for Python 3.x

# This project was done two different methods:
#       Method 1: Brute force
#                 Used itertools.permutations to find all permutations and got 1000,000th entry
#       Method 2: Mathematical
#                 Used factorials to determine each digit one at a time
#                   Example:  there are 9! permutations starting with 0.
#                             9! = 362880 < 999,999 so we know the 1,000,000th entry can't start with a 0

import time
import itertools


# ------------------------------------------------------------
#  Brute Force Methods
# ------------------------------------------------------------
def get_lexicographic_order(digits):
    return sorted([a for a in itertools.permutations(digits,len(digits))])


def get_lex_brute(digits, n):
    """Gets the 'n'th permutation in lexicographic order
            n starts at 1"""
    lexi = get_lexicographic_order(digits)

    # return lexi[n-1]
    result = ""
    for i in range(len(digits)):
        result += str(lexi[n - 1][i])

    return result


# ------------------------------------------------------------
#  Factorial Methods
# ------------------------------------------------------------
def get_lex_factorial_method(digits, n):
    digits = list(digits)
    lexicographic_position = n - 1  # Ordering starts at 0

    factorials = [1]
    for i in range(2,len(digits)):
        factorials.append(factorials[-1] * i)
    factorials.reverse()

    solution = ""
    # digit_options = [0,1,2,3,4,5,6,7,8,9]
    for digit_position in range(len(factorials)):
        index = lexicographic_position // factorials[digit_position]
        solution += str(digits[index])
        digits.pop(index)
        lexicographic_position = lexicographic_position - (index * factorials[digit_position])

    solution += str(digits[0])
    return(solution)


# ------------------------------------------------------------
#  Main
# ------------------------------------------------------------
if __name__ == "__main__":

    print("Performing Calculation using Brute Force Method")
    start_time = time.time()
    lexicographic_position = 1000000                      # Starts at 1
    lexi = get_lex_brute("0123456789", lexicographic_position)
    print("Lexicographic #{} : {}".format(lexicographic_position, lexi))
    print("Completion time: {}".format(time.time() - start_time))

    # Output:
    #      Performing Calculation using Brute Force Method
    #      Lexicographic #1000000 : 2783915460
    #      Completion time: 1.2334587574005127



    print()
    print("Performing Calculation using Mathematical Method")
    start_time = time.time()
    lexicographic_position = 1000000                      # Starts at 1
    lexi = get_lex_factorial_method("0123456789", lexicographic_position)
    print("Lexicographic #{} : {}".format(lexicographic_position, lexi))
    print("Completion time: {}".format(time.time() - start_time))
    # Output:
    #      Performing Calculation using Mathematical Method
    #      Lexicographic #1000000 : 2783915460
    #      Completion time: 1.9073486328125e-05



