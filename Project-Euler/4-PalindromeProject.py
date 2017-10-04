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

# TODO complete Problem

# isPalindrome(n)
#       Tests to see if n is a palindrome
def isPalindrome(n):
    s = str(n)
    b_isP = True
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            b_isP = False
    return b_isP
