"""
188. Best Time to Buy and Sell Stock IV

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

The first thought is dp question
dp[n][k] (n numbers with k transactions)

But when k is very large (and n is very large,too), 
the time complexity O(NK) is not good enough

When k > n >> 1, (k is larger then half length)
just find all the increasing subsequences in the array, sum the biggest - smallest
And the time complexity is O(N)
Otherise do the algorithm above.
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:        
        n = len(prices)
        if n == 0:
            return 0
        elif k > n >> 1: 
            # if k is larger then half length, then just find the sum
            # of the left and right of an increasing subsequence
            return sum(prices[i+1]-prices[i] for i in range(n-1) if prices[i+1] > prices[i])
        
        curr, prev = [0 for i in range(n)],[0 for i in range(n)]
        for x in range(k):
            # initalize curr to a large number
            temp = 2e31 - 1
            for i,p in enumerate(prices): # p means price
                if i > 0: curr[i] = max(curr[i-1],p - temp)
                temp = min(temp,p - prev[i])
            curr, prev = [0 for j in range(n)],[x for x in curr] 
        return prev[n-1]
            
