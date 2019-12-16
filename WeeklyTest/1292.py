"""
1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

convert meaning of array first,
arr[x][y] means the size sum from (0,0) to (x,y)
then the sum from (a,b) to (c,d) can be calculated as -> arr[c][d] - arr[a][d] - arr[c][b] + arr[a][b] * d > b & c > a
"""
class Solution:
    def maxSideLength(self, arr: List[List[int]], tar: int) -> int:
        n,m = len(arr), len(arr[0])
        for i in range(1,n):
            arr[i][0] += arr[i-1][0]
        for i in range(1,m):
            arr[0][i] += arr[0][i-1]
        for i in range(1,n):
            for j in range(1,m):
                arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]
		# arr is the size sum from (0,0) to (x,y) and then find biggest possible number 
        for k in range(1,min(n,m)+1):
            tri = False
            for i in range(k-1,n):
                for j in range(k-1,m):
                    if not tri and arr[i][j] - (arr[i][j-k] if j > k else 0) - (arr[i-k][j] if i > k else 0) 
					+ (arr[i-k][j-k] if j > k and i > k else 0) <= tar:
                        tri = True
                        break
            if not tri:
                return k-1
        return min(n,m)