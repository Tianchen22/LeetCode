"""
5316. Print Words Vertically

https://leetcode.com/problems/print-words-vertically/

The difficulty in this question is that 
we should ignore the space in the end of each string but 
add other spaces
"""

#my solution
class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')[::-1]     
        m = max([len(w) for w in words])
        res = ["" for i in range(m)]
        for w in words:
            for i in range(m-1,-1,-1):
                res[i] = w[i] + res[i] if i < len(w) else ' ' + res[i] if res[i] else ''
        return res
		
		
#short solution using two functions to solve the "space" problems
#itertools.zip_longest is to zip each sequence the length of the max length in the list
#restrip(using in string) is to delete specfic character(space ' ' as normal) in the end of the sequence


    def printVertically(self, s):
        return [''.join(a).rstrip() for a in itertools.zip_longest(*s.split(), fillvalue=' ')]