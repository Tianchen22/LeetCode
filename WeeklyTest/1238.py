"""
1238. Circular Permutation in Binary Representation

Problem link:
https://leetcode.com/problems/circular-permutation-in-binary-representation/

Thought:
	Gray Code
"""

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = []
        for x in range(1<<n):
            res.append(start ^ x ^ (x >> 1))
        return res