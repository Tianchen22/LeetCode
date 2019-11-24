"""
1267. Count Servers that Communicate

https://leetcode.com/problems/count-servers-that-communicate/

calculus the total server number
If current column and row only has one server, then total minus one
"""
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        lenn,lenm = len(grid), len(grid[0])
        col,row = [0 for i in range(lenn)],[0 for i in range(lenm)]
        tot = 0
        for i in range(lenn):
            for j in range(lenm):
                if grid[i][j] == 1:
                    tot += 1
                    col[i] += 1
                    row[j] += 1
        for i in range(lenn):
            for j in range(lenm):
                if grid[i][j] == 1 and col[i] == 1 and row[j] == 1:
                    tot -= 1
        return tot
                
                
