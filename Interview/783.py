"""
783. Minimum Distance Between BST Nodes

https://leetcode.com/problems/minimum-distance-between-bst-nodes/

use list to save all the value, sort it and find the min one
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.arr = []
        def dfs(root):
            if root:
                self.arr.append(root.val)
                dfs(root.right),dfs(root.left)
        dfs(root)
        self.arr.sort()
        return min([self.arr[i] - self.arr[i-1] for i in range(1,len(self.arr))])
                
        
