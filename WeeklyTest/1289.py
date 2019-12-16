"""
1289. Minimum Falling Path Sum II

https://leetcode.com/problems/minimum-falling-path-sum-ii/

greed!!!!
"""
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n,m = len(arr),len(arr[0])
        for i in range(1,n):
            r = sorted(arr[i-1])
			# find smallest one and second smallest one 
            for j in range(m):
				# current dot plus second smallest one 
				# iff the smallest one is in the same column
                arr[i][j] += r[1] if arr[i-1][j] == r[0] else r[0]
        return min([x for x in arr[n-1]])
        