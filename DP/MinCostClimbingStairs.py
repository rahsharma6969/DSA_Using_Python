'''
746. Min Cost Climbing Stairs
Easy

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.'''

# Top-down dynamic programming approach
# This approach uses recursion with memoization to find the minimum cost to reach the top.

def minCostClimbingStairs(cost):
    n = len(cost)
    def dp(i):
        if i >= n:
            return 0
        return cost[i] + min(dp(i + 1), dp(i + 2))
    
    return min(dp(0), dp(1))


#Bottom-up dynamic programming approach
# This approach uses a DP array to store the minimum cost to reach each step.


def MinCostClimbingStairs(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
    return dp[n]


# Example usage
if __name__ == "__main__":
    cost = [10, 15, 20]
    print(MinCostClimbingStairs(cost))  # Output: 15

    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(MinCostClimbingStairs(cost))  # Output: 6
    
    