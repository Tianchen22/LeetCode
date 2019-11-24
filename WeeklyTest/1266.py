"""
1266. Minimum Time Visiting All Points

https://leetcode.com/problems/minimum-time-visiting-all-points/

Easy Simulation Problem
"""

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x,y = points[0][0],points[0][1]
        res = 0
        for a in points:
            tx,ty = a[0],a[1]
            res += min(abs(tx-x),abs(ty-y)) + abs(abs(tx-x)-abs(ty-y))
            x,y = tx,ty
        return res
