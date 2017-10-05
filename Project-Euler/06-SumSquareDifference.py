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

# sumOfSquares(n)
#       returns sum of the squares between 1 and n
def sumOfSquares(n):
    result = 0
    for i in range(n+1):
        result += pow(i,2)
    return result

# squareOfSums(n)
#       returns square of the sums between 1 and n
#       Uses the equation:
#           summation(i) = i*(i+1)/2
def squareOfSums(n):
    return pow(n*(n+1)/2,2)

maxValue = 100
solution = squareOfSums(maxValue) - sumOfSquares(maxValue)

print("The difference between the sum of squares and the square of sums of the"
      + " first one hundred natural numbers is " + str(solution))

# Output:
# The difference between the sum of squares and the square of sums of the first one hundred natural numbers is 25164150.0
