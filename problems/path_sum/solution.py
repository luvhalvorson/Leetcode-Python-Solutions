# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return
        if not root.left and not root.right:
            if targetSum == root.val:
                return True
            else:
                return False
        
        l = self.hasPathSum(root.left, targetSum - root.val)
        if l:
            return True
        r = self.hasPathSum(root.right, targetSum - root.val)
        return r