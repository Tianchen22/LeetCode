"""
1310. XOR Queries of a Subarray

https://leetcode.com/problems/xor-queries-of-a-subarray/

convert the meaning of arr[i] -> total of xor operations from index 0 to i
so the xor from [a,b] can be converted to the arr[b] ^ arr[a-1]
"""
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1,len(arr)):
            arr[i] ^= arr[i-1]
        return [arr[j] ^ (arr[i - 1] if i else 0) for i,j in queries]