# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # pre: rLR
        # in: LrR
        if not preorder:
            return None
        r = TreeNode(preorder[0])
        ri = 0
        for i in range(len(inorder)):
            if inorder[i] == r.val:
                ri = i
                break
        r.left = self.buildTree(preorder[1:1+ri], inorder[:ri])
        r.right = self.buildTree(preorder[1+ri:], inorder[ri+1:])
        
        return r