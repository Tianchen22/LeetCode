"""
Problem link:
  https://leetcode.com/problems/check-if-it-is-a-good-array/
  
Thought:
  Chinese Remainder Theorem

* My solution is quite ugly, so just put the code from the discussion
"""
   def isGoodArray(self, A):
        gcd = A[0]
        for a in A:
            while a:
                gcd, a = a, gcd % a
        return gcd == 1

"""
  here is my code,lol
"""
	 def isGoodArray(self, nums: List[int]) -> bool:
		def gcd(a,b):
			if b == 0:
				return a
			else:
				return gcd(b,a % b)
		temp = nums[0]
		for x in nums:
			temp = gcd(temp,x)
		return temp == 1