# Project Euler
# Problem 30: Digit fifth powers
#     Surprisingly there are only three numbers that can be written
#     as the sum of fourth powers of their digits:
#
#         1634 = 1^4 + 6^4 + 3^4 + 4^4
#         8208 = 8^4 + 2^4 + 0^4 + 8^4
#         9474 = 9^4 + 4^4 + 7^4 + 4^4
#         As 1 = 1^4 is not a sum it is not included.
#
#     The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
#     Find the sum of all the numbers that can be written as
#     the sum of fifth powers of their digits.


# Jeffrey Spahn
# Created for Python 3.x

# Idea: Could possibly improve time by looking closer at the 5th power...
#       Example: No need to check 1-31, when 2^5 = 32

import time

# ------------------------------------------------------------
#  Main
# ------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()

    # Fifth Powers:
    #       0^5 =     0
    #       1^5 =     1
    #       2^5 =    32
    #       3^5 =   243
    #       4^5 =  1024
    #       5^5 =  3125
    #       6^5 =  7776
    #       7^5 = 16807
    #       8^5 = 32768
    #       9^5 = 59049

    # Find the upper Limit
    i = 1
    while 10**i - 1 < i * 9**5:
        i += 1
    max_value = 10**i - 1

    # Search for Solutions
    solutions = []
    for i in range(2,max_value+1):
        summation = 0
        for digit in range(len(str(i))):
            summation += int(str(i)[digit]) ** 5
            if summation > i:
                break
        if i == summation:
            solutions.append(i)

    print("All numbers that are the sum of the fifth powers of their Digits:")
    print("\t{}".format(solutions))
    print("The Sum of them: {}".format(sum(solutions)))

    print("Completion time: {}".format(time.time()-start_time))

    # Output:
    #       All numbers that are the sum of the fifth powers of their Digits:
	#            [4150, 4151, 54748, 92727, 93084, 194979]
    #       The Sum of them: 443839
    #       Completion time: 6.884512186050415

