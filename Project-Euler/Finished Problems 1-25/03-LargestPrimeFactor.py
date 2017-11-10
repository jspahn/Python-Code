# Project Euler
# Problem 3: Largest Prime Factor
#       The prime factors of 13195 are 5, 7, 13 and 29.
#       What is the largest prime factor of the number 600851475143?


# Jeffrey Spahn
# created for Python 3.x

import time


def find_next_prime(l_primes):
    """Looks for the next prime number to be added to the list
        Returns lPrimes with new prime appended to the end"""

    i = l_primes[-1]+2
    is_prime = False
    while not is_prime:
        is_prime = True
        for p in l_primes:
            if i % p == 0:
                is_prime = False
                i += 2
                break
    l_primes.append(i)
    return l_primes


def find_largest_prime_factor(n):
    """Finds the largest Prime Factor of n"""

    l_primes = [2, 3]  # List of prime numbers
    while n % 2 == 0:
        n /= 2
    while n % 3 == 0:
        n /= 2

    while n != 1:
        l_primes = find_next_prime(l_primes)
        while n % l_primes[-1] == 0:
            n /= l_primes[-1]

    return l_primes[-1]


# ------------------------------------------------------------
#  Main
# ------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()
    testNumber = 600851475143

    solution = find_largest_prime_factor(testNumber)

    print("The largest Prime Factor of {} is {}".format(testNumber,solution))
    print("Completion time: {}".format(time.time() - start_time))

    # Output:
    #   The largest Prime Factor of 600851475143 is 6857
    #   Completion time: 0.03122997283935547
