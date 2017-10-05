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

# isPalindrome(n)
#       Tests to see if n is a palindrome
def isPalindrome(n):
    s = str(n)
    b_isP = True
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            b_isP = False
    return b_isP

# findLargest_inRange(low, high)
#       searches for two natural numbers between the low and the high
#       that when multiplied give a palindrome.
#       returns a tuple of those two numbers
def findLargest_inRange(low_i,high_i, low_j, high_j):
    result = (-1,-1)
    for i in range(low_i,high_i+1):
        for j in range(low_j,high_j+1):
            if isPalindrome(i*j) and i*j > result[0]*result[1]:
                result = (i,j)
    return result

# Brute Force method:
solution = findLargest_inRange(100,999, 100, 999)
print(str(solution))
print(str(solution[0]*solution[1]))

# Output:
#       (913, 993)
#       906609

