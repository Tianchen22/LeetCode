"""
1318. Minimum Flips to Make a OR b Equal to c

https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

It is quite like Finding the regular pattern in or \
then dicuss three different kind of situations
"""

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a or b or c:
            i,j = a % 2 + b % 2, c % 2
            res += i if not j else 1 if not i else 0
            a,b,c = a // 2,b // 2,c // 2
        return res