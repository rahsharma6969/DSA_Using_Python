'''
983. Minimum Cost For Tickets
Medium
Topics
premium lock icon
Companies
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

 

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.
'''
# Top Down Approach (Memoization)


'''
Approach:
1. Create a memoization dictionary to store the minimum cost for each day.
2.Define a recursive function that calculates the minimun cost for a given day
3. For each day, calculate the cost for each type of pass (1-day, 7-day, 30-day).
4. Use the memoization dictionary to avoid redundant calculations.  
5. Return the minimum cost for the last day in the days list.
    '''
    

def mincostTickets(days, costs):
    day_set = set(days)
    max_day = days[-1]
    dp = [0] * (max_day + 1)

    for day in range(1, max_day + 1):
        if day not in day_set:
            dp[day] = dp[day - 1]
        else:
            cost1 = dp[day - 1] + costs[0]            # 1-day pass
            cost7 = dp[max(0, day - 7)] + costs[1]    # 7-day pass
            cost30 = dp[max(0, day - 30)] + costs[2]  # 30-day pass
            dp[day] = min(cost1, cost7, cost30)

    return dp[max_day]

 
        
    
# Example usage:
if __name__ == "__main__":
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]  
    print(mincostTickets(days, costs))  # Output: 11