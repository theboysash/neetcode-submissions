class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        curr = root 
        def dfs(curr):
            if curr is None:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            val = left + right
            self.best = max(self.best, val)
            return  1+max(left, right)
        dfs(root)
        return self.best

        
       