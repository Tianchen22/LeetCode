"""
1314. Matrix Block Sum

https://leetcode.com/problems/matrix-block-sum/

using Prefix Sum to optimize the time complexity from O(N^3) to O(N^2)
"""
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n,m = len(mat),len(mat[0])        
        for i in range(n):
            for j in range(m):
                mat[i][j] += (mat[i-1][j] if i else 0) + (mat[i][j-1] if j else 0) - (mat[i-1][j-1] if i and j else 0)
        res = []
        for i in range(n):
            res.append([])
            for j in range(m):                
                a,b = min(i+k,n-1),min(j+k,m-1)
                res[i].append(mat[a][b] - (mat[i-k-1][b] if i>k else 0) - (mat[a][j-k-1] if j>k else 0) 
				+ (mat[i-k-1][j-k-1] if i>k and j>k else 0))
        return res
                 
        
        