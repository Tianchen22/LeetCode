"""
240. Search a 2D Matrix II

https://leetcode.com/problems/search-a-2d-matrix-ii/

Solution 1 (which was my solution) is BFS:
	To current pos, search the bottom and right pos
	Worst Time Complexity is O(N^2)
"""
class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        n,m = len(matrix),len(matrix[0])
        used = [[False for i in range(m)] for i in range(n)]
        q = [[0,0]]
        while q:                
            x,y = q[0][0],q[0][1]
            curr = matrix[x][y]
            if matrix[x][y] == target:
                return True
            if x + 1 < n and not used[x+1][y] and matrix[x+1][y] >= curr:
                used[x+1][y] = True
                q.append([x+1,y])
            if y + 1 < m and not used[x][y+1] and matrix[x][y+1] >= curr:
                used[x][y+1] = True
                q.append([x,y+1])
            q.pop(0)
        return False
        
"""
Solution 2 is very thicky, but smart.
start from top right or left bottom, 
then the patterm is that 
the row and column number is either increasing or decreasing,
so the time Complexity is O(N)  
"""
class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        n,m = len(matrix),len(matrix[0])
        x,y = 0,m-1
        while x < n and y >= 0 and matrix[x][y] != target:
            if matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        if x < n and y >= 0 and matrix[x][y] == target:
            return True
        else:
            return False
        
                    
