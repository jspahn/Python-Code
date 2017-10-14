# Project Euler
# Problem 25: 1000-digit Fibonacci Number
#       The Fibonacci sequence is defined by the recurrance relation:
#           F_n = F_n-1 + F_n-2, where F_1 = 1 and F_2 = 1
#
#       Hence the first 12 terms will be:
#           F_1  = 1
#           F_2  = 1
#           F_3  = 2
#           F_4  = 3
#           F_5  = 5
#           F_6  = 8
#           F_7  = 13
#           F_8  = 21
#           F_9  = 34
#           F_10 = 55
#           F_11 = 89
#           F_12 = 144
#
#       The 12th term, F_12, is the first term to contain three digits.
#
#       What is the index of the first term in the Fibonacci Sequence
#       to contain 1000 digits?

# Jeffrey Spahn
# Created for Python 3.x

import time

start_time = time.time()


def index_n_digits(n):
    """Returns the index of the first fibonacci number that is n digits long"""
    first_num = 1
    second_num = 1

    i = 1
    while len(str(second_num)) < n:
        i += 2
        first_num = first_num + second_num
        second_num = first_num + second_num

    if len(str(first_num)) == n:
        return i
    else:
        return i + 1


print("Index of First Fibonacci Number with 1000 digits: {}".format(index_n_digits(1000)))
print("Completion time: {}".format(time.time()-start_time))

# Output:
#     Index of First Fibonacci Number with 1000 digits: 4782
#     Completion time: 0.013983964920043945
