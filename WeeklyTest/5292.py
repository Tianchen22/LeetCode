"""
https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

5292. Divide Array in Sets of K Consecutive Numbers

use Counter to total each number, and sort the array
check the smallest remaining number each time
return True if there is no numbers left
"""
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = collections.Counter(nums)
        nums.sort()
        for c in nums:
            if count[c] > 0:
                for i in range(k):
                    if count[c+i] == 0:
                        return False
                    else:
                        count[c+i] -= 1
        return True
                    