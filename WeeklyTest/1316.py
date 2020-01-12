"""
1316. Distinct Echo Substrings

https://leetcode.com/problems/distinct-echo-substrings/

Set + String processing

Time complexity is O(N^2)
"""

#Solution 1
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n,res = len(text),set()
        for i in range(n):
            s,s2 = "",""
            for j in range(min(i,n-i)):
                s,s2 = s + text[i+j], text[i-j-1] + s2
                if s == s2:
                    res.add(s)
        return len(res)
        
#Solution 2 by Stefan
class Solution:
    def distinctEchoSubstrings(self, s: str) -> int:
        n,res = len(s),set()
        for i in range(n):
            for j in range(i):
                if s.startswith(s[j:i],i):
                    res.add(s[j:i])
        return len(res)
        