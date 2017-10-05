# Project Euler
# Problem 9: Special Pythagorean Triplet
#       A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
#       a^2 + b^2 = c^2
#       For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
#       There exists exactly one Pythagorean triplet for which a + b + c = 1000
#       Find the product of abc

# Jeffrey Spahn
# Created for Python 3.x


def findTriplet():
    a = 1
    b = 2
    c = 1000 - a - b
    for a in range(1,1000):
        for b in range(a,1000):
            c = 1000 - a - b
            if c > b and a**2 + b**2 == c**2:
                return (a,b,c)


solution = findTriplet()
print(solution)
a = solution[0]
b = solution[1]
c = solution[2]

print("The solution: (a,b,c) = ({},{},{})".format(a,b,c) )
print("a + b + c = {} + {} + {} = {}".format(a,b,c,a+b+c))
print("a^2 + b^2 = {} + {} = {} = {} = c^2".format(a**2,b**2, a**2 + b**2, c**2, c))

print("The product of these numbers is:")
print("     abc = {}".format(a*b*c))

# Output:
#
#     (200, 375, 425)
#     The solution: (a,b,c) = (200,375,425)
#     a + b + c = 200 + 375 + 425 = 1000
#     a^2 + b^2 = 40000 + 140625 = 180625 = 180625 = c^2
#     The product of these numbers is:
#          abc = 31875000
