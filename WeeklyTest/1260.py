"""
1260. Shift 2D Grid

Problem Link:
  https://leetcode.com/problems/shift-2d-grid/
  
Thought:
  Easy simulation solution.

"""

  class Solution:
      def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
          n,m = len(grid), len(grid[0])
          res = []
          for i in range(n):
              res.append([])
              for j in range(m):
                  num = i * m + j - k
                  while num < 0: 
                      num += n*m
                  x,y = num // m, num % m
                  res[i].append(grid[x][y])
          return res
