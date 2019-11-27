"""
1147. Longest Chunked Palindrome Decomposition

https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

Brute Force the string from both head and tail,
once find the same substring, the result add 2
and determine if the final res should add extra 1 (if the text is not empty or the text is odd)
"""

class Solution:
    def longestDecomposition(self, text: str) -> int:
        l,r,res = 0,len(text)-1,0
        strl,strr = "", ""
        while l < r:
            strl = strl + text[l]
            strr = text[r] + strr
            if strl == strr:
                res += 2
                strr,strl = "",""
            l += 1
            r -= 1
        if strl != "" or strr != "" or l == r:
            res += 1
        return res
        
            
