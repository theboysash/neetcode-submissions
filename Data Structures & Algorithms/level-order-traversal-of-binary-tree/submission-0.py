# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([root])
        elements = []

        while queue:
            size = len(queue)
            
            current_level = []
            for i in range(0, size):
                curr = queue.popleft()    
                current_level.append(curr.val)

                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            elements.append(current_level)
        
        return elements


        