"""
1272. Remove Interval

https://leetcode.com/problems/remove-interval/

meeting rooms
"""
class Solution:
    def removeInterval(self, arr: List[List[int]], w: List[int]) -> List[List[int]]:
        a,b,res = w[0],w[1],[]
        for temp in arr:
            x,y = temp[0], temp[1]            
            if y < a or x > b: 
                res.append([x,y])
            else:
                if x < a:
                    res.append([x,a])
                if b < y:
                    res.append([b,y])
        return res
            
