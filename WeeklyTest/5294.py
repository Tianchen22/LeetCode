"""
https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

5294. Maximum Candies You Can Get from Boxes

Simulation problems
"""
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], contain: List[List[int]], q: List[int]) -> int:
        res,used,flag = 0,{},True
        while flag:
            flag = False
            for x in q:
                if used.get(x,True) and status[x] == 1:
                    used[x] = False
                    res += candies[x]
                    for k in keys[x]:
                        status[k] = 1
                    for k in contain[x]:
                        q.append(k)
                    flag = True
        return res 
        
                    
            