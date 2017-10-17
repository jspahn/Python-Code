# Project Euler
# Problem 7: 10001st Prime
# Problem Details:
#         By listing the first six prime number: 2,3,5,7, 11 and 13, we can see
#         that the 6th prime is 13. What is the 10 001st prime?

# Jeffrey Spahn
# created for Python 3.x

import time

def find_prime(index):
    """Finds the prime number occurring at that index (the 3rd, 4th, 5th prime #, etc)"""
    if index == 1: return 2

    lPrimes = [2, 3]
    while len(lPrimes) < index:
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

    return str(lPrimes[-1])

#------------------------------------------------------------
#  Main
#------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()


    print("The 10 001st Prime number is {}".format(find_prime(10001)))
    print("   Completion time: {}".format(time.time() - start_time))
    # Output:
    #    The 10 001st Prime number is 104743
    #        Completion time: 3.5173330307006836
