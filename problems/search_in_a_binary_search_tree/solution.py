# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # if not root or (root.val == val):
        #     return root
        # if root.val < val:
        #     return self.searchBST(root.right, val)
        # elif root.val > val:
        #     return self.searchBST(root.left, val)
        if not root:
            return root
        c = root
        while c:
            if c.val == val:
                return c
            elif c.val < val:
                c = c.right
            elif c.val > val:
                c = c.left
        return None
            