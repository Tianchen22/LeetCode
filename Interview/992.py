"""
992. Subarrays with K Different Integers

https://leetcode.com/problems/subarrays-with-k-different-integers/

The tricky technique is that the total substring which has exactly k different integers
is the total substring with most k integers - total substring with most k-1 integers
++ Sliding Window
"""

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:      
        return self.MostK(A,K) - self.MostK(A,K-1)
    
    def MostK(self,A,K):
        count = collections.Counter()
        res,i,j = 0,0,0
        for i in range(len(A)):
            if count[A[i]] == 0: 
                K -= 1
            count[A[i]] += 1
            while K < 0:
                count[A[j]] -= 1
                if count[A[j]] == 0: 
                    K += 1
                j += 1
            res += i - j + 1
        return res
