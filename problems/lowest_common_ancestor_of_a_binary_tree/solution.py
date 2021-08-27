# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root):
            if not root:
                return False
            l = helper(root.left)
            r = helper(root.right)
            if root is q or root is p:
                if l + r == 1:
                    self.ans = root
            else:
                if l + r  == 2:
                    self.ans = root
            return (root is q) or (root is p) or l or r
        helper(root)
        return self.ans
                