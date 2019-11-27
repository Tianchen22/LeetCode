"""
1145. Binary Tree Coloring Game

https://leetcode.com/problems/binary-tree-coloring-game/

The best stageagy is to choose the point closer to the target
as 'y', which can be the parent, left child and right child of the target
then choose one point which contain the maxium number as res.
compare res > total - res 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.res = 0
        def dfs(root):
            if root:
                if root.val == x:
                    num_l , num_r = dfs(root.left), dfs(root.right)
                    self.res = max(num_l, num_r, n - num_l - num_r - 1)
                return dfs(root.left) + dfs(root.right) + 1
            else:
                return 0
        dfs(root)
        return self.res > n - self.res
