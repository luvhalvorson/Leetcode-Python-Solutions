# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 and not root2:
            return None
        a, b = 0, 0
        l1, r1, l2, r2 = None, None, None,None
        if root1:
            a = root1.val
            if root1.left:
                l1 = root1.left
            if root1.right:
                r1 = root1.right
        if root2:
            b = root2.val 
            if root2.left:
                l2= root2.left
            if root2.right:
                r2 = root2.right
        new = TreeNode(a+b)
        new.left = (self.mergeTrees(l1, l2))
        new.right = (self.mergeTrees(r1, r2))
        return new 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # h1, h2 = root1, root2
#         # while h1 or h2:
#         #     if h1 and h2:
#         #         h1.val += h2.val
#         #     #elif h1:
#         #     elif h2:
#         #         h1
        
#         def help(r1, r2):
#             if not r1:
#                 return 1
#             if not r2:
#                 return 2
#             r1.val += r2.val
#             if not r1.left:
#                 r1.left = Node(r2.left.val)
#             if not r2.left:
                
#             help(r1.left, r2.left)
#             return 0
#         help(root1, root2)
            
#         return root1