"""
1269. Number of Ways to Stay in the Same Place After Some Steps

https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

Classic DP(Dynamic Program) Question
"""
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        q = 1000000007
        last , curr = [0 for i in range(steps+2)],[0 for i in range(steps+2)]
        last[0] = 1
        for i in range(steps):
            curr[0] = (last[0] + last[1]) % q
            for j in range(1,min(arrLen,steps)):
                curr[j] = (last[j-1] + last[j] + last[j+1]) % q
            for j in range(min(arrLen,steps)):
                last[j] = curr[j]
        return curr[0]
        
