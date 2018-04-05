# Project Euler
# Problem 31: Coin Sums
#         In England the currency is made up of pound, £, and pence, p, and
#         there are eight coins in general circulation:
#
#         1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#         It is possible to make £2 in the following way:
#
#         1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#         How many different ways can £2 be made using any number of coins?


# Jeffrey Spahn
# Created for Python 3.x

import time


def num_ways(coin_denominations, target_value):
    """Finds all combinations of coins that add up to the target value."""
    combination_count = 0
    coin_count = {c : 0 for c in coin_denominations}
    l_combinations = []
    coin_denominations.sort()
    coin_denominations.reverse()

    largest_coin = coin_denominations[0]
    delta_coin = coin_denominations[0] + 1

    # If the last combination was not made of all the smallest denominations, then look for more combinations
    while largest_coin > coin_denominations[-1]:
        value = 0

        if delta_coin == coin_denominations[-1]:
            delta_coin = coin_denominations[-2]
            while coin_count[delta_coin] == 0 and coin_denominations.index(delta_coin) > 0:
                delta_coin = coin_denominations[coin_denominations.index(delta_coin) - 1]

        for c in coin_denominations:
            if c == delta_coin:
                coin_count[c] = coin_count[c] - 1
            if c < delta_coin:
                coin_count[c] = (target_value - value) // c
            value += coin_count[c] * c

        if value == target_value:
            combination_count += 1
            delta_coin = c
            l_combinations.append(list(coin_count.values()))

        largest_coin = 0
        # find largest coin
        for c in coin_denominations:
            if coin_count[c] > 0:
                largest_coin = c
                break
    return l_combinations


# ------------------------------------------------------------
#  Main
# ------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()

    coin_denominations = [100, 50, 25, 10, 5, 1]
    goal_value = 200

    all_combinations = num_ways(coin_denominations, goal_value)
    for combin in all_combinations:
        print(combin)

    solution = len(all_combinations)

    print("\nThe Answer is: {}".format(solution))
    print("Completion time: {}".format(time.time() - start_time))

    # Output:
    #     The Answer is: 73682
    #     Completion time: 0.19931387901306152


