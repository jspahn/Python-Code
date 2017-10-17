# Project Euler
# Problem 10: Summation of Primes
#       The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
#       What is the sum of all the primes below two million

# Jeffrey Spahn
# Created for Python 3.x

import time

def primes(n):
    """Lists all primes from 2 to n (inclusive)
            Uses Sieve of Erathosthenes Algorithm"""
    l_primes = [2]
    sieve = [True] * (n+1)
    for i in range(3,n,2):
        if sieve[i]:
            l_primes.append(i)
            for j in range(2,int(n/i)+1):
                if i*j<=n:
                    sieve[i*j] = False
    return l_primes

#------------------------------------------------------------
#  Main
#------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()

    n = 2000000
    l_primes = primes(n)
    print("The Sum of all primes less than {0} is {1}".format(n,sum(l_primes)))

    print("   Completion time: {}".format(time.time() - start_time))
    # Output:
    #     The Sum of all primes less than 2000000 is 142913828922
    #        Completion time: 1.1524379253387451


