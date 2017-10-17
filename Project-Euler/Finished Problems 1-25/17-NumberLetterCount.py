# Project Euler
# Problem 17: Number Letter Counts
#       If the numbers 1 to 5 are written out in words: one, two, three, four,
#       five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#       If all the numbers from 1 to 1000 (one thousand) inclusive were written
#       out in words, how many letters would be used?
#
#       Note: Do not count spaces or hyphens. For example, 342 (three hundred
#       and forty-two) contains 23 letters and 115 (one hundred and fifteen)
#       contains 20 letters.  The use of "and" when writing out numbers is in
#       compliance with British usage.

# Jeffrey Spahn
# Created for Python 3.x

import time

startTime = time.time()

digitLengths = {
    1:   3,  # one
    2:   3,  # two
    3:   5,  # three
    4:   4,  # four
    5:   4,  # five
    6:   3,  # six
    7:   5,  # seven
    8:   5,  # eight
    9:   4,  # nine
    10:  3,  # ten
    11:  6,  # eleven
    12:  6,  # twelve
    13:  8,  # thirteen
    14:  8,  # fourteen
    15:  7,  # fifteen
    16:  7,  # sixteen
    17:  9,  # seventeen
    18:  8,  # eighteen
    19:  8,  # nineteen
    20:  6,  # twenty
    30:  6,  # thirty
    40:  5,  # forty
    50:  5,  # fifty
    60:  5,  # sixty
    70:  7,  # seventy
    80:  6,  # eighty
    90:  6,  # ninety
    100: 7,  # hundred
    1000:8   # thousand
}


def get_letter_count(i):
    """Returns the number of letters needed to write out the number using British English"""
    letter_count = 0

    if i // 1000 != 0:
        letter_count += digitLengths[i // 1000]  # one, two, three...
        letter_count += digitLengths[1000]       # thousand
    if (i%1000) // 100  != 0:
        letter_count += digitLengths[(i%1000) // 100] # one, two, three...
        letter_count += digitLengths[100]             # hundred
        if i % 100  != 0:
            letter_count += 3                         # and
    if (i%100) // 10   >1:
        letter_count += digitLengths[((i%100) // 10) * 10]   # twenty, thirty, forty...

    if (i % 100) // 10 == 1:
        letter_count += digitLengths[i%100]   # ten, eleven, twelve, ... nineteen
    elif i % 10 != 0:
        letter_count += digitLengths[i % 10]  # one, two, three...

    return letter_count


#------------------------------------------------------------
#  Main
#------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()

    total_letter_count = 0

    for i in range(1001):
        total_letter_count += get_letter_count(i)

    print("The total letter count of all numbers between 1 and 1000 (inclusive) is: {}".format(total_letter_count))
    print("    Completion time: {}".format(time.time() - start_time))

    # Output
    #     The total letter count of all numbers between 1 and 1000 (inclusive) is: 21124
    #         Completion time: 0.001583099365234375