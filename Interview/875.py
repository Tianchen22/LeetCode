"""
875. Koko Eating Bananas

https://leetcode.com/problems/koko-eating-bananas/

Classic Binary Search
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l , r = 1 , max(piles)
        # l cannot be 0 because mid is the divisor
        # r can be max(piles) because piles.length <= H (in the note)
        while l < r:
            mid = (l+r) // 2
            if sum((x + mid - 1) // mid for x in piles) <= H:
            # (x + mid - 1) // mid is a billiant way of
            # -> x // mid + (1 if x % mid > 0)
                r = mid
            else:
                l = mid + 1
        return l
        
