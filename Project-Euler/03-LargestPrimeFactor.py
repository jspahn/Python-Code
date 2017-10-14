# Project Euler
# Problem 3: Largest Prime Factor
#       The prime factors of 13195 are 5, 7, 13 and 29.
#       What is the largest prime factor of the number 600851475143?


# Jeffrey Spahn
# created for Python 3.x

import time

start_time = time.time()

testNumber = 600851475143

lPrimes = [2,3]  # List of prime numbers

# findNextPrime()
#       Appends the next prime number to the list lPrimes
def findNextPrime():
    i = lPrimes[-1]+2
    isPrime = False
    while isPrime == False:
        isPrime = True
        for p in lPrimes:
            if i % p == 0:
                isPrime = False
                i += 2
                break
    lPrimes.append(i)

# findLargestPrimeFactor(n)
#       Finds the largest prime factor of n
def findLargestPrimeFactor(n):
    while n % 2 == 0:
        n /= 2
    while n % 3 == 0:
        n /= 2

    while n != 1:
        findNextPrime()
        while n % lPrimes[-1] == 0:
            n /= lPrimes[-1]

    return lPrimes[-1]

solution = findLargestPrimeFactor(testNumber)

print("The largest Prime Factor of "+ str(testNumber) + " is"
      + " " + str(solution))

print("Completion time: {}".format(time.time() - start_time))

# Output:
#   The largest Prime Factor of 600851475143 is 6857
