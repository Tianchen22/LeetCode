"""
890. Find and Replace Pattern

https://leetcode.com/problems/find-and-replace-pattern/

Honestly, i came up with the concept of the solution but don't know how to realize it clearly and shortly.
The solution below combines the solution by lee215
->https://leetcode.com/problems/find-and-replace-pattern/discuss/161288/C%2B%2BJavaPython-Normalise-Word
"""
class Solution:
    def findAndReplacePattern(self, w: List[str], p: str) -> List[str]:
        def dic(s):
            d = {}
            return [d.setdefault(x,len(d)) for x in s]
            #e.g. s = 'abb' or 'bcc'
            #return [0,1,1]
        return [x for x in w if dic(x) == dic(p)]
        
