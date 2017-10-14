# Project Euler
# Problem 4: Largest Palindrome Product
# Problem Details:
#         A Palindromic number reads the same both ways.  The largest
#         palindrome  made from the product of two 2-digit numbers is
#         9009 = 91 * 99
#         Find the largest palindrome made from the product of two
#         3-digit numbers.
#

# Jeffrey Spahn
# created for Python 3.x

import time

def isPalindrome(n):
    """ Tests to see if n is a palindrome
        Returns boolean"""
    s = str(n)
    b_isP = True
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            b_isP = False
    return b_isP

def findLargest_inRange(low_i,high_i, low_j, high_j):
    """ Searches for two natural numbers between the low and the high
        that when multiplied give a palindrome.
        returns a tuple of those two numbers"""
    result = (-1,-1)
    for i in range(low_i,high_i+1):
        for j in range(low_j,high_j+1):
            if isPalindrome(i*j) and i*j > result[0]*result[1]:
                result = (i,j)
    return result

#------------------------------------------------------------
#  Main
#------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()
    # Brute Force method:
    multipliers = findLargest_inRange(100,999, 100, 999)
    solution = multipliers[0] * multipliers[1]

    print("The Largest Palindrome made from the product of the two 3-digit numbers is: {}".format(solution))
    print("The two 3-digit numbers are: {} and {}".format(multipliers[0], multipliers[1]))
    print("Completion time: {}".format(time.time() - start_time))

    # Output:
    #     The Largest Palindrome made from the product of the two 3-digit numbers is: 906609
    #     The two 3-digit numbers are: 913 and 993
    #     Completion time: 1.4271514415740967



