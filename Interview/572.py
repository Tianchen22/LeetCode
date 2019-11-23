"""
572. Subtree of Another Tree

https://leetcode.com/problems/subtree-of-another-tree/

first dfs to pretend every node in the tree as the root
second dfs to check if the current root equal the target

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def dfs(s,t):
            if not s and not t:
                return True
            if not s or not t or s.val != t.val:
                return False
            return dfs(s.left,t.left) and dfs(s.right,t.right)
        if s:
            if dfs(s,t):
                return True
            else:
                return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        else:
            return False