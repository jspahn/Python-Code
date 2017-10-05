# Project Euler
# Problem 10: Summation of Primes
#       The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
#       What is the sum of all the primes below two million

# Jeffrey Spahn
# Created for Python 3.x

import time

Start_time = time.time()

# primes(n)
#       List all primes up to n using Sieve of Eratosthenes Algorithm
def primes(n):
    l_primes = [2]
    sieve = [True] * (n+1)
    for i in range(3,n,2):
        if sieve[i]:
            l_primes.append(i)
            for j in range(2,int(n/i)):
                sieve[i*j] = False
    return l_primes


print(sum(primes(2000000)))

print(time.time() - Start_time)

