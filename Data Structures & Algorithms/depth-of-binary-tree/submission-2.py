# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #bottom up
        curr = root
        if curr is None:
            return 0
        left = self.maxDepth(curr.left)
        right = self.maxDepth(curr.right)

        return 1 + max(left, right)
      