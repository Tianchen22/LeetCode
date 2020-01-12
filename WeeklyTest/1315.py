"""
1315. Sum of Nodes with Even-Valued Grandparent

https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

Tree simulation
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#solution 1
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root,a,b):
            if root:
                if a:
                    self.res += root.val
                dfs(root.left,b,True if root.val & 1 == 0 else False)
                dfs(root.right,b,True if root.val & 1 == 0 else False)
        dfs(root,False,False)
        return self.res
		
#solution 2		
	class Solution:
		def sumEvenGrandparent(self, root: TreeNode, a = 1, b = 1) -> int:
			return self.sumEvenGrandparent(root.left,b,root.val) + \
			self.sumEvenGrandparent(root.right,b,root.val) + \
			root.val * (1 - a % 2) if root else 0
		