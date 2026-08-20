class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node is not None:
            if p.val < node.val and q.val < node.val:
                node = node.left       # both targets are smaller -> LCA must be further left
            elif p.val > node.val and q.val > node.val:
                node = node.right      # both targets are bigger -> LCA must be further right
            else:
                return node            # split (or one equals node) -> this is the LCA
        return None