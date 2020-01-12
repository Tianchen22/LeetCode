"""
1319. Number of Operations to Make Network Connected

https://leetcode.com/problems/number-of-operations-to-make-network-connected/

Union - Find + Set
"""

class Solution:
    def makeConnected(self, n: int, c: List[List[int]]) -> int:    
        if len(c) + 1 < n:
            return -1        
        a = [i for i in range(n)]
        def uni(x):
            return uni(a[x]) if x != a[x] else x        
        for i,j in c:
            x,y = uni(i),uni(j)
            a[x] = a[y] = min(x,y)
        res = set()
        for i in range(n):
            res.add(uni(i))
        return len(res) - 1