"""
1293. Shortest Path in a Grid with Obstacles Elimination

https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

BFS + Dictionary
*put unused point or used point with less Obstacles to the stack
"""
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n,m = len(grid),len(grid[0])
        if n == 1 and m == 1:
            return -1 if k == 0 and grid[0][0] == 1 else 0
        used = {}
        d = [[1,0],[0,1],[-1,0],[0,-1]]
        q,used[(0,0)] = [[0,0,0,0]],0
		# x pos, y pos, Obstacle, current route
        while len(q) > 0:
            x,y,prev,rt = q[0][0], q[0][1], q[0][2], q[0][3]
            for i in range(4):
                tx,ty = x + d[i][0], y + d[i][1]
                if tx >= 0 and tx < n and ty >= 0 and ty < m:
                    curr = prev if grid[tx][ty] == 0 else prev + 1
                    if curr <= k and used.get((tx,ty),k + 1) > curr:
                        if tx == n-1 and ty == m-1:
                            return rt + 1
                        used[(tx,ty)] = curr
                        q.append([tx,ty,curr,rt+1])                        
            q.pop(0)
        return -1