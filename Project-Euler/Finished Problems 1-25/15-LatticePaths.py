# Project Euler
# Problem 15: Lattice Paths
#       Starting in the top left corner of a 2x2 grid, and only being able
#       to move to the right and down, there are exactly 6 routes to the
#       bottom right corner.
#            * *        * _        * _
#           |_|_*      |_*_|      |_**|
#           |_|_*      |_**|      |_|_*
#           RRDD        RDDR       RDRD
#
#            _ _        _ _        _ _
#           **|*|      **|_|      *_|_|
#           |_|_*      |_**|      **|*|
#           DRRD       DRDR       DDRR
#
#       How many such routes are there through a 20x20 grid?

# Jeffrey Spahn
# Created for Python 3.x

# To find the number of paths, we can work backwards. Starting at the end point,
#       we can ask, how many paths does it take to get to the end point, and we
#       work our way out; not needing to count every path each time, only add
#       the total paths that we have already counted.
#     Example for a 3x3:
#                   20 - 10 -  4 -  1
#                   10 - 6  -  3 -  1
#                    4 - 3  -  2 -  1
#                    1 - 1  -  1 -  1
#       We see that this is pascal's triangle.
# For a 20x20 grid we just need to calculate the binomial coefficent for  nCr (40,20)
#       nCr (40,20) = 40!/(20!*20!)
import time


def factorial(n):
    """Performs a factorial calculation on n: n!"""
    result = 1
    for i in range(1,n+1):
        result *= i
    return result


def bin_coef(n,r):
    """returns the binary coefficient of nCr"""
    return factorial(n)/ (factorial(r)* factorial(n-r))


#------------------------------------------------------------
#  Main
#------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()
    print("The number of paths in a 20x20 grid is: {}".format(bin_coef(40,20)))
    print("    Completion time: {}".format(time.time() - start_time))

    # Output:
    #     The number of paths in a 20x20 grid is: 137846528820.0
    #     Completion time: 3.719329833984375e-05