"""
1312. Minimum Insertion Steps to Make a String Palindrome

https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

This question can be converted to Longest Palindrome Sequences.
And LPS above can be converted to Longest Common Sequence.
Which is a classic DP question.

"""

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        def dfs(i,j)
            dfs()
        if s == s[::-1]:
            return 0
        f = [[0] * (n+1) for i in range(n+1)]
        for i in range(n):
            for j in range(n):
                f[i+1][j+1] = f[i][j] + 1 if s[i] == s[n - j - 1] else max(f[i][j+1],f[i+1][j])
        return n - f[n][n]
		