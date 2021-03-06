"""
Cells with Odd Values in a Matrix    

Problem link:
  https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

Thought:
  Just simulation using two arrays as rows and columns
"""

  def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
      listn = [0 for i in range(n)]
      listm = [0 for i in range(m)]
      for i in range(len(indices)):
          listn[indices[i][0]] += 1
          listm[indices[i][1]] += 1
      res = 0
      for i in range(n):
          for j in range(m):
              if (listn[i] + listm[j]) & 1 == 1:
                  res += 1
      return res
