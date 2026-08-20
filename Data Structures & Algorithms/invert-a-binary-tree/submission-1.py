# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current = root

        if current is None:
            return None
        #postorder

        left = self.invertTree(current.left)
        right = self.invertTree(current.right)

        current.left = right
        current.right = left

        return root
        
        