"""
5318. Minimum Number of Taps to Open to Water a Garden

https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

The number in the range means the segment instead of the point(confuse me for a long time)

There're about 3 different solutions
and same questions as 1024. Video Stitching
"""
# My solution
    def minTaps(self, n: int, ranges: List[int]) -> int:   
        w = [[max(i - c, 0), i + c] for i,c in enumerate(ranges)]
        w = sorted(w, key = lambda x:(x[0], -x[1]))
        curr, res, maxn= -1, 0, 0        
        for l,r in w:
            if maxn >= n:
                return res
            if l <= curr:
                maxn = max(maxn,y)
            else:
                if x > maxn:
                    return -1
                res += 1
                curr,maxn = maxn,y
                
        return res if maxn >= n else -1
		
# DP solution by Lee
    def minTaps(self, n, A):
        dp = [0] + [n + 2] * n
        for i, x in enumerate(A):
            for j in xrange(max(i - x + 1, 0), min(i + x, n) + 1):
                dp[j] = min(dp[j], dp[max(0, i - x)] + 1)
        return dp[n] if dp[n] < n + 2 else -1