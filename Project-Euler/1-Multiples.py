# Project Euler
# Problem 1: Multiples of 3 and 5
# Problem Details:
#     If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
#     3, 5, 6, and 9.  The sum of these multiples is 23.
#     Find the sum of all the multiples fof 3 and 5 below 1000.
#

# Jeffrey Spahn
# created for Python 3.x

result = 0
for x in range(1,1000):
    if x%3 == 0 or x%5 == 0:
        result += x


print("The sum of all multiples of 3 or 5 below 1000 is " + str(result))

# Solution calculated is 233168