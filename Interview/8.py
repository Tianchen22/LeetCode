"""
8. String to Integer (atoi)

https://leetcode.com/problems/string-to-integer-atoi/

Classic simulation problem
"""
class Solution:
    def myAtoi(self, str: str) -> int:
        set = "1234567890"
        res = 0
        first,negative = True,False
        minvalue = -2147483648
        maxvalue = 2147483647
        def solve(n,negative):
            if negative:
                return -n
            else:
                return n
        for x in str:
            if first and x == ' ':
                continue
            if first and (x in set or x in '+-'):
                first = False
                if x == '-':
                    negative = True
                elif x == '+':
                    negative = False
                else:
                    res = ord(x) - 48
                continue
            if x not in set:
                return solve(res,negative)
            res = res * 10 + ord(x) - 48
            if solve(res,negative) > maxvalue:
                return maxvalue
            if solve(res,negative) < minvalue:
                return minvalue
        return solve(res,negative)