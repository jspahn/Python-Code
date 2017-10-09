# Project Euler
# Problem 12: Highly Divisible Triangular Number
#         The sequence of triangle numbers is generated by adding the natural numbers.
#         So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
#         The first ten terms would be:
#         1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#         Let us list the factors of the first seven triangle numbers
#           1:  1
#           3:  1, 3
#           6:  1, 2, 3, 6
#           10: 1, 2, 5, 10
#           15: 1, 3, 5, 15
#           21: 1, 3, 7, 21
#           28: 1, 2, 4, 7, 14, 28
#         We can see that 28 is the first triangle number to have over five divisors.
#         What is the value of the first triangle number to have over five hundred
#         divisors?

# Jeffrey Spahn
# Created for Python 3.x

# triangle numbers  y = (x^2 + x)/2 = (x)(x+1)/ 2   <<<-- this means triangle numbers can't be prime
# TODO
import time
import itertools


# findPrimes(n)
#   returns the list of primes from 2 to n
def primes(n):
    sieve = [True] * n
    l_primes = [2]
    if n >= 5:
        for i in range(3,n,2):
            if sieve[i]:
                l_primes.append(i)
                for j in range(2,int(n/i)):
                    sieve[i*j] = False
    else:
        l_primes.append(3)
    return l_primes


# l_primes_100mill = primes(100000000)
# prime_factorize(n)
#       returns a list of the exponents of the prime factorization of a number
#          Example:   700 = 2^2 * 3^0 * 5^2 * 7^1
#             Will return [2,0,2,1]
#
def prime_factorize(n):
    if n < 5:
        l_primes = primes(n)
    else:
        l_primes = primes(int(n/2)+1)

    # l_primes = l_primes_100mill
    # print("The List of Prime Numbers : {}:".format(l_primes))
    result = [0] * len(l_primes)
    for i in range(len(l_primes)):
        while(n % l_primes[i] == 0):
            result[i] +=1
            n = int(n/l_primes[i])
        if n == 1:
            return result

    return result


# numberOfDivisors(l_degeneracy)
#       l_degeneracy: list of degeneracy for primes needed to create number
#           example:  3500 = 2^2 * 5^3 * 7^1
#                          l_degeneracy = [2,3,1]
#                   result = 2^0 * [      (2-1)(3-1)(1-1)               ]
#                          + 2^1 * [(2-1)(3-1) + (2-1)(1-1) + (3-1)(1-1)]
#                          + 2^2 * [(2-1)      + (3-1)      + (1-1)     ]
#                          + 2^3
#                             = 0 + 4 + 8 + 12
#                             = 24

def numberOfDivisors(l_degeneracy):
    l_degeneracy = list(filter((0).__ne__, l_degeneracy))
    n_unique_primes = len(l_degeneracy)  # The number of unique primes (in example this would be 3
    result = 0
    base_coefficients = [ x-1 for x in l_degeneracy]
    for i in range(n_unique_primes+1):
        coeff = 0
        # print("Now looking at combinations of size {}".format(i))
        for subset in itertools.combinations(base_coefficients,i):
            # print("   Subset: {}".format(subset))
            inner_coeff = 1
            for j in range(i):
                inner_coeff *= subset[j]
            coeff += inner_coeff
            # print("   InnerCoeff: {}".format(inner_coeff))
            # print("        Coeff: {}".format(coeff))
        # print("   2^{} * {} = {}".format(n_unique_primes - i,coeff, 2**(n_unique_primes - i) * coeff))
        result += 2**(n_unique_primes - i) * coeff
    print("Number of Divisors: {}".format(result))
    return result

#
# overallTimeStart = time.time()
# i = 1
# test_number = 0
# b_continue = True
# while b_continue:
#     startTimeLoop = time.time()
#     # Step 1: calculate triangle number
#     test_number = test_number + i
#     print("============================================")
#     print("Testing Triangle Number ({}): {}".format(i,test_number))
#     # Step 2: Prime Factorize
#     startTimePrime = time.time()
#     l_prime = prime_factorize(test_number)
#     print("Time to Factorize: {}".format(time.time() - startTimePrime))
#
#     # print("The Prime Factorization is: {}".format(l_prime))
#     # Step 3: get Number of Divisors
#     # Step 4: if number of divisors is >=500, quit
#     startTimeDiv = time.time()
#     if sum(l_prime) < 9 and numberOfDivisors(l_prime) >= 500:
#         b_continue = False
#     else:
#         i += 1
#     print("Time to find Number of Divisors: {}".format(time.time() - startTimeDiv))
#     print("Time for full loop: {}".format(time.time() - startTimeLoop))
#     print("Overall Time Thus far: {}".format(time.time() - overallTimeStart))




# New Strategy
#   Step 1:  Assume all the prime numbers needed to create the correct answer can be found in the first 20 primes
#            Justification: if we have 1 instance of each prime number in order, we only need the first
#               9 primes to get over
#               500 factors
#   Step 2:  Test number of Divisors for all numbers
#
# n = 10      # number of primes we'll be testing
# d = 10      # degeneracy of each prime
# list_of_primes = [0] * n
# list_of_500divisors = []
# for i in range(n):
#     for j in range(d):
#         list_of_primes[i] += 1
#         if numberOfDivisors(list_of_primes) >= 500:
#             list_of_500divisors.append(list_of_primes)
#
# print("We found {} instances of 500+ divisors".format(len(list_of_500divisors)))
#
# prime_values = primes(50)
# for number in list_of_500divisors:
#     y = 1
#     for i in range(n):
#         y *= prime_values[i] ** number[i]
#     print(number)
#     print(y)
#     x = (0.25 + 2 * y)**0.5 - 0.5
#     print(x)
#     if x%1.0 == 0.0:
#         print("----------SOLUTION!!!!!--------")
#


def testTriangle(y):
    return ((2*y + 0.25)**0.5 - 0.5) % 1.0 == 0.0

def primeToNumber(l):
    p = [2,3,5,7,11,13,17,19,23,29]  # first 10 primes
    result = 1
    for i in range(10):
        result *= p[i]**l[i]
    return result


n = 10
list_of_primes = [0] * n
list_of_primes[0] = 500

success_pile = []
if testTriangle(primeToNumber(list_of_primes)):
    print("Success!: {}".format(list_of_primes))
    success_pile.append(list_of_primes)

for i in range(5):
    list_of_primes[0] = int(list_of_primes[0] / 2)
    list_of_primes[i+1] += 1
    if testTriangle(primeToNumber(list_of_primes)):
        print("Success!: {}".format(list_of_primes))
        success_pile.append(list_of_primes)
