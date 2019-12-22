"""
1277. Count Square Submatrices with All Ones

https://leetcode.com/problems/count-square-submatrices-with-all-ones/submissions/

At first, i am so stupid using O(NMK) and trying to prune, but always TLE.
Anyway i find that one nesting loop is unnesscessary so the time complexity could be O(NM)
*but the time just beat 33% in python3, maybe there are quicker algorithms
"""
class Solution:
    def countSquares(self, a:List[List[int]]) -> int:
        n,m,res = len(a), len(a[0]), 0
        for i in range(1,n):
            for j in range(1,m):
                if a[i][j] == 0: continue
                l = min(a[i][j-1],a[i-1][j])
                a[i][j] = l + 1 if a[i-l][j-l] else l
        return sum([j for i in a for j in i])
            
