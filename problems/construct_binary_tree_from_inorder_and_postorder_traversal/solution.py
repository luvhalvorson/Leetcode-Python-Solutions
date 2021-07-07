# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        r = postorder[-1]
    
        ri = 0
        for i, n in enumerate(inorder):
            if r == n:
                ri = i
                break
        r = TreeNode(r)
        r.left = self.buildTree(inorder[:ri], postorder[:ri])
        r.right = self.buildTree(inorder[ri+1:], postorder[ri:-1])
        
        return r