# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def ismirror(l, r):
            if not l and not r:
                return True
            if not r or not l:
                return False
            if l.val != r.val:
                return False
            if ismirror(l.left, r.right) and ismirror(l.right, r.left):
                return True

        if ismirror(root.left, root.right):
            return True
        else:
            return False

