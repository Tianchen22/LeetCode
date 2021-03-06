"""
Reconstruct a 2-Row Binary Matrix    

Problem Link:
https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

Thought:
  if colsum == 2, then upper and lower both minus one
  if colsum == 0, then upper and lower both cannot change
  if colsum == 1, then either upper or lower minus one
  First loop to solve all the colsum two, and then solve the colsum one
  if lower and upper is smaller than 0, return null 
"""  

  def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        length = len(colsum)
        res = [[0 for i in range(length)] for j in range(2)]
        for i,c in enumerate(colsum):
            if c == 2:
                res[0][i],res[1][i] = 1,1
                lower -= 1
                upper -= 1
        if lower < 0 or upper < 0:
            return []
        for i,c in enumerate(colsum):
            if c == 1:
                if lower > 0:
                    lower -= 1
                    res[1][i] = 1
                elif upper > 0:
                    upper -= 1
                    res[0][i] = 1
                else:
                    return []
        if lower != 0 or upper != 0:
            return []
        return res
