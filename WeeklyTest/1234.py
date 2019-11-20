"""
1234. Replace the Substring for Balanced String

Problem link:
https://leetcode.com/problems/replace-the-substring-for-balanced-string/

Thought:
	Sliding Window~~~~~~~~~~~~~~~~
"""


class Solution:
    def balancedString(self, s: str) -> int:
        count = collections.Counter(s)
        res = n = len(s)
        i = 0
        for j,c in enumerate(s):
            count[c] -= 1
            while i < n and all(n / 4 >= count[x] for x in 'QWER'):
                res = min(res,j - i + 1)
                count[s[i]] += 1
                i += 1
        return res
    
        