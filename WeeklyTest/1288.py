"""
1288. Remove Covered Intervals

https://leetcode.com/problems/remove-covered-intervals/


"""
class Solution:
    def removeCoveredIntervals(self, arr:List[List[int]]) -> int:
        arr.sort(key = lambda s:(s[0],-s[1]))
		# sort from smallest to biggest in first index
		# and from biggest to smallest in second index	
        ct,res = -1,0
        for x in arr:
			# always update the biggest second index
			# once update, res plus one 
            res += 1 if x[1] > ct else 0
            ct = max(ct,x[1])
        return res