# Project Euler
# Problem 19: Counting Sundays
#       You are given the following information, but you may prefer
#       to do some research yourself.
#           * 1 Jan 1900 was a Monday.
#           * Thirty days has September,
#             April, June and November.
#             All the rest have thirty-one,
#             Saving February alone,
#             which has twenty-eight, rain or shine.
#             And on leap years,  twenty-nine
#           * A leap year occurs on any year divisible by 4,
#                  but not on a century unless it is divisible by 400.
#
#       How many Sundays fell on the first of the month during the
#       twentieth Century?  (1 Jan 1901 to 31 Dec 2000)

# Todo

# Jeffrey Spahn
# Created for Python 3.x

'''
Notes:
    1900: Jan starts Mon (1)
          Feb starts 1 + 31%7

'''

month_length = {
    1 : 31,  # January
    2 : 28,  # February - Non Leap Year
    3 : 31,  # March
    4 : 30,  # April
    5 : 31,  # May
    6 : 30,  # June
    7 : 31,  # July
    8 : 31,  # August
    9 : 30,  # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}