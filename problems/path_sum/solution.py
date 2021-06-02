# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        if root:
            if root.val == targetSum and not (root.left or root.right):
                #print("T")
                return True
        else:
            return False
        #print(root.val, targetSum)
        a=b=0
        
        a = self.hasPathSum(root.left, targetSum - root.val)
        b = self.hasPathSum(root.right, targetSum - root.val)
        #print(a,b)
        if a or b:
            return True
        else:
            return False