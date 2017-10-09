# Project Euler
# Problem 18: Maximum Sum Path 1
#       By starting at the top of the triangle below and moving to adjacent
#       numbers on the row below, the maximum total from the top to bottom
#       is 23.
#                                   3
#                                 7   4
#                               2   4   6
#                             8   5   9   3
#
#       That is, 3 + 7 + 4 + 9 = 23
#       Find the maximum total from top to bottom of the triangle below:
#                                     75
#                                   95  64
#                                 17  47  82
#                               18  35  87  10
#                             20  04  82  47  65
#                           19  01  23  75  03  34
#                         88  02  77  73  07  63  67
#                       99  65  04  28  06  16  70  92
#                     41  41  26  56  83  40  80  70  33
#                   41  48  72  33  47  32  37  16  94  29
#                 53  71  44  65  25  43  91  52  97  51  14
#               70  11  33  28  77  73  17  78  39  68  17  57
#             91  71  52  38  17  14  91  43  58  50  27  29  48
#           63  66  04  68  89  53  67  30  73  16  69  87  40  31
#         04  62  98  27  23  09  70  98  73  93  38  53  60  04  23
#       Note: As there are only 16384 routes, it is possible to solve this
#           problem by trying every route.  However, Problem 67, is the same
#           challenge with a triangle containing one-hundred rows; it cannot
#           be solved by brute force, and requires a clever method! ;o)

# Jeffrey Spahn
# Created for Python 3.x

# Pseudocode:
'''
Start at the line second from the bottom (n -1). For each number there, add the
largest number it could go to.  These is now the new last line. repeat until you
reach the top

example: 63 becomes 63 + 62 = 125
         66 becomes 66 + 98 = 164
         04 becomes 04 + 98 = 102
         68 becomes 68 + 27 = 95
'''

import time
startTime = time.time()

s_triangle = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

# toIntTriangle(args_Triangle)
#       returns the triangle array in integer form
def toIntTriangle(args_Triangle):
    args_Triangle = args_Triangle.split("\n")

    n_triangle = []
    for s in args_Triangle:
        s_level = s.split(" ")
        n_level = []
        for value in s_level:
            n_level.append(int(value))
        n_triangle.append(n_level)
    return n_triangle


int_triangle = toIntTriangle(s_triangle)
n = len(int_triangle)   # Height of Triangle

# for row in int_triangle:
#     print(row)

for i in range(n-2,-1,-1):
    for j in range(i+1):
        if int_triangle[i+1][j] > int_triangle[i+1][j+1]:
            int_triangle[i][j] = int_triangle[i][j] + int_triangle[i+1][j]
        else:
            int_triangle[i][j] = int_triangle[i][j] + int_triangle[i+1][j+1]


# for row in int_triangle:
#     print(row)

print("The Maximum total from the top to the bottom is: {}".format(int_triangle[0][0]))
print("Time: {}".format(time.time() - startTime))

# Output:
#       The Maximum total from the top to the bottom is: 1074
#       Time: 0.0
