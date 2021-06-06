# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        if not root:
            return True
       
        res = True
        def maxheight(root):
            if not root:
                return 0
            
            l = maxheight(root.left)
            r = maxheight(root.right)
            if  l== -1 or  r == -1 or abs(l-r) >1:
                return -1
            return max(l, r) + 1
        
        

        return maxheight(root)!=-1