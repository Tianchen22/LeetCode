"""
1317. Convert Integer to the Sum of Two No-Zero Integers

https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

Simple Simulation Question 
"""
#Solution 1 -> check:
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check(x):
            while x > 9:
                if x % 10 == 0:
                    return False
                else:
                    x //= 10
            return True if x else False
        for i in range(n):
            if check(i) and check(n-i):
                return [i,n-i]

#Solution 2 -> using f~string:
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            if '0' in f'{i}{n-i}':
                i += 1
            else:
                return [i,n-i]