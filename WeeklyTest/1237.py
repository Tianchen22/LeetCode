"""
1237. Find Positive Integer Solution for a Given Equation

Problem Link:
https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

Thought:
	easy simutation solution.
"""

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        for x in range(1,z+1):
            for y in range(1,z+1):
                if customfunction.f(x,y) == z :
                    res.append([x,y])
        return res
        