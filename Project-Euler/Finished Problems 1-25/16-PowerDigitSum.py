# Project Euler
# Problem 16: Power Digit Sum
#       2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
#       What is the sum of the digits of the number 2^1000?

# Jeffrey Spahn
# Created for Python 3.x

import time



#------------------------------------------------------------
#  Main
#------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()

    number = 2**1000

    summation = 0

    for i in str(number):
        summation += int(i)

    print("2^1000 = {}".format(number))
    print("Sum of digits: {}".format(summation))
    print("    Completion time: {}".format(time.time() - start_time))

    # Output:
    #     2^1000 = 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
    #     Sum of digits: 1366
    #         Completion time: 0.00015282630920410156