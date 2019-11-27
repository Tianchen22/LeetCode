"""
1143. Longest Common Subsequence

https://leetcode.com/problems/longest-common-subsequence/

Simple DP Solution
Time complexity O(NM)
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1), len(text2)
        if n == 0 or m == 0: return 0
        dp = [[0 for i in range(m)] for j in range(n)]
        if text1[0] == text2[0] : dp[0][0] = 1
        for i in range(1,m):
            if text1[0] == text2[i]: 
                dp[0][i] = 1
            else:
                dp[0][i] = dp[0][i-1]
        for i in range(1,n):
            if text2[0] == text1[i]: 
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i-1][0]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i][j],dp[i-1][j-1] + 1)
        return dp[n-1][m-1]
