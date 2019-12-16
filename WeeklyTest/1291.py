"""
1291. Sequential Digits

https://leetcode.com/problems/sequential-digits/

Simulation!
"""
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res,ct,nm,curr = [] , 1 , 1, 1
        while ct < high:
            temp = ct
            for i in range(curr,10): # maintain units (< 10 equals <= 9)
                if temp >= low and temp < high:
                    res.append(temp)
                temp += nm                
            nm, ct, curr = nm * 10 + 1,ct * 10 + curr + 1, curr + 1 
			# for example,
			# nm = 111, ct = 123, curr = 3
        return res
        