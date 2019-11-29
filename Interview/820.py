"""
820. Short Encoding of Words

https://leetcode.com/problems/short-encoding-of-words/

Flip the array and Using Startswith to ignore the short one(which has to be covered by)
"""

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted([x[::-1] for x in words])[::-1]
        last,res = words[0],len(words[0]) + 1
        for curr in words:
            if not last.startswith(curr):
                last = curr
                res += len(curr) + 1
        return res
