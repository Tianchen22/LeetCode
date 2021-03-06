"""
1261. Find Elements in a Contaminated Binary Tree

Problem Link:
  https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/
  
Thought:
  initialize the tree,record all the shown value to an list.
  then just check if the target is in the list.
"""
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, x):
  #         self.val = x
  #         self.left = None
  #         self.right = None

  class FindElements:
      def __init__(self, root: TreeNode):
          self.set = []

          def dfs(root: TreeNode,val):
              if root:
                  root.val = val
                  self.set.append(val)
                  dfs(root.left,val * 2 + 1)
                  dfs(root.right,val * 2 + 2)
          dfs(root,0)

      def find(self, target: int) -> bool:
          return target in self.set


  # Your FindElements object will be instantiated and called as such:
  # obj = FindElements(root)
  # param_1 = obj.find(target)


