"""
5293. Maximum Number of Occurrences of a Substring

https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

Sliding window + hash map
"""
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ss,count,res,j,tot = {},{},0,0,0
        for i,c in enumerate(s):
            count[c] = count.get(c,0) + 1
            tot += 1 if count[c] == 1 else 0
            while tot > maxLetters and j < i:
                count[s[j]] -= 1
                tot -= 1 if count.get(s[j],0) == 0 else 0
                j += 1     
            curr = ""
            for k in range(i,j-1,-1):
                curr = s[k] + curr
                if len(curr) > maxSize:
                    break
                if len(curr) >= minSize:
                    ss[curr] = ss.get(curr,0) + 1
                    res = max(ss[curr],res)
        return res