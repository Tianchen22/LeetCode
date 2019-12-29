"""
1300. Sum of Mutated Array Closest to Target

https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

Binary(Terary?) search
"""
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:        
        l,r = 0,target
        def check(k):
            res = 0
            for x in arr:
                res += x if x < k else k
            return abs(res-target)
        while l<r:
            mid = (l+r) // 2
            mid2 = (l+mid) // 2
            if check(mid) < check(mid2):
                l = mid2 + 1
            else:
                r = mid 
        return l
                
                