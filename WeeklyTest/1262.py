"""
1262. Greatest Sum Divisible by Three

Problem link:
  https://leetcode.com/problems/greatest-sum-divisible-by-three/
  
Thought:
  if the sum reminder left 1, just minus one number left 1(module 3) or two number left 2(module 3)
  if the sum reminder left 2, just minus one number left 2(module 3) or two number left 1(module 3) 
"""

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        num,res = 0,0
        left,left2 = [],[]
        for x in nums:
            res += x
            reminder = x % 3
            if (x % 3 == 1): left.append(x)
            elif (x % 3 == 2): left2.append(x)
            num += reminder
            num %= 3
        left.sort()
        left2.sort()
        temp = 2e31
        if (num == 1):
            if len(left2) < 2 and len(left) < 1:
                return 0
            if len(left2) >= 2:
                temp = min(temp,left2[0]+left2[1])
            if len(left) >= 1:
                temp = min(temp,left[0])
            res -= temp
                
        if (num == 2):
            if len(left) < 2 and len(left2) < 1:
                return 0
            if len(left) >= 2:
                temp = min(temp,left[0]+left[1])
            if len(left2) >= 1:
                temp = min(temp,left2[0])
            res -= temp
        
        return res 
                
                
        
