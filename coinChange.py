# You are given coins of different denominations and total amount of money. Find the minimum number of coins that you need to make up the given ammount.

def coinChnge(totalNumber, coins):
    N = totalNumber
    coins.sort()
    index = len(coins) - 1
    while True:
        coinValue = coins[index]
        if N >= coinValue:
            print(coinValue, end=" ")
            N = N - coinValue
        if N < coinValue:
            index -= 1
        if N == 0:
            break


coins = [1, 2, 5, 20, 50, 100]
coinChnge(201, coins)
