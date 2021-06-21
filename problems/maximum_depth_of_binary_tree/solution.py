# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        res = 0
        def help(root, depth):
            
            if not root:
                return
            if not root.left or root.right:
                nonlocal res
                res = max(res, 1 + depth)
            help(root.left, 1 + depth)
            help(root.right, 1 + depth)

            
        help(root, 0)
        return res