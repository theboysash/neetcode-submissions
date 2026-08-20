class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                node = queue.popleft()
                
                if i == size - 1:          # last node processed at this level
                    result.append(node.val)
                
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        
        return result