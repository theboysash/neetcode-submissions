class Solution:
    def isValidBST(self, root: Optional[TreeNode], low=float('-inf'), high=float('inf')) -> bool:
        #we work with boundaries
        #if at ever condition doesnt hold, return false
        #check low < curr.left < curr 
        #check curr < curr.right < high 
        if not root:
            return True 

        if not (low<root.val<high):
            return False
        return (self.isValidBST(root.left, low, root.val) and self.isValidBST(root.right, root.val, high))