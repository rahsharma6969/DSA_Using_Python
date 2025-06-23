'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
'''



def maxProfit(prices):
    min_price = float('inf')  # Start with very high price
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            
            
            profit = price - min_price                          
            max_profit = max(max_profit, profit)

    return max_profit

'''Approach
| Day | Price | min\_price | Profit = price - min | max\_profit |
| --- | ----- | ---------- | -------------------- | ----------- |
| 0   | 7     | 7          | -                    | 0           |
| 1   | 1     | 1 ✅      | -                     | 0            |
| 2   | 5     | 1          | 4                    | 4 ✅        |
| 3   | 3     | 1          | 2                    | 4            |
| 4   | 6     | 1          | 5 ✅                 | 5 ✅        |
| 5   | 4     | 1          | 3                    | 5            |
'''
