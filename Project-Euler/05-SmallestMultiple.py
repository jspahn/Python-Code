# Project Euler
# Problem 5: Smallest Multiple
# Problem Details:
#         2520 is the smallest number that can be divided by each of the
#         numbers from 1 to 10 without any remainder.
#         What is the smallest positive number that is evening divisible
#         by all the numbers from 1 to 20?

# Jeffrey Spahn
# created for Python 3.x


multipliers = [2]
for i in range(2,20):
    for m in multipliers:
        if i%m == 0:
            i = int(i)/ int(m)
    if i !=1:
        multipliers.append(int(i))

solution = 1
for x in multipliers:
    solution = solution * x

print("The smallest multiple of all numbers from 1 to 20 is: "
      + str(solution))

# Output:
#   The smallest multiple of all numbers from 1 to 20 is: 232792560



