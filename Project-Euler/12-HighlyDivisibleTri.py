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

# triangle numbers  y = (x^2 + x)/2 = (x)(x+1)/ 2
#             By looking at this, we know triangle numbers are not prime.
#           We can find triangle numbers by finding x and x+1
#           x and x+1 must have a unique set of prime numbers in their prime factorization.
#
import time


def factorize(n):
    l_factors = []
    count = 0
    divisor = 2
    while n%divisor == 0:
        n = n/divisor
        count += 1
    l_factors.append(count)
    divisor = 3
    while n > 1:
        count = 0
        while n % divisor == 0:
            n = n / divisor
            count += 1
        l_factors.append(count)
        divisor += 2
    return l_factors


def numberOfDivisors_v2(l_degeneracy):
    result = 1
    for p in l_degeneracy:
        result = result * (p+1)
    return result

start_time = time.time()
i = 5
b_keepLooking = True
while b_keepLooking:
    number = factorize(i)
    # print("{} : {}".format(i,number))
    number.extend((factorize(int((i+1)/2))))
    number = list(filter((0).__ne__, number))
    n_div = numberOfDivisors_v2(number)
    # print("Testing #{}".format(i))
    if n_div > 500:
        b_keepLooking = False
        print("The Triangle Number ({}) : {} is the first number with over 500 Divisors".format(i,i*(i+1)/2))
        print("It has {} divisors".format(n_div))
    i +=2

print("Completion time: {} ".format(time.time() - start_time))

# Output:
#     The Triangle Number (12375) : 76576500.0 is the first number with over 500 Divisors
#     It has 576 divisors
#     Completion time: 2.3457491397857666
