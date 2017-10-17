# Project Euler
# Problem 8: Largest Product in a Series
#       The four adjacent digits in the 1000-digit number that have the
#       greatest product are 9 * 9 * 8 * 9 = 5832
#           73167176531330624919225119674426574742355349194934
#           96983520312774506326239578318016984801869478851843
#           85861560789112949495459501737958331952853208805511
#           12540698747158523863050715693290963295227443043557
#           66896648950445244523161731856403098711121722383113
#           62229893423380308135336276614282806444486645238749
#           30358907296290491560440772390713810515859307960866
#           70172427121883998797908792274921901699720888093776
#           65727333001053367881220235421809751254540594752243
#           52584907711670556013604839586446706324415722155397
#           53697817977846174064955149290862569321978468622482
#           83972241375657056057490261407972968652414535100474
#           82166370484403199890008895243450658541227588666881
#           16427171479924442928230863465674813919123162824586
#           17866458359124566529476545682848912883142607690042
#           24219022671055626321111109370544217506941658960408
#           07198403850962455444362981230987879927244284909188
#           84580156166097919133875499200524063689912560717606
#           05886116467109405077541002256983155200055935729725
#           71636269561882670428252483600823257530420752963450
#       Find the thirteen adjacent digits in the 1000-digit number that
#       have the greatest product.  What is the value of this product?

# Jeffrey Spahn
# Created for Python 3.x

import time


def get_product(start_index, series):
    """Starting at the start_index, will multiply the next 13 numbers together.
            If one of these numbers is a 0, the start_index will shift to one digit
            past that and will begin again."""
    end_index = start_index
    product = -1    # Product of -1 means there was no 13 digits starting at start_index with a product larger than 0

    while end_index - start_index < 13 and end_index < len(series):
        if int(series[end_index]) != 0:
            if product < 0:
                product *= -1
            product = product * int(series[end_index])
            end_index += 1
        else:
            start_index = end_index + 1
            end_index = start_index
            product = -1
    if end_index - start_index < 13:
        product = -1
    return {"start_index":start_index, "product":product}


def shift_forward(params, series):
    """Divides the product by the number at the start_index and multiplies by
            the next number in the series.  Shifts forward the start_index by 1.
            If the next number in the series is 0, we reset the product by
            multiplying the next 13 numbers that don't include 0.
            Returns a product of -1 if there are not 13 numbers left with a
            product greater than 0"""
    if params["start_index"]+13 >= len(series):
        params["product"] = -1
        return params
    if int(series[params["start_index"]+13]) == 0:
        return get_product(params["start_index"]+14, series)
    else:
        params["product"] = params["product"] / int(series[params["start_index"]])
        params["product"] = params["product"] * int(series[params["start_index"]+13])
        params["start_index"] += 1
    return params


def find_largest_product(series):
    """ Finds the 13 adjacent digits that result in the largest product"""
    max_result = 0
    max_start_index = 0

    # get the Initial product
    params = get_product(0, series)
    if params["product"] !=-1:
        max_result = params["product"]

    # go through the rest of the series to see if there is anything bigger
    while params["start_index"] + 13 < len(series):
        params = shift_forward(params, series)
        if params["product"] > max_result:
            max_result = params["product"]
            max_start_index = params["start_index"]

    return {"max_result": max_result, "max_start_index":max_start_index}


#------------------------------------------------------------
#  Main
#------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()

    s_series = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    result = find_largest_product(s_series)
    digits = s_series[result["max_start_index"]:result["max_start_index"] + 13]

    print("Max Result = " + str(result["max_result"]))
    print("Start Index = " + str(result["max_start_index"]))
    print("Multiplication: " + str(digits[0]), end='')
    for i in range(1, 13):
        print(" * " + str(digits[i]), end='')
    print()
    print("   Completion time: {}".format(time.time() - start_time))

    # Output:
    #     Max Result = 23514624000.0
    #     Multiplication: 5 * 5 * 7 * 6 * 6 * 8 * 9 * 6 * 6 * 4 * 8 * 9 * 5
    #     Start Index = 197
    #        Completion time: 0.001241922378540039


