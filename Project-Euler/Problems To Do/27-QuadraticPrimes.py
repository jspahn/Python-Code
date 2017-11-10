# Project Euler
# Problem 27: Quadratic Primes
#     Euler discovered the remarkable quadratic formula:
#         n^2 + n + 41
#
#     It turns out that the formula will produce 40 primes for the
#     consecutive integer values 0 <= n <= 39. However, when
#     n = 40, 40^2 +40 + 41 = 40(40+1) + 41 is divisible by 41, and
#     certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
#
#     The incredible formula n^2 - 79n + 1601 was discovered, which
#     produces 80 primes for the consecutive values 0 <= n <= 79.
#     The product of the coefficients, -79 and 1601, is -126479.
#
#     Considering quadratics of the form:
#           n^2 + an + b, |a| < 1000 and |b| <= 1000
#           where |n| is the modulus/absolute value of n
#           e.g. |11| = 11 and |-4| = 4
#
#     Find the product of the coefficients, a and b, for the quadratic
#     expression that produces the maximum number of primes for
#     consecutive values of n, starting with n = 0

# Jeffrey Spahn
# Created for Python 3.x

import time


def get_primes(n):
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


# ------------------------------------------------------------
#  Main
# ------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()

    primes = get_primes(1000)
    solution = {
        "max": 0,
        "a":   0,
        "b":   0
    }

    for b in primes:
        for second_prime in primes:
            a = second_prime - b - 1
            n = 2
            while (n**2 + a*n + b) in primes:
                n = n+1
            if solution["max"] < n:
                solution["max"] = n
                solution["a"] = a
                solution["b"] = b

    print("n^2 + {}n + {}".format(solution["a"], solution["b"]))
    print("  creates the most primes: {}".format(solution["max"]))
    print("a * b = {}".format(solution["a"] * solution["b"]))

    print("Completion time: {}".format(time.time()-start_time))
    # Output:
    #     n^2 + -61n + 971
    #       creates the most primes: 61
    #     a * b = -59231
    #     Completion time: 0.10309195518493652
