"""
1309. Decrypt String from Alphabet to Integer Mapping

https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

useful tools -> re.findall \d means the number from 0 to 9
"""
class Solution:
    def freqAlphabets(self, s: str) -> str:        
        return ''.join(chr(int(x[:2]) + 96) for x in re.findall(r"\d\d#|\d",s))
        