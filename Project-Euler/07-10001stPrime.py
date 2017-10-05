# Project Euler
# Problem 7: 10001st Prime
# Problem Details:
#         By listing the first six prime number: 2,3,5,7, 11 and 13, we can see
#         that the 6th prime is 13. What is the 10 001st prime?

# Jeffrey Spahn
# created for Python 3.x

lPrimes = [2,3]

while len(lPrimes) < 10001:
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
    # print("Prime #"+ str(len(lPrimes)) + " is " + str(lPrimes[-1]))

solution = str(lPrimes[-1])

print("The 10 001st Prime number is " + solution)

# Output:
#   The 10 001st Prime number is 104743
