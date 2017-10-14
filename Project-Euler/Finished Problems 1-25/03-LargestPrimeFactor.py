# Project Euler
# Problem 3: Largest Prime Factor
#       The prime factors of 13195 are 5, 7, 13 and 29.
#       What is the largest prime factor of the number 600851475143?


# Jeffrey Spahn
# created for Python 3.x

import time

def findNextPrime(lPrimes):
    """Looks for the next prime number to be added to the list
        Returns lPrimes with new prime appended to the end"""

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
    return lPrimes

def findLargestPrimeFactor(n):
    """Finds the largest Prime Factor of n"""

    lPrimes = [2, 3]  # List of prime numbers
    while n % 2 == 0:
        n /= 2
    while n % 3 == 0:
        n /= 2

    while n != 1:
        lPrimes = findNextPrime(lPrimes)
        while n % lPrimes[-1] == 0:
            n /= lPrimes[-1]

    return lPrimes[-1]

#------------------------------------------------------------
#  Main
#------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()
    testNumber = 600851475143


    solution = findLargestPrimeFactor(testNumber)

    print("The largest Prime Factor of {} is {}".format(testNumber,solution))
    print("Completion time: {}".format(time.time() - start_time))

    # Output:
    #   The largest Prime Factor of 600851475143 is 6857
    #   Completion time: 0.03122997283935547
