"""
1271. Hexspeak

https://leetcode.com/problems/hexspeak/

First need to know the hex function -> hex(247) -> '0x101' and hex(15) -> '0xF'

Second, always add the else function in x if what else!!!! otherwise will occur compile error and so damn hard to find it
"""
class Solution:
    def toHexspeak(self, num: str) -> str:
        curr = hex(int(num))[2:]
        return "ERROR" if any([1 if x not in '10abcdef' else 0 for x in curr]) 
                       else ''.join([x.upper() if x not in '10' else 'I' if x == '1' else 'O' for x in curr])
        # line 11 and line 12 are in the same line
        # and always add else!!!!!!!!! -> a if b == c else d, expression(or sentence?)
