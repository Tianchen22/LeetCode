"""
5317. Delete Leaves With a Given Value

https://leetcode.com/problems/delete-leaves-with-a-given-value/

Classic Tree Simulation
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root:                  
            root.left = self.removeLeafNodes(root.left,target)
            root.right = self.removeLeafNodes(root.right,target) 
            if not root.left and not root.right and root.val == target:
                return None
            else:
                return root
        else:
            return root