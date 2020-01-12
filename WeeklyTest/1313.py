"""
1313. Decompress Run-Length Encoded List

https://leetcode.com/problems/decompress-run-length-encoded-list/

use zip to put odd and even number to sequence[] is more clear and readable to the code
zip(_[0::2],_[1::2]) 

"""

class Solution:
    def decompressRLElist(self, _: List[int]) -> List[int]:
        return [x for a,b in zip(_[0::2],_[1::2]) for x in [b] * a]