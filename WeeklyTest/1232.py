"""
1232. Check If It Is a Straight Line

Problem link:
https://leetcode.com/problems/check-if-it-is-a-straight-line/

Thought:
	Using the CrossProduct
"""
class Solution:
    def checkStraightLine(self, a: List[List[int]]) -> bool:
        i,j = a[0] , a[1]
        return all(i[0] * j[1] + j[0] * k[1] + k[0] * i[1] - i[1] * j[0] - j[1] * k[0] - k[1] * i[0] == 0 for k in a)