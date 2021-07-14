# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        def help(root):
            nonlocal res
            if not root:
                return 0
            if not root.left and not root.right:
                return 0
            left, right = 0,0
            if root.left:
                left = 1 + help(root.left)
            if root.right:
                right = 1 + help(root.right)
            
            res = max(res, left + right )
            #print(res)
            return max(left, right)
        help(root)
        return res