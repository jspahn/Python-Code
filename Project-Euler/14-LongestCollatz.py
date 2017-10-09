# Project Euler
# Problem 14: Longest Collatz Sequence
#       The following iterative sequence is defined for the set of positive
#       integers:
#           n -> n/2 (n is even)
#           n -> 3n+1 (n is odd)
#       Using the rule above and starting with 13, we  generate the following
#       sequence:
#           13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#       It can be seen that this sequence (starting at 13 and finishing at 1)
#       contains 10 terms.  Although it has not been proved yet (Collatz
#       Problem), it is thought that all starting numbers finish at 1.
#
#       Which starting number, under one million, produces the longest chain?
#       Note: Once the chain starts the terms are allowed to go above one million


# Jeffrey Spahn
# Create for Python 3.x

import time

def nextCollatz(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return int(3*n+1)

start_time = time.time()
n = 1000001
pathLengths = [0] * n
pathLengths[1] = 1

for i in range(2,n):
    if pathLengths[i] == 0:
        count = 1
        path = [i]
        b_continueOnPath = True
        while b_continueOnPath:
            i = nextCollatz(i)
            if i < n:
                if pathLengths[i] != 0:
                    b_continueOnPath = False
                    count += pathLengths[i]
            if b_continueOnPath:
                path.append(i)
                count += 1
        for j in range(len(path)):
            if path[j] < n:
                pathLengths[path[j]] = count
            count -= 1



maxNumber = pathLengths.index(max(pathLengths))
print("The Largest chain begins with #{} and is {} numbers long.".format(maxNumber,pathLengths[maxNumber]))
print("This took {} s".format(time.time()-start_time))

# Output
#     The Largest chain begins with #837799 and is 525 numbers long.
#     This took 3.2922286987304688 s
