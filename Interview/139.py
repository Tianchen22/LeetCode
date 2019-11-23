"""
139. Word Break

Probelm Link:
https://leetcode.com/problems/word-break/

Thought:
using queue to check if word start with the string, 
if true then push new substring to the queue
once one null substring shown up, return True
return False at last

** remember to use set to optimize repeatation
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        arr, used = [s] , [s]
        while len(arr) > 0:
            curr = arr[0]
            for word in wordDict:
                if curr == word:
                    return True
                if curr.startswith(word) and curr[len(word):] not in used:
                    used.append(curr[len(word):])
                    arr.append(curr[len(word):])
            arr.pop(0)
        return False