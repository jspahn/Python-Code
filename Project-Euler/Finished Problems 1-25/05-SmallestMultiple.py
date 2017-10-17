# Project Euler
# Problem 5: Smallest Multiple
# Problem Details:
#         2520 is the smallest number that can be divided by each of the
#         numbers from 1 to 10 without any remainder.
#         What is the smallest positive number that is evening divisible
#         by all the numbers from 1 to 20?

# Jeffrey Spahn
# created for Python 3.x

import time


def product(l):
    """Returns the product of all values in l"""
    solution = 1
    for x in multipliers:
        solution = solution * x
    return solution


#------------------------------------------------------------
#  Brute Force Method
#------------------------------------------------------------
def find_multipliers(n):
    """Looks through all numbers between 2 through n and returns a list of
        the numbers divided by the Greatest common factor of all previous numbers.
        Example:
                n = 10 returns: [2,3,2,5,7,2,3]"""

    multipliers = [2]
    for i in range(2,n):
        for m in multipliers:
            if i%m == 0:
                i = int(i)/ int(m)
        if i !=1:
            multipliers.append(int(i))
    return multipliers

#------------------------------------------------------------
#  Primes Method
#------------------------------------------------------------

def primes(n):
    """Returns a list of prime numbers between 2 and n(inclusive)"""
    l_primes = [2]
    seive = [True]* (n+1)
    for i in range(3,n, 2):
        if seive[i]:
            l_primes.append(i)
            for j in range(2,int(n/i)+1):
                if i*j <= n:
                    seive[i*j] = False
    return l_primes

def prime_factorize_all_naturals(n):
    """Looks at each natural number between 1 and n(inclusive) and prime factorizes"""
    l_primes = primes(n)
    d_total_factorized = dict((p, 0) for p in l_primes)

    for p in l_primes:
        multiplied = p
        while multiplied <= n:
            d_total_factorized[p] += 1
            multiplied *= p

    return d_total_factorized

def power_dict(d):
    """Raises each key in the dictionary to the power of its value and multiplies all results together"""
    result = 1
    for key in list(d.keys()):
        result *= key ** d[key]
    return result

#------------------------------------------------------------
#  Main
#------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()

    # Brute Force
    n=20
    multipliers = find_multipliers(n)
    # print("Multipliers: {}".format(multipliers))
    solution = product(multipliers)
    print("The smallest multiple of all numbers from 1 to {0} is: {1}".format(n,solution))
    print("   Completion time: {}".format(time.time() - start_time))

    # Output:
    #   The smallest multiple of all numbers from 1 to 20 is: 232792560
    #      Completion time: 5.0067901611328125e-05


    # Primes Method
    start_time = time.time()
    d_factorized = prime_factorize_all_naturals(n)
    # print("Multipliers: {}".format(d_factorized))
    solution = power_dict(d_factorized)
    print("The smallest multiple of all numbers from 1 to {0} is: {1}".format(n,solution))
    print("   Completion time: {}".format(time.time() - start_time))

    # Output:
    #     The smallest multiple of all numbers from 1 to 20 is: 232792560
    #        Completion time: 5.1021575927734375e-05



