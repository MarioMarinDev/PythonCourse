#!/bin/python3

# Complete the howManyGames function below.
# P = normal price
# D = discount per game
# M = minimum price
# S = Current money
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    price = p
    can_purchase = s >= price
    games = 0
    while can_purchase:
        games += 1
        # print("{} | {} - {} = {}".format(games, s, price, s - price))
        s -= price
        price = clamp(price - d, m, p)
        can_purchase = s >= price
    return games


def clamp(value, vMin, vMax):
    if value > vMax:
        return vMax
    if value < vMin:
        return vMin
    return value


if __name__ == '__main__':
    result = howManyGames(20, 3, 6, 80)
    print(result)
