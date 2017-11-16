# Project Euler
# Problem 28:  Number spiral diagonals
#     Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
#             *21*  22   23   24  *25*
#              20  * 7*   8  * 9*  10
#              19    6  * 1*   2   11
#              18  * 5*   4  * 3*  12
#             *17*  16   15   14  *13*
#
#     It can be verified that the sum of the numbers on the diagonals is 101.
#
#     What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
#       formed in the same way?


# Jeffrey Spahn
# Created for Python 3.x

import time


def new_circle(n):
    """sums the corners of an nxn square
    Assumes n is odd"""
    if n == 1:
        return 1
    else:
        return 4*(n-2)**2 + 10*(n-1)


# ------------------------------------------------------------
#  Main
# ------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()

    diagonal_sum = 0
    for n in range(1,1002,2):
        diagonal_sum += new_circle(n)

    print("The solution is {}".format(diagonal_sum))
    print("Completion time: {}".format(time.time()-start_time))
    # Output:
    #     The solution is 669171001
    #     Completion time: 0.00043010711669921875
    #


