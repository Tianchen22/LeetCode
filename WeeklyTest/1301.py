"""
1301. Number of Paths with Max Score

https://leetcode.com/problems/number-of-paths-with-max-score/

Trikyyyyyyyyyyy DP question!
"""

class Solution:
    def pathsWithMaxScore(self, b: List[str]) -> List[int]:           
        n, p = len(b), 1000000007
        a,ct = [[0 for i in range(n)] for i in range(n)],[[0 for i in range(n)] for i in range(n)]
        ct[0][0] = 1
        for i in range(n):
            for j in range(n):
                if b[i][j] in 'EX':
                    continue
                for dx,dy in [[0,1],[1,0],[1,1]]:
                    x,y = i - dx, j - dy
                    if x >= 0 and y >= 0:
                        if a[x][y] == a[i][j]:
                            ct[i][j] = (ct[i][j] + ct[x][y]) % p
                        elif a[x][y] > a[i][j]:
                            ct[i][j],a[i][j] = ct[x][y], a[x][y]
                a[i][j] += int(b[i][j]) if b[i][j] != 'S' else 0                    
        return [a[n-1][n-1] if ct[n-1][n-1] else 0,ct[n-1][n-1]]