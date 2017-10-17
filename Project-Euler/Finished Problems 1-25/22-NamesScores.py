# Project Euler
# Problem 22: Names Scores
#       Using 22-names.txt, a 46K text file containing over five-thousand
#       first names, begin by sorting it into alphabetical order. Then
#       working out the alphabetical value of each name, multiply this
#       by its alphabetical position in the list to obtain a name score.
#
#       For example, when the list is sorted into alphabetical order,
#       COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th
#       name on the list. So, COLIN would obtain a score of 938 * 53 = 49714.
#
#       What is the total of all the name scores in the file?

# Jeffrey Spahn
# Created for Python 3.x

import time

start_time = time.time()


def word_to_score(s):
    """Calculates the word score:
        Takes a word (string) and converts each letter to an integer:
        A = 1, B = 2, C = 3, ... Z = 26
        Sums the values together and returns an integer score of the
        word.  (Is not case sensitive)"""
    s = str(s).upper()
    score = 0
    for i in s:
        score += ord(i)-64
    return score


# ------------------------------------------------------------
#  Main
# ------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()

    f_names = open("22-names.txt", 'rt')
    s_names = f_names.read()
    f_names.close()

    l_names = s_names[1:-1].split('","')
    l_names.sort()

    total_score = 0
    for i in range(len(l_names)):
        total_score += (i+1) * word_to_score(l_names[i])

    print("Total Score = {}".format(total_score))
    print("    Completion time: {}".format(time.time() - start_time))

    # Output:
    #     Total Score = 871198282
    #         Completion time: 0.01044011116027832
