"""
1302. Deepest Leaves Sum

https://leetcode.com/problems/deepest-leaves-sum/

Simulation
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.res, self.dep = 0, 0
        def dfs(root,dep):
            if root:
                if dep > self.dep:
                    self.dep, self.res = dep, root.val
                elif dep == self.dep:
                    self.res += root.val
                dfs(root.left,dep+1)
                dfs(root.right,dep+1)
        dfs(root,0)
        return self.res