'''
322. Coin Change
Medium
Topics
premium lock icon
Companies
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
'''

# By Bottom-Up Approach (Tabulation)
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins to make amount 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:   # Check if the coin can be used
                dp[i] = min(dp[i], 1 + dp[i - coin])  # Update the minimum coins needed

    return -1 if dp[amount] == float('inf') else dp[amount]

## By Top-Down Approach (Memoization)
def CoinChange(coins, amount):
    memo = {}

    def helper(rem):

        if rem in memo:
            return memo[rem]
        if rem == 0:
            return 0
        if rem < 0:
            return float('inf')

        min_coins = float('inf')
        for coin in coins:
            res = helper(rem - coin)
            if res != float('inf'):
                min_coins = min(min_coins, 1 + res)

        memo[rem] = min_coins
        return memo[rem]

    ans = helper(amount)
    return -1 if ans == float('inf') else ans

# Example usage:
if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(coinChange(coins, amount))  # Output: 3

    coins = [2]
    
    amount = 3
    print(coinChange(coins, amount))  # Output: -1

    coins = [1]
    amount = 0
    print(coinChange(coins, amount))  # Output: 0
    