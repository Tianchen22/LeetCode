"""
1268. Search Suggestions System

https://leetcode.com/problems/search-suggestions-system/

Substring Sort Question + Startswith
"""

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        arr = products
        arr.sort()
        arr2 = []
        res = []
        for i in range(len(searchWord)):
            res.append([])
            flag = False
            curr = searchWord[:i+1]
            for x in arr:
                if x.startswith(curr):
                    if len(res[i]) < 3:
                        res[i].append(x)
                    arr2.append(x)
                    flag = True
                elif flag:
                    break
            arr,arr2 = arr2 , []
        return res
