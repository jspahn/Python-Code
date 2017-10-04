# Project Euler
# Problem 5: Smallest Multiple
# Problem Details:
#         2520 is the smallest number that can be divided by each of the
#         numbers from 1 to 10 without any remainder.
#         What is the smallest positive number that is evening divisible
#         by all the numbers from 1 to 20?

# Jeffrey Spahn
# created for Python 3.x


# findPrimes(maxValue)
#     returns list of all prime numbers between 1 and maxValue (inclusive)

def findPrimes(maxValue):
    if maxValue < 2:
        return []
    primes = [2]
    i = 3
    while i < maxValue+1:
        isPrime = True
        for p in primes:
            if i % p == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
        i +=1

    return primes

#   findSmallestMultiple(n)
#       finds smallest multiple of all numbers from 1 to n
def findSmallestMultiple(n):
    primes = findPrimes(n)

    result =1
    for p in primes:
        result*= p

    return result


print("The smallest multiple of all numbers from 1 to 20 is:"
      + str(findSmallestMultiple(20)))
