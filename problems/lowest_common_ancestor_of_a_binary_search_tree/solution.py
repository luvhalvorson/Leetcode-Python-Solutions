class TreeNode:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.l = l
        self.r = r

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # iterative
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                break
        return root
#         if p.val > q.val: p, q = q, p # this line makes it a little bit faster
#         if not root:
#             return root
#         if root is p or root is q:
#             return root
        
#         if p.val < root.val and q.val < root.val:
#             return self.lowestCommonAncestor(root.left, p, q)
#         elif p.val > root.val and q.val > root.val:
#             return self.lowestCommonAncestor(root.right, p , q)
#         else:
#             return root