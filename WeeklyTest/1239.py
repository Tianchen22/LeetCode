"""
1239. Maximum Length of a Concatenated String with Unique Characters

Problem link:
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

Thought:
	Using Set list to find each existed numbers, and using bits operation "and" and "or" 
	to check if tehe same words exists twice, then put the new set into the list
	In the end, find the max length from the list
"""

class Solution(object):
    def maxLength(self, A):
        dp = [set()]
        for a in A:
            if len(set(a)) != len(a): continue
            a = set(a)
            for c in dp:
                if a & c: continue
                dp.append(a | c)
        return max(len(a) for a in dp)