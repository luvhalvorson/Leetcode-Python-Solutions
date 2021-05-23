# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l=[]
        if not root:
            return []
        else:
            if root.left:
                l += self.inorderTraversal(root.left)
            if root:
                l += [root.val]
            if root.right:
                l += self.inorderTraversal(root.right)
        return l