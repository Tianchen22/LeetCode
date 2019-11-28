"""
971. Flip Binary Tree To Match Preorder Traversal

https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.count = -1
        self.res = []
        def dfs(root):
            if root:`
                self.count += 1
                if root.val != voyage[self.count]: 
                    return False
                # just need to determine if left child is not null and need to switch
                # cause if left child is null,the count for right child remain the same
                # and if left child is matched,even if right child is different we still cannot switch
                # cause that will change the match for left child
                if (root.left and root.left.val != voyage[self.count + 1]):
                    self.res.append(root.val)
                    return dfs(root.right) and dfs(root.left)
                else:
                    return dfs(root.left) and dfs(root.right)                
            else: return True
        return self.res if dfs(root) else [-1]
            
