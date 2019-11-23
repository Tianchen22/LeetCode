"""
239. Sliding Window Maximum

https://leetcode.com/problems/sliding-window-maximum/

classic slide windows problem
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr, pos, res = [] , [] , []
        deltot = 0 
        for i,c in enumerate(nums):
            if (pos and pos[0] <= i - k):
                pos.pop(0)
                arr.pop(0)
            while (arr and arr[-1] < c):
                arr.pop()
                pos.pop()                
            arr.append(c)
            pos.append(i)            
            if i + 1 >= k:
                res.append(arr[0])
        return res