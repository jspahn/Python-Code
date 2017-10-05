# Project Euler
# Problem 10: Summation of Primes
#       The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
#       What is the sum of all the primes below two million

# Jeffrey Spahn
# Created for Python 3.x

lPrimes = [2,3]
sum = 5
while lPrimes[-1] < 2000000:
    testNumber = lPrimes[-1]
    b_isPrime = False
    while b_isPrime == False:
        testNumber += 2
        b_isPrime = True
        for p in lPrimes:
            if testNumber % p == 0:
                b_isPrime = False
                break
    lPrimes.append(testNumber)
    print(lPrimes[-1])
    sum += testNumber

sum -= testNumber
print("The sum of all primes between 1 and 2,000,000 is {}".format(sum))

# Output:
#       The sum of all primes between 1 and 2,000,000 is 142913828922