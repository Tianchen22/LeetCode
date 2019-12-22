"""
1273. Delete Tree Nodes

https://leetcode.com/problems/delete-tree-nodes/

using [] to create a relationship linked list then dfs
"""
class Solution:
    def deleteTreeNodes(self, n: int, p: List[int], v: List[int]) -> int:
        c,root = [[] for x in p], 0
        for i,x in enumerate(p):
            if x >= 0:
                c[x].append(i)
                root = i if x == -1 else root
        def dfs(root):
            res = 1
            for x in c[root]:
                num,val = dfs(x)
                v[root] += val
                res += num if val else 0                
            return res if v[root] else 0,v[root]
        return dfs(root)[0]
