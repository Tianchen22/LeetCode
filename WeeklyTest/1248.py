"""
  1248 Count Number of Nice Subarrays    
  
Problem link:
  https://leetcode.com/problems/count-number-of-nice-subarrays/
  
Thought:
  record the index of every odd position.
  ....using combination to sum the position between k
  
"""

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = []
        for i,c in enumerate(nums):
            if c % 2 == 1:
                count.append(i)
        i,res = 0,0
        while i + k - 1 < len(count):
            le,re = 0,0
            if i == 0 :
                le = count[i]
            else:
                le = count[i] - count[i-1] - 1
            if i + k == len(count):
                re = len(nums) - count[i + k - 1] - 1
            else:
                re = count[i + k] - count[i + k - 1] - 1
            res += re + le + 1 + le * re
            i += 1
        return res
