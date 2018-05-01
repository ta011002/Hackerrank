"""
Problem : DP: Coin Change
Explain : https://www.hackerrank.com/challenges/ctci-coin-change/problem
Input : number of dollars, n,, and a list of dollar values for m distinct coins, C ={c_0, c_1, c_2,..., c_(m-1)}
Output : single integer denoting the number of ways we can make change for n dollars using an infinite supply of our m types of coins.
"""


def make_change(coins, n):
    lookup = [1] + [0] * n
    for coin in coins:
        for i in range(n+1-coin):
            lookup[i+coin] += lookup[i]
    return lookup[n]


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))