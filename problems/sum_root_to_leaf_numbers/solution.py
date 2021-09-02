# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root, path):
            nonlocal res
            if not root.left and not root.right:                
                res += int(path)
                return
            
            if root.left:
                dfs(root.left, path + str(root.left.val))
            
            if root.right:
                dfs(root.right, path + str(root.right.val))
            
        dfs(root, str(root.val))
        return res