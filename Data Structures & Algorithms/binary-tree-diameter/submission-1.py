class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        current = root
        if current is None:
            return 0

        def solve(node):
            if node is None:
                return 0
            left = solve(node.left)
            right = solve(node.right)
            self.best = max(self.best, left + right)
            return 1 + max(left, right)
        solve(root)
        return self.best

        


        

       
       